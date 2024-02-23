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
        id = uuid.uuid4() #乱数によりOSを利用して一意なidを設定
        password = hashlib.sha256(password.encode('utf-8')).hexdigest() #passwordをハッシュ化
        DBuser = dbConnect.getUser(email) #フォームに入力したアドレスが登録されている行をデータベースから呼び出す。無ければNoneが返る

        if DBuser != None: #登録されているメーアドレスが一意であるかの確認
            flash('このめーるあどれすはすでに登録されているようです')
        else:
            dbConnect.createUser(id, name, email, password)
            UserId = str(id) #uidを文字列に変換
            session['id'] = UserId #セッションにユーザーIDを保存、保持したい情報を辞書データとして登録
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
            hashPassword = hashlib.sha256(password.encode('etf-8')).hexdigest()#passwordをハッシュ化
            if hashPassword != user["password"]:#取り出した行のpasswordと一致するか
                flash('ぱすわーどが間違っています')
            else:
                session['id'] = user["id"]#セッションにユーザーIDを保存、保持したい情報を辞書データとして登録
                return redirect('/')


## ログアウト
@app.route('/logout')
def logout():
    session.clear()#セッション情報を削除
    return redirect('/login')#ログイン画面へ遷移する


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

