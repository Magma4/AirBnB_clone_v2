/*File: setup_mysql_test.sql
Authors: Raymond Frimpong Amoateng - Christopher Wiafe Debrah
email(s): raymondamoateng@gmail.com - cd.jobs.w@gmail.com
          */
          
-- Script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
