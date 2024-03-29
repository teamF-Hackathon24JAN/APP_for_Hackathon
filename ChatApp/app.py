from flask import Flask, request, redirect, render_template, session, flash, abort, url_for, jsonify
# Flask ルーティング
# request データを受け取る、取得、参照
# redirect 自動的に指定した他のページに転送
# render_template　templaetsフォルダ内にあるテンプレートファイル名を指定して読み込む、テンプレートにパラメータを渡すこともできる
# session セッションの管理
# flash　フラッシュ表示する
# abort　http通信が失敗した際にhttpステータスとメッセージを返却する
from datetime import timedelta #timedeltaは経過時間、二つの日付や時刻間の差を表す
import hashlib #外部に漏れてほしくないデータを固定の長さの値に変換（ハッシュ化）するモジュール
import uuid #universal unique identifer 一意な識別子を生成する
import re #正規表現モジュール　文字列内で文字の組み合わせを照合するために用いるパターンを扱う
import time
import json

#models.pyで定義したクラスdbConnectを呼び出す
from models import dbConnect
from s3 import awsConnect


app = Flask(__name__) #Flaskクラスのインスタンスを作る
app.secret_key = uuid.uuid4().hex #uuid=(universal unique identifer)36文字の英数字からなる一意の識別子、sessionを暗号化するための鍵を設定
app.permanent_session_lifetime = timedelta(days = 30) #sessionの有効期限を定める　30日間


# ルート直下の処理（セッション確保時はhome、ない場合はloginへ遷移
@app.route('/')
def route():
    session_id = session.get("session_id")
    if session_id is None:
        return redirect('/login')
    else:
        return redirect('/home')

# # サインアップページの表示
@app.route('/signup') #ルーティングURLと処理を対応づける、methodを指定しないと、デフォルトでGETリクエストがルーティングされる
def signup():
    return render_template('registration/signup.html') #htmlを読み込んで返す

# # サインアップ処理
@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name') #フォームからnameを取得
    email = request.form.get('email') #フォームからemailを取得
    password = request.form.get('password') #フォームからpasswordを取得
    picture = "https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG"
    one_phrase = "ひとこと が とうろく されていません"

    pattern = "^[a-z0-9_+-]+(\.[a-z0-9_+-]+)*[a-z0-9_+-]+@[a-z]+(\.[a-z]+)*\.[a-z]+$" #正規表現でemailアドレスの形式を指定
    
    if name == '' or email == '' or password == '':
        flash('からのふぉーむがあるようです')
    elif re.match(pattern, email) is None: #文字列の先頭が一致しているかどうか、先頭にマッチする文字列がない場合はNoneを返す
        flash('正しいめーるあどれすの形式ではありません')
    else:
        session_id = uuid.uuid4() #乱数によりOSを利用して一意なidを設定
        password = hashlib.sha256(password.encode('utf-8')).hexdigest() #passwordをハッシュ化
        DBuser = dbConnect.getUser(email) #フォームに入力したアドレスが登録されている行をデータベースから呼び出す。無ければNoneが返る

        if DBuser != None: #登録されているメーアドレスが一意であるかの確認
            flash('このめーるあどれすはすでに登録されているようです')
        else:
            dbConnect.createUser(session_id, name, email, password, picture, one_phrase)
            UserId = str(session_id) #session_idを文字列に変換
            session['session_id'] = UserId #セッションにユーザーIDを保存、保持したい情報を辞書データとして登録
            return redirect('/') #新規登録完了後、セッションを保持した状態で'/'へ遷移
    return redirect('/signup') #/signupにリダイレクト

##ログインページの表示
@app.route('/login')
def login():
    return render_template('registration/login.html')

##ログイン処理
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')#フォームから送信されたパスワードを変数emailに格納
    password = request.form.get('password')#フォームから送信されたパスワードを変数passwordに格納

    if email =='' or password == '':
        flash('からのふぉーむがあるようです')
    else:
        user = dbConnect.getUser(email)#userテーブルから変数emailがある行を取り出す
        if user is None:
            flash('このゆーざーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()#passwordをハッシュ化
            if hashPassword != user["password"]:#取り出した行のpasswordと一致するか
                flash('ぱすわーどが間違っています')
            else:
                session['session_id'] = user["session_id"]#セッションにセッションIDを保存、保持したい情報を辞書データとして登録
                return redirect('/')

# パスワード再設定
@app.route('/passwordlost')
def passwordlost():
    #フォームから送信されたパスワードを変数emailに格納
    email = request.form.get('email')
    password = request.form.get('password')
    #user = dbConnect.getUser(email)

    #if user is not None:
    #    flash('')




    return render_template('/registration/passwordlost.html')

# ログアウト、セッションクリア
@app.route('/logout')
def logout():
    session.clear()#セッション情報を削除
    return redirect('/login')#ログイン画面へ遷移する

# ホームへの遷移
@app.route('/home')
def home():
    session_id = session.get("session_id")
    if session_id is None:
        return redirect('/login')
    else:
        #ユーザー情報の取得
        user = dbConnect.getUserBySessionID(session_id)
        user_id = user["id"]
        #フレンド情報の取得
        #辞書型friends{id, friend_id, friend_name, friend_one_phrase, friend_picture}
        friends = dbConnect.getFriendAll(user_id)
        # friendsをjson形式へ
        friends_json = json.dumps(friends, default=str)
        #チャンネル情報の取得
        #辞書型friends{user_id, user_name, channel_id, channel_name, description}
        channels = dbConnect.getJoinedChannelById(user_id)

        return render_template('home.html', user=user, friends=friends, channels=channels, friends_json=friends_json)

# # チャンネル作成機能
@app.route('/home', methods=['POST'])
def add_channel():
    # セッションからuidを取得
    session_id = session.get('session_id')
    # uidがNoneだった場合ログインページにリダイレクト
    if session_id is None:
        return redirect('/login')
    
    else:
        #user_idを取得
        user = dbConnect.getUserBySessionID(session_id)
        user_id = user["id"]
        owner_id = user_id

        # フォームからフォームから検索したユーザーIDを取得
        friend_id = request.form.get('friend_id')
        # フォームからチャンネル名を取得
        channel_name = request.form.get('channel_name')
        description = request.form.get('channel_description')
        friend_ids = dbConnect.getFriendIdAll(user_id)

        if friend_id is not None:
            # 自分のフレンドIDを入力した場合
            if str(user_id) == str(friend_id):
                pass
            else:
                # 検索したIDをフレンドIDとして追加
                dbConnect.addFriend(user_id, friend_id)
                # 相手のフレンド欄に自分を追加
                dbConnect.addFriend(friend_id, user_id)
        else:
            pass

        if channel_name is not None:   
            # 新しいチャンネルをデータベースに追加
            dbConnect.createChannel(channel_name, description, owner_id)
            # 新しいチャンネルのシリアルIDを取得
            channel_id = dbConnect.getCreatedChannelId(channel_name, owner_id)
            # 新しいチャンネルに自分を追加
            dbConnect.insertMe(user_id, channel_id)
        else:
            pass

        # ホームページにリダイレクト
        return redirect('/home')

@app.route('/setting', methods=['POST'])
def add_phrase():

    # セッションからuidを取得
    session_id = session.get('session_id')

    # uidがNoneだった場合ログインページにリダイレクト
    if session_id is None:
        return redirect('/login')
    
    else:
        #user_idを取得
        user = dbConnect.getUserBySessionID(session_id)
        user_id = user["id"]

        # 各フォームから情報を取得
        name = request.form.get('name')
        one_phrase = request.form.get('one_phrase')
        email = request.form.get('email')
        password = request.form.get('password')
        phrase = request.form.get('fixed_phrase')
        delete_phrase_id = request.form.get('phrase_id')


        # 画像ファイル変更機能
        if 'image' in request.files:

            # ファイルオブジェクトを取得
            file = request.files['image']

            if file is not None:
                # ファイル名を取得
                file_name = file.filename

                # boto3でイメージファイルをs3へアップロード
                object_url = awsConnect.uploadImage(file, file_name, user_id)
                # オブジェクトURLをusers(picture)に格納
                dbConnect.updateUserPicuture(object_url, user_id)
            else:
                pass

        else:
            #名前の変更機能
            if name is not None:
                dbConnect.updateUserName(name, user_id)
            else:
                pass

            #ひとことの変更機能
            if one_phrase is not None:
                dbConnect.updateOnePhrase(one_phrase, user_id)
            else:
                pass

            #メールアドレスの変更機能
            if email is not None:
                dbConnect.updateUserEmail(email, user_id)
            else:
                pass

            #パスワードの変更機能
            if password is not None:
                dbConnect.updateUserPassword(password, user_id)
            else:
                pass

            #定型文の追加機能
            if phrase is not None:
                # 新しい定型文をデータベースに追加
                dbConnect.createFixedPhrase(user_id, phrase)
            else:
                pass

            #定型文の削除機能
            if delete_phrase_id is not None:
                # 新しい定型文をデータベースに追加
                dbConnect.deleteFixedPhrase(delete_phrase_id)
            else:
                pass
        
        # 設定にリダイレクト
        return redirect('/setting')

# 設定ページの表示
@app.route('/setting')
def setting():
    session_id = session.get("session_id")
    if session_id is None:
        return redirect('/login')
    
    else:
        #自分のユーザー情報を取得
        # 辞書型users{id, session_id, name, email, password, picure, birthday, one_phrase}
        user = dbConnect.getUserBySessionID(session_id)
        user_id = user["id"]
        #自分のユーザーIDに紐づく定型文を取得
        fixed_phrases = dbConnect.getFixedPhraseAll(user_id)

        #channels.reverse()
    return render_template('/setting.html', user=user, fixed_phrases=fixed_phrases)

# メッセージ作成機能
@app.route('/chatpage/<channel_id>', methods=['POST'])
def add_message(channel_id):
    session_id = session.get("session_id")
    # ユーザーがログインしていない場合は、ログインページにリダイレクトする
    if session_id is None:
        return redirect('/login')
    else:
        pass

    user = dbConnect.getUserBySessionID(session_id)
    user_id = user["id"]

    message = request.form.get('message')
    member_id = request.form.get('member_id')

    channel_name = request.form.get('channel_name')
    channel_description = request.form.get('channel_description')
    
    
    if message is not None:
    # メッセージが存在する場合のみ、データベースにメッセージを追加
        if message == "":
            pass
        else:
            dbConnect.createMessage(user_id, channel_id, message)
    else:
        pass
    # チャンネル情報が変更された際にデータベースを変更
    if channel_name or channel_description is not None:
        dbConnect.updateChannel(channel_name, channel_description, channel_id)
    else:
        pass
    # チャンネルメンバーを追加
    if member_id is not None:   
        dbConnect.addChannelMenber(member_id, channel_id)
    else:
        pass    
    
    return redirect(url_for('chatpage', channel_id=channel_id))

# # チャットページ、
@app.route('/chatpage/<channel_id>')
def chatpage(channel_id):
    # 現在のセッションからユーザーID ('uid') を取得
    session_id = session.get("session_id")
    
    # もしユーザーIDが存在しない場合、ユーザーがログインしていない場合は、ログインページにリダイレクト
    if session is None:
        return redirect('/login')
    
    # user_idを取得
    user = dbConnect.getUserBySessionID(session_id)
    user_id = user["id"]
    # channel_memberを取得
    members = dbConnect.getChannelMemberAll(channel_id)
    # パスパラメーターから取得したチャンネルIDを使用し、チャンネルの情報をデータベースから取得
    # 辞書型channel{id, name, description, owner_id}
    channel = dbConnect.getChannelById(channel_id)
    # 指定されたチャンネルIDに関連する全てのメッセージを取得
    messages = dbConnect.getMessageAll(channel_id)
    #自分のユーザーIDに紐づく定型文を取得
    fixed_phrases = dbConnect.getFixedPhraseAll(user_id)

    # メッセージテーブルがNoneの場合、空のカラムを渡す
    if messages is None:
        messages = []
    else:
        pass
    
    return render_template(
        'chatpage.html', 
        fixed_phrases=fixed_phrases, 
        channel=channel, 
        messages=messages, 
        members=members, 
        user_id=user_id
        )

# メッセージの削除
@app.route('/delete_message', methods=['POST'])
def delete_message():
    session_id = session.get("session_id")
    if session_id is None:
        return redirect('/login')

    message_id = request.form.get('message_id')
    channel_id = request.form.get('channel_id')

    # message_idの存在を確認し、あるならば（True）メッセージの削除関数を実行
    if message_id:
        dbConnect.deleteMessage(message_id)

    #　メッセージの削除後にチャンネル詳細を再表示
    return redirect('/detail/{channel_id}'.format(channel_id = channel_id))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)