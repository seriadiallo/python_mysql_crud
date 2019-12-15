-- creation de la table clients dans la base de donnees
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    prenom VARCHAR(30) NOT NULL,
    age INT
) 
ENGINE=INNODB;
--  ajout d'un enregistrement
INSERT INTO clients (nom, prenom, age) VALUES ('Barry', 'Aliou', 20);