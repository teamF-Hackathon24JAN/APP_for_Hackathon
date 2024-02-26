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
        #uid = uuid.uuid4() #乱数によりOSを利用して一意なidを設定
        password = hashlib.sha256(password.encode('utf-8')).hexdigest() #passwordをハッシュ化
        DBuser = dbConnect.getUser(email) #フォームに入力したアドレスが登録されている行をデータベースから呼び出す。無ければNoneが返る

        if DBuser != None: #登録されているメーアドレスが一意であるかの確認
            flash('このめーるあどれすはすでに登録されているようです')
        else:
            dbConnect.createUser(id, name, email, password)
            #UserId = str(id) #uidを文字列に変換
            session['id'] = UserId #セッションにユーザーIDを保存、保持したい情報を辞書データとして登録
            return redirect('/') #新規登録完了後、セッションを保持した状態で'/'へ遷移
    return redirect('/signup') #/signupにリダイレクト

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)


from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)

# # メッセージ作成機能
@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    # ユーザーがログインしていない場合は、ログインページにリダイレクトする
    if not uid:
        return redirect('/login')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')
    
    # メッセージが存在する場合のみ、データベースにメッセージを追加
    if message:
        dbConnect.createMessage(uid, channel_id, message)
    else:
        # メッセージが空の場合は、エラーメッセージと共に元のページに戻る
        return redirect('/error_page') 

    # チャンネル情報とそのチャンネルのメッセージを取得してテンプレートに渡す
    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)
    
    return render_template('detail.html', messages=messages, channel=channel, uid=uid)

# # メッセージ一覧機能
@app.route('/detail/<cid>')
def detail(cid):
    # 現在のセッションからユーザーID ('uid') を取得
    uid = session.get("uid")
    
    # もしユーザーIDが存在しない場合、ユーザーがログインしていない場合は、ログインページにリダイレクト
    if uid is None:
        return redirect('/login')
    
    # パスパラメーターから取得したチャンネルIDを使用し、チャンネルの情報をデータベースから取得
    channel = dbConnect.getChannelById(cid)
    
    # 指定されたチャンネルIDに関連する全てのメッセージを取得
    messages = dbConnect.getMessageAll(cid)

    # 取得したチャンネル情報とメッセージ、ユーザーIDをdetail.htmlテンプレートに渡し、そのテンプレートを使用してレンダリングしたページを返す
    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


# # チャンネル作成機能
@app.route('/', methods=['post'])
def add_channel():
    # セッションからuidを取得
    uid = session.get('uid')
    print(uid)
    # uidがNoneだった場合ログインページにリダイレクト
    if uid is None:
        return redirect('/login')
    # フォームからチャンネル名を取得
    channel_name = request.form.get('channel-title')
    # データベースからチャンネル名で検索
    channel = dbConnect.getChannelByName(channel_name)

    # もしチャンネルが存在しない場合
    if channel == None:
        # フォームからチャンネルの説明を取得
        channel_description = request.form.get('channel-description')
        # 新しいチャンネルをデータベースに追加
        dbChannel.addChannel(uid, channel_name, channel_description)
        # ホームページにリダイレクト
        return redirect('/')
    else:
        # もしチャンネルがすでに存在する場合エラーメッセージを表示
        error = 'すでに同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)
    

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
db = SQLAlchemy(app)

class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

@app.route('/phrases', methods=['GET'])
def get_phrases():
    phrases = Phrase.query.all()
    return jsonify([phrase.text for phrase in phrases])

@app.route('/phrases', methods=['POST'])
def add_phrase():
    data = request.get_json()
    new_phrase = Phrase(text=data['text'])
    db.session.add(new_phrase)
    db.session.commit()
    return jsonify({'message': 'Phrase added'}), 201

@app.route('/phrases/<int:id>', methods=['DELETE'])
def delete_phrase(id):
    phrase = Phrase.query.get(id)
    if not phrase:
        return jsonify({'message': 'Phrase not found'}), 404
    db.session.delete(phrase)
    db.session.commit()
    return jsonify({'message': 'Phrase deleted'}), 200




from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# データベース設定（例: SQLite）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class FixedPhrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    phrase = db.Column(db.String(255), nullable=False)

# データベース初期化用ルート（本番環境では削除またはコメントアウト）
@app.route('/initdb')
def initdb():
    db.create_all()
    return "データベースが初期化されました。"






# # 定型文の追加、編集、削除

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)
# データベース設定をアプリケーションに設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
# SQLAlchemyオブジェクトを初期化
db = SQLAlchemy(app)

# 定型文を保持するデータモデル
class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主キーとしてのID
    text = db.Column(db.String(255), nullable=False)  # 定型文のテキスト

# 定型文の一覧を取得するエンドポイント
@app.route('/phrases', methods=['GET'])
def get_phrases():
    phrases = Phrase.query.all()  # データベースからすべての定型文を取得
    return jsonify([phrase.text for phrase in phrases])  # 定型文のリストをJSON形式で返す

# 新しい定型文を追加するエンドポイント
@app.route('/phrases', methods=['POST'])
def add_phrase():
    data = request.get_json()  # リクエストボディからJSONデータを取得
    new_phrase = Phrase(text=data['text'])  # 新しいPhraseオブジェクトを作成
    db.session.add(new_phrase)  # データベースセッションに追加
    db.session.commit()  # 変更をデータベースにコミット
    return jsonify({'message': '定型文が追加されました。'}), 201  # 成功メッセージを返す

# 特定の定型文を更新するエンドポイント
@app.route('/phrases/<int:id>', methods=['PUT'])
def update_phrase(id):
    data = request.get_json()  # リクエストボディからJSONデータを取得
    phrase = Phrase.query.get(id)  # IDに基づいて定型文を取得
    if not phrase:
        return jsonify({'message': '定型文が見つかりません。'}), 404  # 定型文が見つからない場合はエラーを返す
    phrase.text = data['text']  # 定型文のテキストを更新
    db.session.commit()  # 変更をデータベースにコミット
    return jsonify({'message': 'Phrase updated'}), 200  # 成功メッセージを返す

# 特定の定型文を削除するエンドポイント
@app.route('/phrases/<int:id>', methods=['DELETE'])
def delete_phrase(id):
    phrase = Phrase.query.get(id)  # IDに基づいて定型文を取得
    if not phrase:
        return jsonify({'message': '定型文が見つかりません。'}), 404  # 定型文が見つからない場合はエラーを返す
    db.session.delete(phrase)  # 定型文をデータベースから削除
    db.session.commit()  # 変更をデータベースにコミット
    return jsonify({'message': '定型文が削除されました。'}), 200  # 成功メッセージを返す

# アプリケーションを実行
if __name__ == '__main__':
    app.run(debug=True)