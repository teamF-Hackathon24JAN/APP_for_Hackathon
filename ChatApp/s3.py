import boto3, os, datetime

class awsConnect:
    def uploadImage(file, file_name, user_id):
        try:
            # AWS認証情報（環境変数から取得）
            AWS_ACCESS_KEY_ID='AKIA3FLDZEDGFNMYG6UV' 
            AWS_SECRET_ACCESS_KEY='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'

            # S3 Bucket 名
            S3_BUCKET_NAME = 'test-fteam'
            path = file_name
            # 保存するイメージファイルの拡張子を取得
            file_extension = os.path.splitext(os.path.basename(path))[1][1:]

            ContentType = None
            # 拡張子によってコンテントタイプ(mime)を変更する
            if file_extension == "jpeg" or file_extension == "jpg" or file_extension == "JPEG" or file_extension == "JPG":
                ContentType = "image/jpeg"
            else:
                if file_extension == "png" or file_extension == "PNG":
                    ContentType = "image/png"
                else:
                    if file_extension == "gif" or file_extension == "GIF":
                        ContentType = "image/gif"
                    else:
                        redirect('/setting')
            
            if ContentType is not None:
                # 現在時刻を取得
                t_delta = datetime.timedelta(hours=9)
                JST = datetime.timezone(t_delta, 'JST')
                now = datetime.datetime.now(JST)
                now = now.strftime('%Y%m%d%H%M%S')
                # S3に登録するファイル名：[user_id][yyyymmddss]
                add_file_name = str(user_id) + str(now)
                # DB格納用のオブジェクトURL https://test-fteam.s3.ap-northeast-1.amazonaws.com/icon/id8_20240301110405.jpg
                add_key = "icon/" + add_file_name + "." + str(file_extension)
                object_url = "https://test-fteam.s3.ap-northeast-1.amazonaws.com/" + add_key

                # boto3クライアントの初期化
                s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

                # S3へファイルをアップロードする
                s3.upload_fileobj(Fileobj=file, Bucket=S3_BUCKET_NAME, Key=add_key, ExtraArgs={"ContentType": ContentType, "ACL": "public-read"})

                return object_url
            
            else:
                redirect('/setting')

        except Exception as e:
            print(str(e) + 'が発生しています')

        finally:
            pass
