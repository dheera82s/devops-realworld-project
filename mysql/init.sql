CREATE DATABASE IF NOT EXISTS devopsdb;

USE devopsdb;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO users (name, email)
VALUES
('Anil', 'anil@example.com'),
('DevOps User', 'devops@example.com');