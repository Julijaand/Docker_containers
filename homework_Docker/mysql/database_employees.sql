CREATE DATABASE IF NOT EXISTS db;
use db;

CREATE TABLE employees(
    employee_ID int not null AUTO_INCREMENT, 
    firstName varchar(50) not null,
    surName varchar(50) not null,
    contact varchar(30)
    PRIMARY KEY (employee_ID)
);
