-- Schema del database CRUD
-- Tabella items con tutti i campi necessari per CRUD completo

DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Dati di esempio
INSERT INTO items (name, description) VALUES ('Laptop', 'Computer portatile performante');
INSERT INTO items (name, description) VALUES ('Mouse', 'Mouse wireless ergonomico');
INSERT INTO items (name, description) VALUES ('Tastiera', 'Tastiera meccanica RGB');
INSERT INTO items (name, description) VALUES ('Monitor', 'Monitor 27 pollici 144Hz');
INSERT INTO items (name, description) VALUES ('Cuffie', 'Cuffie Bluetooth wireless');
