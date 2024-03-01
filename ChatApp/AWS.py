from flask import Flask, request
import boto3
import os

class awsConnect:
    def uplode_image(file, file_name)
        try:
            # AWS認証情報（環境変数から取得）
            AWS_ACCESS_KEY_ID = "AKIA3FLDZEDGPNYWOT52"
            AWS_SECRET_ACCESS_KEY = "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"

            # S3 Bucket 名
            S3_BUCKET_NAME = 'test-fteam'

             # boto3クライアントの初期化
            s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            # S3にファイルをアップロード
            s3.upload_fileobj(file, S3_BUCKET_NAME, file_name)
            except Exception as e:
                print(str(e) + 'が発生しています')
            finally:


https://test-fteam.s3.ap-northeast-1.amazonaws.com/icon/id8_20240301110405.jpg

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # ファイルがリクエストに含まれているか確認
    if 'image' not in request.files:
        return "ファイルがリクエストに含まれていません", 400
    
    # ファイルオブジェクトを取得
    file = request.files['image']
    
    # ファイル名を取得
    file_name = file.filename
    
    # boto3クライアントの初期化
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    
    # S3にファイルをアップロード
    try:
        s3.upload_fileobj(file, S3_BUCKET_NAME, file_name)
    except Exception as e:
        return str(e), 500
    
    return "アップロード成功", 200

if __name__ == '__main__':
    app.run(debug=True)