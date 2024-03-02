
DROP DATABASE gutara_chat;
DROP USER 'admin';

CREATE USER 'admin' IDENTIFIED BY 'fteam';
CREATE DATABASE gutara_chat;
USE gutara_chat
GRANT ALL PRIVILEGES ON gutara_chat.* TO 'admin';

CREATE TABLE users (
    id serial PRIMARY KEY,
    session_id varchar(255) UNIQUE NOT NULL,
    name varchar(255) NOT NULL,
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
