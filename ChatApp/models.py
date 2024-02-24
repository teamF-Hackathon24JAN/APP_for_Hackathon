import pymysql

#util/DB.pyからインポート　def getConnection()
from util.DB import DB

# データベースに接続し、ユーザーを新規登録する
class dbConnect:
    def createUser(id, name, email, password):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (id, name, email, password) VALUES (%s, $s, %s, %s);"
            cur.execute(sql, (id, name, email, password))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# データベースに接続し、フォームに入力されたメールアドレスが登録されているuserテーブルの行を取り出す
    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM user WHERE email=%s;" #usersのテーブルからemailの行を取り出す
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + "が発生しています")
        finally:
            cur.close()