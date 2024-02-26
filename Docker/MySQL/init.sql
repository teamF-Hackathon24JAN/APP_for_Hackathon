
DROP DATABASE gutara_chat;
DROP USER 'admin';

CREATE USER 'admin' IDENTIFIED BY 'fteam';
CREATE DATABASE gutara_chat;
USE gutara_chat
GRANT ALL PRIVILEGES ON gutara_chat.* TO 'admin';

CREATE TABLE users (
    id serial PRIMARY KEY,
    session_id varchar(255) UNIQUE NOT NULL,
    name varchar(255) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    picture varchar(255),
    birthday datetime,
    one_phrase varchar(255)
);

CREATE TABLE channels (
    id serial PRIMARY KEY,
    name varchar(255) UNIQUE NOT NULL,
    description varchar(255)
);

CREATE TABLE channels_users (
    id serial PRIMARY KEY,
    user_id integer REFERENCES users(id),
    channel_id integer REFERENCES channels(id)
);

CREATE TABLE friends(
    id serial PRIMARY KEY,
    user_id integer REFERENCES users(id),
    friend_id integer REFERENCES users(id)
)

CREATE TABLE fixed_phrases (
    id serial PRIMARY KEY,
    user_id integer REFERENCES users(id),
    phrase varchar(255) NOT NULL
);

CREATE TABLE messages (
    id serial PRIMARY KEY,
    user_id integer REFERENCES users(id),
    channel_id integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at timestamp not null default current_timestamp
);

INSERT INTO users(id,session_id, name, email, password,picture,one_phrase)VALUES(1,'970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578',hoge.com,'残業上等');
INSERT INTO channels(id, name, description)VALUES(1,'ぼっち部屋' ,'テストさんの孤独な部屋です');
INSERT INTO messages(id, user_id, channel_id, message)VALUES(1, 1, '1', '誰かかまってください、、')
