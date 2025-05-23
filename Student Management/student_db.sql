CREATE DATABASE IF NOT EXISTS student_db;

USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    roll_number VARCHAR(50),
    stream VARCHAR(50),
    year VARCHAR(10),
    semester VARCHAR(10),
    password VARCHAR(100)
);
