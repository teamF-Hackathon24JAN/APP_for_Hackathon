from flask import Flask, request, redirect, render_template, session, flash, abort
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

#models.pyで定義したクラスdbConnectを呼び出す
from models import dbConnect


app = Flask(__name__) #Flaskクラスのインスタンスを作る
app.secret_key = uuid.uuid4().hex #uuid=(universal unique identifer)36文字の英数字からなる一意の識別子、sessionを暗号化するための鍵を設定
app.permanent_session_lifetime = timedelta(days = 30) #sessionの有効期限を定める　30日間


# # サインアップページの表示
@app.route('/signup', methods=['GET']) #ルーティングURLと処理を対応づける、methodを指定しないと、デフォルトでGETリクエストがルーティングされる
def signup():
    return render_template('registration/signup.html') #htmlを読み込んで返す

# # サインアップ処理
@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name') #フォームからnameを取得
    email = request.form.get('email') #フォームからemailを取得
    password = request.form.get('password') #フォームからpasswordを取得

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
            dbConnect.createUser(session_id, name, email, password)
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

#（仮あとで削除）ログイン前、ログイン後のホーム表示
@app.route('/')
def home():
    session_id = session.get("session_id")
    if session_id is None:
        return redirect('/login')
    else:
        return render_template('home.html')

# 設定ページの表示
@app.route('/setting')
def index():
    session_id = session.get("session_id")
    if session_id is None:
        return redirect('/login')
    else:
        user_id = dbConnect.getUserID(session_id)
        channels = dbConnect.getChannelAll()
        channels.reverse()
    return render_template('index.html', channels=channels, user_id=user_id)


## ログアウト
@app.route('/logout')
def logout():
    session.clear()#セッション情報を削除
    return redirect('/login')#ログイン画面へ遷移する


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

# # メッセージ作成機能
@app.route('/message', methods=['POST'])
def add_message():
    session_id = session.get("session_id")
    # ユーザーがログインしていない場合は、ログインページにリダイレクトする
    if not session_id:
        return redirect('/login')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')
    user_id = dbConnect.getSerialID(session_id)
    
    # メッセージが存在する場合のみ、データベースにメッセージを追加
    if message:
        dbConnect.createMessage(user_id, channel_id, message)
    else:
        # メッセージが空の場合は、エラーメッセージと共に元のページに戻る
        return redirect('/error_page') 

    # チャンネル情報とそのチャンネルのメッセージを取得してテンプレートに渡す
    channel = dbConnect.getChannelById(channel_id)
    message = dbConnect.getMessageAll(channel_id)
    
    return render_template('detail.html', message=message, channel=channel, user_id=user_id)

# # メッセージ一覧機能
@app.route('/detail/<channel_id>')
def detail(channel_id):
    # 現在のセッションからユーザーID ('uid') を取得
    session_id = session.get("session_id")
    
    # もしユーザーIDが存在しない場合、ユーザーがログインしていない場合は、ログインページにリダイレクト
    if session is None:
        return redirect('/login')
    
    #user_idを取得
    user_id = dbConnect.getSerialID(session_id)  

    # パスパラメーターから取得したチャンネルIDを使用し、チャンネルの情報をデータベースから取得
    channel = dbConnect.getChannelById(channel_id)
    
    # 指定されたチャンネルIDに関連する全てのメッセージを取得
    messages = dbConnect.getMessageAll(channel_id)

    #ユーザーIDを取得
    user_id = dbConnect.getSerialID()

    # 取得したチャンネル情報とメッセージ、ユーザーIDをdetail.htmlテンプレートに渡し、そのテンプレートを使用してレンダリングしたページを返す
    return render_template('detail.html', message=message, channel=channel, user_id=user_id)

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



# # チャンネル作成機能
@app.route('/', methods=['post'])
def add_channel():
    # セッションからuidを取得
    session_id = session.get('session_id')

    # uidがNoneだった場合ログインページにリダイレクト
    if session_id is None:
        return redirect('/login')
    
    #user_idを取得
    user_id = dbConnect.getSerialID(session_id)

    # フォームからチャンネル名を取得
    channel_name = request.form.get('channel-title')
    # データベースからチャンネル名で検索
    channel = dbConnect.getChannelByName(channel_name)

    # もしチャンネルが存在しない場合
    if channel == None:
        # フォームからチャンネルの説明を取得
        channel_description = request.form.get('channel-description')
        # 新しいチャンネルをデータベースに追加
        dbChannel.addChannel(user_id, channel_name, channel_description)
        # ホームページにリダイレクト
        return redirect('/')
    else:
        # もしチャンネルがすでに存在する場合エラーメッセージを表示
        error = 'すでに同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)
