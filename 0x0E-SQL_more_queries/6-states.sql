-- create usa states database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa -- create states table
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY DEFAULT 0 UNIQUE,
    VARCHAR(256) NOT NULL
)