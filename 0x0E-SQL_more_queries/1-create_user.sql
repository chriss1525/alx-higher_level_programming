-- create new user with privileges
-- create new user
CREATE USER user_0d_1 @localhost IDENTIFIED BY 'user_0d_1_pwd';
-- grant user all privileges
GRANT ALL PRIVILEGES ON *.* TO user_0d_1 @localhost WITH
GRANT OPTION;