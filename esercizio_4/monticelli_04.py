import sqlite3

# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('scuola.db')
# 3. Creazione Cursore
cursor = conn.cursor()

try:
    # Eseguo DDL per creare la tabella se non esiste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studenti (
            Matricola INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Cognome TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Esami (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Matricola INT,
            Corso TEXT NOT NULL,
            Voto INTEGER,
            FOREIGN KEY (Matricola) REFERENCES Studente(Matricola)
        )
    """)


    
    cursor.executemany(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        [(101, 'Mario', 'Rossi'),
        (102, 'Lucia', 'Bianchi'),]
    )
    
    cursor.executemany(
        "INSERT INTO Esami (Id, Matricola, Corso, Voto) VALUES (?, ?, ?)",
        [(101,"Matematica",28),
        (101,"Informatica",30),
        (101,"Fisica",27),
        (102,"Matematica",30),
        (102,"Informatica",26),
        (102,"Fisica",29),]
        
    )
    

    # 5. Conferma delle modifiche
    conn.commit()

    # Eseguo una SELECT
    cursor.execute("SELECT Nome, Cognome FROM Studenti WHERE Matricola = ?", (101,))
    studente = cursor.fetchone() # I risultati sono tuple
    if studente:
        print(f"Studente trovato (SQLite): {studente} {studente}")

finally:
    # 6. Chiusura Connessione
    conn.close()