-- script that creates the MySQL server user

CREATE USER IF NOT EXISTS user_0d_1@localhostIDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
ON *.*
TO user_0d_1@localhost;
FLUSH PRIVILEGES;
