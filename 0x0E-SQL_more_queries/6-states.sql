-- create usa states database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create states table
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);