
-- 1. Creare le tabelle del modello ER

CREATE TABLE TIPOLOGY (
    id INT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    descrizione VARCHAR(50),
  
);

CREATE TABLE  MIELE (
    id INT PRIMARY KEY,
    denominazione VARCHAR(50),
    typology_id INT, 
    FOREIGN KEY(typology_id) REFERENCES TIPOLOGY(id)
  
);


CREATE TABLE APICOLTORE (
    id INT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
  
);


CREATE TABLE APIARI (
    code STRING PRIMARY KEY,
    numeroArnie INT,
    localita VARCHAR(50),
    comune VARCHAR(50),
    provincia VARCHAR(50),
    regione VARCHAR(50),
    apicoltore_id INT,
    FOREIGN KEY(apicoltore_id) REFERENCES APICOLTORE(id)

  
);


CREATE TABLE PRODUZIONE (
    id INT PRIMARY KEY,
    anno INT,
    quantita INT,
    miele_id INT,
    apiario_id INT,
    FOREIGN KEY(miele_id) REFERENCES MIELE(id)
    FOREIGN KEY(apiario_id) REFERENCES APIARI(code)
  
);


-- 2. Inserire dati nelle tabelle con le istruzioni di INSERT (2-3 righe per tabella)

INSERT INTO TIPOLOGY (id, Nome, descrizione)
VALUES (1, 'Acacia', 'Miele di acacia'),
       (2, 'Castagno', 'Miele di castagno'),
       (3, 'Melata', 'Miele di melata');

INSERT INTO MIELE (id, denominazione, typology_id)
VALUES (1, 'Miele di acacia', 1),
       (2, 'Miele di castagno', 2),
       (3, 'Miele di melata', 3);

INSERT INTO APICOLTORE (id, Nome)
VALUES (1, 'Mario Rossi'),
       (2, 'Luigi Bianchi'),
       (3, 'Giovanni Verdi');

INSERT INTO APIARI (code, numeroArnie, localita, comune, provincia, regione, apicoltore_id)
VALUES ('A001', 15, 'Localita1', 'Comune1', 'Provincia1', 'Lombardia', 1),
       ('A002', 8, 'Localita2', 'Comune2', 'Provincia2', 'Lombardia', 2),
       ('A003', 12, 'Localita3', 'Comune3', 'Provincia3', 'Lazio', 1);

INSERT INTO PRODUZIONE (id, anno, quantita, miele_id, apiario_id)
VALUES (1, 2023, 200, 1, 'A001'),
       (2, 2023, 150, 2, 'A002'),
       (3, 2024, 180, 3, 'A001');

-- 3. Fare le seguenti query:

-- Seleziona tutti gli apicoltori.       
SELECT *
FROM APICOLTORE

-- Seleziona l'apicoltore con id 1.
SELECT id, Nome
FROM APICOLTORE
where id = 1;

-- Seleziona tutti gli apiari nella regione 'Lombardia'.
SELECT *
FROM APIARI
where regione = 'Lombardia';

-- Seleziona codice e numero_arnie degli apiari con più di 10 arnie.
SELECT code, numeroArnie
FROM APIARI
where numeroArnie > 10;

-- Seleziona codice e località degli apiari posseduti dall'apicoltore con id = 2.
SELECT code, localita
FROM APIARI
where apicoltore_id = 2;

-- Seleziona tutti i mieli appartenenti alla tipologia con id = 3.
SELECT *
FROM MIELE
where typology_id = 3;

-- Seleziona la denominazione del miele con id = 5.
SELECT denominazione
FROM MIELE
where id = 5;

-- Seleziona tutte le produzioni dell'anno 2024.
SELECT *
FROM PRODUZIONE
where anno = 2024;

-- Seleziona tutte le produzioni dell'apiario con id = 'A001'.
SELECT *
FROM PRODUZIONE
where apiario_id = 'A001';

-- Seleziona tutte le produzioni del miele con id = 3 nell'anno 2023.
SELECT *
FROM PRODUZIONE
where miele_id  = 3 AND anno = 2023;

    