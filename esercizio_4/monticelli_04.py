import sqlite3

# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('esercizio_4/scuola.db')
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
        "INSERT OR IGNORE INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        [(101, 'Mario', 'Rossi'),
        (102, 'Lucia', 'Bianchi'),]
    )
    
    cursor.executemany(
        "INSERT OR IGNORE INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)",
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
    #1. Elenco di tutti gli studenti (Matricola, Nome, Cognome).
    cursor.execute("""
        SELECT *
        FROM Studenti
    """)
    studenti = cursor.fetchall()
    print("\nElenco di tutti gli studenti (Matricola, Nome, Cognome):")
    for studente in studenti:
        print(studente)
    
    # 2. Elenco dei corsi e voti sostenuti da uno studente specifico
    # (usa la matricola 101 come esempio).
    cursor.execute("""
        SELECT Matricola, Corso, Voto
        FROM Esami
        WHERE Matricola = 101
    """)
    studenti = cursor.fetchall()
    print("\nElenco dei corsi e voti sostenuti da uno studente specifico (usa la matricola 101 come esempio):")
    for studente in studenti:
        print(studente)
        
    # 3. Numero di esami sostenuti per ciascuno studente (GROUP BY Matricola).
    cursor.execute("""
        SELECT S.Nome, S.Cognome, Count(*)
        FROM Studenti AS S
        JOIN Esami AS E ON S.Matricola = E.Matricola
        GROUP BY E.Matricola
    """)
    studenti = cursor.fetchall()
    print("\nNumero di esami sostenuti per ciascuno studente (GROUP BY Matricola):")
    for studente in studenti:
        print(studente)

finally:
    # 6. Chiusura Connessione
    conn.close()