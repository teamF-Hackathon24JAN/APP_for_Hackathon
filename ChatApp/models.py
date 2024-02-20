import pymysql
from util.DB import DB #util/DB.pyからインポート　def getConnection()

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