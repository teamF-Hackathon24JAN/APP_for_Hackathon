
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
    description varchar(255),
    owner_id integer REFERENCES users(id)
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
);

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


INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(1, '1', 'いち', 'one@gmail.com', '1234', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', '1残業上等');
INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(2, '2', 'にー', 'two@gmail.com', '1234', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', '2残業上等');
INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(3, '3', 'さん', 'three@gmail.com', '1234', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', '3残業上等');
INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(4, '4', 'よん', 'four@gmail.com', '1234', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', '4残業上等');
INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(5, '5', 'ごー', 'five@gmail.com', '1234', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', '5残業上等');
INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(6, '6', 'ろく', 'six@gmail.com', '1234', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', '6残業上等');
INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(7, 'd9f77623-4b63-48f0-bfd9-37e3a55bc8de', 'asdf', 'asdf@gmail.com', 'f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', 'ひとこと が とうろく されていません');
INSERT INTO users(id, session_id, name, email, password, picture, one_phrase) VALUES(8, '845f952b-56ee-4664-8456-893728e08fe8', 'nao', 'naoentry@gmail.com', 'f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b', 'https://test-fteam.s3.ap-northeast-1.amazonaws.com/default_icon.JPG', 'ひとこと が とうろく されていません');

INSERT INTO channels(id, name, description, owner_id) VALUES(1, 'テスト', 'テストさんの孤独な部屋です', 8);

INSERT INTO channels_users(id, user_id, channel_id) VALUES(1, 1, 1);
INSERT INTO channels_users(id, user_id, channel_id) VALUES(2, 2, 1);
INSERT INTO channels_users(id, user_id, channel_id) VALUES(3, 3, 1);
INSERT INTO channels_users(id, user_id, channel_id) VALUES(4, 4, 1);
INSERT INTO channels_users(id, user_id, channel_id) VALUES(5, 5, 1);
INSERT INTO channels_users(id, user_id, channel_id) VALUES(6, 6, 1);
INSERT INTO channels_users(id, user_id, channel_id) VALUES(7, 8, 1);

INSERT INTO friends(id, user_id, friend_id) VALUES(1, 8, 1);
INSERT INTO friends(id, user_id, friend_id) VALUES(2, 8, 2);
INSERT INTO friends(id, user_id, friend_id) VALUES(3, 8, 3);
INSERT INTO friends(id, user_id, friend_id) VALUES(4, 8, 4);
INSERT INTO friends(id, user_id, friend_id) VALUES(5, 8, 5);
INSERT INTO friends(id, user_id, friend_id) VALUES(6, 8, 6);
INSERT INTO friends(id, user_id, friend_id) VALUES(7, 8, 7);

INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '誰かかまってください、、')