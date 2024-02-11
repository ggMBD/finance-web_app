-- Create the database
CREATE DATABASE IF NOT EXISTS `finance-web_app`;

-- Create the user
CREATE USER 'finance_dev_user'@'localhost' IDENTIFIED BY 'finance_password';

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON `finance-web_app`.* TO 'finance_dev_user'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
