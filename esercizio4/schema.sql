DROP TABLE IF EXISTS prodotti;

-- Tabella prodotti
CREATE TABLE prodotti (
    codice TEXT PRIMARY KEY,
    prezzo REAL,
    marca TEXT,
    modello TEXT
);

-- Inseriamo alcuni dati di esempio
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('A123', 299.99, 'Dell', 'XPS 13');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('B456', 899.00, 'Apple', 'MacBook Air');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('C789', 549.50, 'Lenovo', 'ThinkPad X1');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('D111', 399.00, 'HP', 'Pavilion 14');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('E222', 1299.00, 'Asus', 'ZenBook 14');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('F333', 749.99, 'Acer', 'Swift 3');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('G444', 199.50, 'Microsoft', 'Surface Go');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('H555', 2199.00, 'Apple', 'MacBook Pro');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('I666', 159.99, 'Samsung', 'Galaxy Book');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('J777', 89.90, 'Chromebook', 'Lenovo Chromebook 3');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('K888', 499.00, 'LG', 'Gram 14');
INSERT INTO prodotti (codice,prezzo,marca,modello) VALUES ('L999', 349.00, 'Razer', 'Blade Stealth');
