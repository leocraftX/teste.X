CREATE DATABASE sistema_login;
USE sistema_login;
CREATE table usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100)NOT NULL,
    senha VARCHAR(100) NOT NULL
);
INSERT INTO usuarios(nome,email, senha)values('agatha','agatha@flamma','123456');

SELECT * FROM usuarios;