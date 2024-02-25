# Pythonのイメージを指定
FROM python:3.11.3-buster
# PYTHONDONTWRITEBYTECODEとPYTHONUNBUFFEREDはオプション
# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
# コンテナのワークディレクトリを/codeに指定
WORKDIR /code
#uWSGIの依存関係問題解決のためのインストール
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    build-essential \
    libpcre3 \
    libpcre3-dev \
    less \
    vim \
    curl \
    unzip \
    sudo
# aws cli v2 のインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install
# ローカルのrequirements.txtをコンテナの/codeフォルダ直下に置く
COPY ./requirements.txt /code/
# コンテナ内でpip install -r requirements.txtを実行
RUN pip install -U pip && \
    pip install -r requirements.txt
# ソースコードをコンテナにコピー
COPY . /code/

CMD ["uwsgi", "app.ini"]