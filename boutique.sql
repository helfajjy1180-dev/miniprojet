CREATE DATABASE mini_projet ;

USE mini_projet;


CREATE TABLE produits (
    id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prix FLOAT NOT NULL
);

CREATE TABLE clients (
    id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);
SHOW DATABASES;

USE mini_projet;

SHOW TABLES;