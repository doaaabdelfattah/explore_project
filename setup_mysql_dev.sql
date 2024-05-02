-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS explore_project_db;
CREATE USER IF NOT EXISTS 'porto_dev'@'localhost' IDENTIFIED BY 'porto_dev_pwd';
GRANT ALL PRIVILEGES ON `explore_project_db`.* TO 'porto_dev'@'localhost';
FLUSH PRIVILEGES;