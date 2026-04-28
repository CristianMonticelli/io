-- Tabella prodotti
CREATE TABLE IF NOT EXISTS prodotti (
    codice TEXT PRIMARY KEY,
    prezzo REAL,
    marca TEXT,
    modello TEXT
);

-- Inseriamo alcuni dati di esempio
INSERT OR IGNORE INTO prodotti VALUES ('A123', 299.99, 'Dell', 'XPS 13');
INSERT OR IGNORE INTO prodotti VALUES ('B456', 899.00, 'Apple', 'MacBook Air');
INSERT OR IGNORE INTO prodotti VALUES ('C789', 549.50, 'Lenovo', 'ThinkPad X1');
