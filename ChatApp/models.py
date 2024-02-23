import pymysql

#util/DB.pyからインポート　def getConnection()
from util.DB import DB

# データベースに接続し、ユーザーを新規登録する
class dbConnect:
    def createUser(uid, name, email, password):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email password) VALUES (%s, $s, %s, %s);"
            cur.execute(sql, (uid, name, email, password))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)


# データベースに接続し、フォームに入力されたメールアドレスが登録されているuserテーブルの行を取り出す
    def getUser(email):
        try:
            conn = DB.getConnectinon()
            cur = conn.cursor()
            sql = "SELECT * FROM user WHERE email=%s;" #usersのテーブルからemailの行を取り出す
            cur.execute(sql, (email))
            user = cur.fetchone()
        except Exception as e:
            print(e + "が発生しています")
            abort(500)
        finally:
            cur.close()

def createMessage(uid, cid, message):
    # tryブロックを使用して、データベースへの接続と操作を試みる
    try:
        # データベース接続を取得
        conn = DB.getConnection()
        # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
        cur = conn.cursor()
        # SQL文を定義
        sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
        # executeメソッドを使用してSQL文を実行。プレースホルダーにはuid, cid, messageの値を渡す
        cur.execute(sql, (uid, cid, message))
    except Exception as e:
        # エラーが発生した場合、エラーメッセージを出力
        print(str(e) + 'が発生しています')
        # エラーが発生した場合は、Noneを返す

    finally:
        # finallyブロックは、tryブロックの実行が成功したか、エラーが発生したかに関わらず実行
        # カーソルオブジェクトを閉じる
        cur.close()

def getMessageAll(cid):
    # tryブロックを使用して、データーベースへの接続と操作を試みる
    try:
        # データベース接続を取得
        conn = DB.getConnection()
        # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
        cur = conn.cursor()
        # SQL文を定義。このSQL文では、指定されたcidに対するメッセージとそれに関連するユーザー情報を取得
        sql = "SELECT id, u.uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid = u.id WHERE cid = %s;"
        # executeメソッドを使用してSQL文を実行
        # cidの値をSQLクエリのパラメータとして渡す
        cur.execute(sql, (cid,))
        # fetchallメソッドを使用してクエリ結果の全ての行を取得
        messages = cur.fetchall()
        # 取得したメッセージ情報を返す
        return messages
    except Exception as e:
        # エラーが発生した場合、エラーメッセージを出力
        print(str(e) + 'が発生しています')
        # エラーが発生した場合はNoneを返す
        return None
    finally:
        # finallyブロックは、tryブロックの実行が成功したか、エラーが発生したかに関わらず実行
        # カーソルオブジェクトを閉じる
        cur.close()




def getChannelById(uid):
    try:
        # データベースへの接続を確立
        conn = DB.getChnnection()
        # カーソルを作成
        cur = conn.cursor()
        # 実行するSQL文を定義。ここでは指定されたidを持つチャンネルを検索
        sql = "SELECT * FROM channels WHERE id=%s;"
        # SQL文を実行。パラメータとしてuidを渡す
        cur.execute(sql, (uid,))
        # 結果を取得
        channel = cur.fetchone()
        # 取得したチャンネル情報を返す
        return channel
    except Exception as e:
        # 例外が発生した場合、エラーをコンソールに出力
        print(str(e) + 'が発生しています')
        # 例外が発生した場合はNoneを返す
        return None
    finally:
        # 最後に必ずカーソルを閉じる
        cur.close()
