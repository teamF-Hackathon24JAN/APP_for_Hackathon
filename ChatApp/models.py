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
#    def getChannelByName(channel_name):
#        try:
#            conn = DB.getConnection()
#            cur = conn.cursor()
#            sql = "SELECT * FROM channels WHERE name=%s;"
#            cur.execute(sql, (channel_name))
#            channel = cur.fetchone()
#            return channel
#        except Exception as e:
#            print(e + 'が発生しています')
#            return None
#        finally:
#            cur.close()

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
            sql = "SELECT f.id, friend_id, u.name AS friend_name, u.one_phrase AS friend_one_phrase, u.picture AS friend_picture FROM friends AS f INNER JOIN users AS u ON f.friend_id = u.id WHERE user_id = %s;"
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

# フレンド一覧機能、自分のuser_idに紐付けされているfriend_idを一覧で引き出す
    def getFriendIdAll(user_id):
    # tryブロックを使用して、データーベースへの接続と操作を試みる
        try:
            # データベース接続を取得
            conn = DB.getConnection()
            # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
            cur = conn.cursor()
            # SQL文を定義
            sql = "SELECT friend_id FROM friends WHERE user_id = %s;"
            # executeメソッドを使用してSQL文を実行
            cur.execute(sql, (user_id))
            # fetchallメソッドを使用してクエリ結果の全ての行を取得
            friend_ids = cur.fetchall()
            # 取得した情報を返す
            return friend_ids
        except Exception as e:
            # エラーが発生した場合、エラーメッセージを出力
            print(str(e) + 'が発生しています')
            # エラーが発生した場合はNoneを返す
            return None
        finally:
            # finallyブロックは、tryブロックの実行が成功したか、エラーが発生したかに関わらず実行
            # カーソルオブジェクトを閉じる
            cur.close()

# パスワード変更機能
    def updateUserPicuture(picture, user_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET picture = %s WHERE id = %s;"
            cur.execute(sql, (picture, user_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# 名前変更機能
    def updateUserName(name, user_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET name = %s WHERE id = %s;"
            cur.execute(sql, (name, user_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# ひとこと変更機能
    def updateOnePhrase(one_phrase, user_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET one_phrase = %s WHERE id = %s;"
            cur.execute(sql, (one_phrase, user_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# メールアドレス変更機能
    def updateUserEmail(email, user_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET email = %s WHERE id = %s;"
            cur.execute(sql, (email, user_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# パスワード変更機能
    def updateUserPassword(password, user_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET password = %s WHERE id = %s;"
            cur.execute(sql, (password, user_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# 定型文新規作成用
    def createFixedPhrase(user_id, phrase):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO fixed_phrases (user_id, phrase) VALUES (%s, %s);"
            cur.execute(sql, (user_id, phrase))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

#定型文の削除
    def deleteFixedPhrase(phrase_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM fixed_phrases WHERE id=%s;"
            cur.execute(sql, (phrase_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
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
            sql = "SELECT id, user_id, phrase FROM fixed_phrases WHERE user_id = %s;"
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

# チャンネル作成機能
    def createChannel(channel_name, description, owner_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (name, description, owner_id) VALUES (%s, %s, %s);"
            cur.execute(sql, (channel_name, description, owner_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# 作成したチャンネルのidを取得
    def getCreatedChannelId(channel_name, owner_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name = %s AND owner_id = %s;"
            cur.execute(sql, (channel_name, owner_id))
            channel = cur.fetchone()
            channel_id = channel["id"]
            return channel_id
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# チャンネルのidからチャンネル情報を取得
    def getChannelById(channel_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id = %s;"
            cur.execute(sql, (channel_id))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# チャンネル情報の編集機能
    def updateChannel(channel_name, channel_description, channel_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels SET name = %s, description = %s WHERE id = %s;"
            cur.execute(sql, (channel_name, channel_description, channel_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# 作成したチャンネルに自分を追加
    def insertMe(user_id, channel_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels_users (user_id, channel_id) VALUES (%s, %s);"
            cur.execute(sql, (user_id, channel_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

# 自分が参加しているチャンネルを取得
    def getJoinedChannelById(user_id):
        try:
            # データベースへの接続を確立
            conn = DB.getConnection()
            # カーソルを作成
            cur = conn.cursor()
            # 実行するSQL文を定義。ここでは指定されたidを持つチャンネルを検索
            sql = "SELECT user_id, u.name AS user_name, channel_id, c.name AS channel_name, c.description FROM channels_users AS cs INNER JOIN users AS u ON cs.user_id = u.id INNER JOIN channels AS c ON cs.channel_id = c.id WHERE cs.user_id = %s;"
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
            sql = "SELECT cs.id, user_id as member_id, u.name as member_name, u.picture AS member_picture, u.one_phrase AS member_one_phrase FROM channels_users AS cs INNER JOIN users AS u ON cs.user_id = u.id INNER JOIN channels AS c ON cs.channel_id = c.id WHERE cs.channel_id = %s;"
            
            # SQL文を実行。パラメータとしてuidを渡す
            cur.execute(sql, (channel_id))
            # 結果を取得
            members = cur.fetchall()
            # 取得したチャンネル情報を返す
            return members
        except Exception as e:
            # 例外が発生した場合、エラーをコンソールに出力
            print(str(e) + 'が発生しています')
            # 例外が発生した場合はNoneを返す
            return None
        finally:
            # 最後に必ずカーソルを閉じる
            cur.close()

# フレンド追加機能、検索したユーザーのIDを格納
    def addChannelMenber(member_id, channel_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels_users (user_id, channel_id) VALUES (%s, %s);"
            cur.execute(sql, (channel_id, friend_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()

    def createMessage(user_id, channel_id, message):
    # tryブロックを使用して、データベースへの接続と操作を試みる
        try:
            # データベース接続を取得
            conn = DB.getConnection()
            # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
            cur = conn.cursor()
            # SQL文を定義
            sql = "INSERT INTO messages (user_id, channel_id, message) VALUES(%s, %s, %s);"
            # executeメソッドを使用してSQL文を実行。プレースホルダーにはuid, cid, messageの値を渡す
            cur.execute(sql, (user_id, channel_id, message))
            conn.commit()
        except Exception as e:
            # エラーが発生した場合、エラーメッセージを出力
            print(str(e) + 'が発生しています')
            # エラーが発生した場合は、Noneを返す

        finally:
            # finallyブロックは、tryブロックの実行が成功したか、エラーが発生したかに関わらず実行
            # カーソルオブジェクトを閉じる
            cur.close()

    def getMessageAll(channel_id):
        # tryブロックを使用して、データーベースへの接続と操作を試みる
        try:
            # データベース接続を取得
            conn = DB.getConnection()
            # カーソルオブジェクトを作成。これを使用してSQLクエリを実行
            cur = conn.cursor()
            # SQL文を定義。このSQL文では、指定されたcidに対するメッセージとそれに関連するユーザー情報を取得
            sql = "SELECT m.id, user_id, u.name as user_name, message, created_at FROM messages AS m INNER JOIN users AS u ON m.user_id = u.id WHERE channel_id = %s;"
            # executeメソッドを使用してSQL文を実行
            # cidの値をSQLクエリのパラメータとして渡す
            cur.execute(sql, (channel_id))
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