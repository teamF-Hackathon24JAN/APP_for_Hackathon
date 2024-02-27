import pymysql

#util/DB.pyからインポート　def getConnection()
from util.DB import DB

# データベースに接続し、ユーザーを新規登録する
class dbConnect:
    def createUser(session_id, name, email, password, picture, one_phrase):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (session_id, name, email, password, picture, one_phrase) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(sql, (session_id, name, email, password, picture, one_phrase))
            conn.commit()
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cur.close()

# データベースに接続し、フォームに入力されたメールアドレスが登録されているuserテーブルの行を取り出す
    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;" #usersのテーブルからemailの行を取り出す
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cur.close()
    
#session_IDからuser(usersテーブル)を取得する
    def getUserBySessionID(session_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE session_id = %s;"
            cur.execute(sql, (session_id))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(str(e) + 'が発生しています')
            return None
        finally:
            cur.close()

#channelテーブルのチャンネル名から該当した行を取り出す
    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()

# フレンド追加機能、検索したユーザーのIDを格納
    def addFriend(user_id, friend_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO friends (user_id, friend_id) VALUES (%s, %s);"
            cur.execute(sql, (user_id, friend_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()
    
# フレンド一覧機能、自分のuser_idに紐付けされているfriend_idを一覧で引き出す
    def getFriendAll(user_id):
    # tryブロックを使用して、データーベースへの接続と操作を試みる
        try:
            # データベース接続を取得
            conn = DB.getConnection()
            # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
            cur = conn.cursor()
            # SQL文を定義
            sql = "SELECT id, friend_id, u.name AS friend_name, u.one_phrase AS friend_one_phrase, u.picture AS friend_picture FROM friends AS f INNER JOIN users AS u ON f.friend_id = u.id WHERE user_id = %s;"
            # executeメソッドを使用してSQL文を実行
            cur.execute(sql, (user_id))
            # fetchallメソッドを使用してクエリ結果の全ての行を取得
            friends = cur.fetchall()
            # 取得した情報を返す
            return friends
        except Exception as e:
            # エラーが発生した場合、エラーメッセージを出力
            print(str(e) + 'が発生しています')
            # エラーが発生した場合はNoneを返す
            return None
        finally:
            # finallyブロックは、tryブロックの実行が成功したか、エラーが発生したかに関わらず実行
            # カーソルオブジェクトを閉じる
            cur.close()

# 自分が登録した定型文テーブルを取得する
    def getFixedPhraseAll(user_id):
     # tryブロックを使用して、データーベースへの接続と操作を試みる
        try:
            # データベース接続を取得
            conn = DB.getConnection()
            # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
            cur = conn.cursor()
            # SQL文を定義
            sql = "SELECT id, user_id, fixed_phrase FROM fixed_phrases WHERE user_id = %s;"
            # executeメソッドを使用してSQL文を実行
            cur.execute(sql, (user_id))
            # fetchallメソッドを使用してクエリ結果の全ての行を取得
            fixed_phrases = cur.fetchall()
            # 取得した情報を返す
            return fixed_phrases
        except Exception as e:
            # エラーが発生した場合、エラーメッセージを出力
            print(str(e) + 'が発生しています')
            # エラーが発生した場合はNoneを返す
            return None
        finally:
            # finallyブロックは、tryブロックの実行が成功したか、エラーが発生したかに関わらず実行
            # カーソルオブジェクトを閉じる
            cur.close()


    def createMessage(user_id, cid, message):
    # tryブロックを使用して、データベースへの接続と操作を試みる
        try:
            # データベース接続を取得
            conn = DB.getConnection()
            # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
            cur = conn.cursor()
            # SQL文を定義
            sql = "INSERT INTO messages(user_id, channel_id, message) VALUES(%s, %s, %s)"
            # executeメソッドを使用してSQL文を実行。プレースホルダーにはuid, cid, messageの値を渡す
            cur.execute(sql, (user_id, cid, message))
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
            
#メッセージの削除
    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            abort(500)
        finally:
            cur.close

# 自分が参加しているチャンネルを取得
    def getJoinedChannelById(user_id):
        try:
            # データベースへの接続を確立
            conn = DB.getConnection()
            # カーソルを作成
            cur = conn.cursor()
            # 実行するSQL文を定義。ここでは指定されたidを持つチャンネルを検索
            sql = "SELECT user_id, u.name as user_name, channel_id, c.name as channel_name, c.description FROM channels_users AS cs INNER JOIN users AS u ON cs.user_id = u.id INNER JOIN channels AS c ON cs.channel_id = c.id WHERE cs.user_id = %s;"
            # SQL文を実行。パラメータとしてuidを渡す
            cur.execute(sql, (user_id,))
            # 結果を取得
            channels = cur.fetchall()
            # 取得したチャンネル情報を返す
            return channels
        except Exception as e:
            # 例外が発生した場合、エラーをコンソールに出力
            print(str(e) + 'が発生しています')
            # 例外が発生した場合はNoneを返す
            return None
        finally:
            # 最後に必ずカーソルを閉じる
            cur.close()

# チャンネル参加者を取得
    def getChannelMemberAll(channel_id):
        try:
            # データベースへの接続を確立
            conn = DB.getConnection()
            # カーソルを作成
            cur = conn.cursor()
            # 実行するSQL文を定義。ここでは指定されたidを持つチャンネルを検索
            sql = "SELECT channel_id, c.name as channel_name, user_id, u.name as user_name FROM channels_users AS cs INNER JOIN users AS u ON cs.user_id = u.id INNER JOIN channels AS c ON cs.channel_id = c.id WHERE cs.channel_id = %s;"
            
            # SQL文を実行。パラメータとしてuidを渡す
            cur.execute(sql, (user_id,))
            # 結果を取得
            channels = cur.fetchall()
            # 取得したチャンネル情報を返す
            return channelMembers
        except Exception as e:
            # 例外が発生した場合、エラーをコンソールに出力
            print(str(e) + 'が発生しています')
            # 例外が発生した場合はNoneを返す
            return None
        finally:
            # 最後に必ずカーソルを閉じる
            cur.close()