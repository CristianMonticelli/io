CREATE TABLE Typology (
    id INT PRIMARY KEY,
    typology_name VARCHAR(50) NOT NULL,
    typology_description VARCHAR(300),
);

CREATE TABLE Honey (
    id INT PRIMARY KEY,
    denomination VARCHAR(50) NOT NULL,
    typology_id INT,
    FOREIGN KEY (typology_id) REFERENCES Typology(id)
);

CREATE TABLE Beekeeper (
    id INT PRIMARY KEY,
    beekeeper_name VARCHAR(50) NOT NULL,
);

CREATE TABLE Apiary (
    code INT PRIMARY KEY,
    num_hives INT NOT NULL,
    locality VARCHAR(300) NOT NULL,
    comune VARCHAR(300) NOT NULL,
    province VARCHAR(300) NOT NULL,
    region VARCHAR(300) NOT NULL,
    beekeeper_id INT,
    FOREIGN KEY (beekeeper_id) REFERENCES Beekeeper(id)
);

CREATE TABLE Production (
    id INT PRIMARY KEY,
    year INT,
    quantity FLOAT,
    apiary_code INT,
    honey_id INT,
    FOREIGN KEY (apiary_code) REFERENCES Apiary(code),
    FOREIGN KEY (honey_id) REFERENCES Honey(id)
);

-- Typology
INSERT INTO Typology (id, typology_name, typology_description) VALUES
(1, 'Monofloral', 'Miele prodotto prevalentemente da un unico fiore'),
(2, 'Polyfloral', 'Miele di millefiori, raccolto da più specie floreali'),
(3, 'Honeydew', 'Miele prodotto a partire dal melato (secrezioni di insetti)');

-- Beekeeper
INSERT INTO Beekeeper (id, beekeeper_name) VALUES
(1, 'Marco Rossi'),
(2, 'Lucia Bianchi'),
(3, 'Alessandro Verdi');

-- Honey
INSERT INTO Honey (id, denomination, typology_id) VALUES
(1, 'Acacia', 1),
(2, 'Castagno', 1),
(3, 'Millefiori', 2),
(4, 'Eucalipto', 2),
(5, 'Melata di Bosco', 3);

-- Apiary
INSERT INTO Apiary (code, num_hives, locality, comune, province, region, beekeeper_id) VALUES
(100, 12, 'Fattoria Le Rose', 'San Pietro', 'Pisa', 'Toscana', 1),
(101, 8, 'Colle Verde', 'Montevarchi', 'Arezzo', 'Toscana', 2),
(102, 20, 'Bosco Alto', 'Vercelli', 'Vercelli', 'Piemonte', 3),
(103, 5, 'Terrazza Sud', 'Verona', 'Verona', 'Veneto', 1);

-- Production
INSERT INTO Production (id, year, quantity, apiary_code, honey_id) VALUES
(1, 2022, 120.5, 100, 1),
(2, 2022, 95.2, 101, 3),
(3, 2023, 210.0, 102, 5),
(4, 2023, 34.7, 103, 2),
(5, 2024, 150.0, 100, 3),
(6, 2024, 78.3, 101, 4);

-- Seleziona la quantità totale prodotta per anno.
SELECT year, SUM(quantity) AS tot_prodotta
FROM Production AS P
GROUP BY year;

-- Seleziona la produzione media per apiario.
SELECT apiary_code, AVG(quantity) AS production_media
FROM Production AS P
GROUP BY apiary_code;

-- Seleziona il numero di produzioni e la produzione totale per miele.
SELECT H.denomination, COUNT(P.honey_id) AS numero_produzioni, SUM(P.quantity) AS produzione_totale
FROM Production AS P
JOIN Honey AS H
ON P.honey_id = H.id
GROUP BY H.denomination;

-- Seleziona la produzione totale per miele nell'anno 2024.
SELECT year,SUM(quantity)
FROM Production
where year = 2024

-- Seleziona il valore massimo e minimo di produzione per anno.
SELECT year,MAX(quantity),MIN(quantity)
FROM Production
GROUP BY year;

-- Seleziona gli apiari la cui produzione totale supera 200. X
-- Seleziona la produzione totale per tipologia di miele (typology_id).
SELECT T.typology_name,SUM(P.quantity)
FROM Production AS P
JOIN Honey AS H
ON P.honey_id = H.ID
JOIN Typology AS T
ON H.typology_id = T.ID
GROUP BY T.ID;

-- Seleziona il numero di mieli per ciascuna tipologia.
SELECT typology_id, SUM(typology_id)
FROM Honey
GROUP BY typology_id

-- Seleziona la produzione totale per apicoltore (beekeeper_id).
SELECT B.beekeeper_name,SUM(P.quantity)
FROM Production AS P
JOIN Apiary AS A
ON P.apiary_code = A.code
JOIN Beekeeper AS B
ON A.beekeeper_id = B.id
GROUP BY B.id;
-- Seleziona la produzione media per arnia (produzione totale divisa per num_hives) per apiario.
SELECT A.code, AVG(P.quantity) AS media_arnia
FROM Production AS P
JOIN Apiary AS A
ON P.apiary_code = A.code
GROUP BY A.code

-- Seleziona per ogni anno il conteggio delle produzioni con quantità maggiore di 100.
SELECT year, COUNT(quantity)
FROM Production
WHERE quantity>100
GROUP BY year

-- Seleziona per ogni miele e anno la somma delle quantità.
SELECT H.denomination, P.year, SUM(quantity)
FROM Production AS P
JOIN Honey AS H
ON P.honey_id = H.id
GROUP BY P.year, P.honey_id

