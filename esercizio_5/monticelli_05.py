import sqlite3
from typing import List, Tuple
import db_utils
#Connessione: crea il file 'libreria.db' se non esiste
conn: sqlite3.Connection = sqlite3.connect('libreria.db')
#Creazione Cursore
cursor: sqlite3.Cursor = conn.cursor()

def create_tables():
    #try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AUTORI (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cognome TEXT NOT NULL
)""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LIBRI (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            titolo TEXT NOT NULL,
            autore_id INTEGER,
            anno INTEGER,
            genere TEXT,
            FOREIGN KEY (autore_id)  REFERENCES AUTORI(id)
)""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PRESTITI (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            libro_id INTEGER,
            utente  TEXT NOT NULL,
            data_prestito TEXT,
            data_restituzione TEXT,
            FOREIGN KEY (libro_id)  REFERENCES LIBRI(id)
)""")

Autori: List[Tuple[int, str, str]] =  [(1,'Mario','Rossi'),
        ( 2,'Lucia', 'Bianchi'),
        ( 3,'Alessandro','Verdi')]

Libri: List[Tuple[int, str, int, int, str]] = [( 1,  'Il mistero del castello', 1,2020, 'Giallo'),
        ( 2,  'Viaggio nel tempo', 1,2018, 'Fantascienza'),
        ( 3,  'La cucina italiana', 2,2019, 'Cucina'),
        ( 4,  'Storia antica', 3,2021, 'Storia'),
        ( 5,  'Romanzo moderno', 3,2022, 'Narrativa'),
        ( 6,  'Il ritorno del castello', 1,2023, 'Giallo'),]

Prestiti: List[Tuple[int,int, str, str, str]] = [(1,1,'Mario Rossi','2023-01-01','2023-01-15'),
         (2,2,'Lucia Bianchi','2023-02-01','NULL'),
         (3,3,'Alessandro Verdi','2023-03-01','2023-03-10'),
         (4,4,'Mario Rossi','2023-04-01','NULL'),]

def insert_data(Autori, Libri, Prestiti):
    cursor.executemany(
        "INSERT OR IGNORE INTO AUTORI (ID, nome,cognome) VALUES (?, ?, ?)",
        Autori
    )
    
    cursor.executemany(
        "INSERT OR IGNORE INTO LIBRI (ID, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
        Libri
    )
    cursor.executemany(
        "INSERT OR IGNORE INTO PRESTITI (ID, libro_id, utente,data_prestito, data_restituzione) VALUES (?, ?, ?, ?, ?)",
        Prestiti
    )

def query_libri_per_autore(autore_id: int):
    cursor.execute("""
        SELECT L.titolo, A.nome, A.cognome
        FROM LIBRI AS L
        JOIN AUTORI AS A
        ON L.autore_id = A.ID
        WHERE A.ID = ?

    """,(autore_id,))
    show_fetched_data(cursor.fetchall())
    
def query_prestiti_per_utente(utente: str):
    cursor.execute("""
        SELECT P.utente ,L.titolo, P.data_prestito, P.data_restituzione
        FROM PRESTITI AS P
        JOIN LIBRI AS L
        ON P.libro_id = L.ID
        WHERE P.utente = ?
""",(utente,))
    
    db_utils.show_fetched_data(cursor.fetchall())
        
def query_libri_per_genere():
    cursor.execute("""
        SELECT L.genere, count(?) AS NUMERO_LIBRI
        FROM LIBRI AS L
        GROUP BY L.genere
""",('Giallo',))
    
    db_utils.show_fetched_data(cursor.fetchall())

def query_autori_con_piu_libri():
    cursor.execute("""
        SELECT A.nome, A.cognome, count(L.autore_id) AS NUMERO_LIBRI
        FROM AUTORI AS A
        JOIN LIBRI AS L
        ON A.ID = L.autore_id
        GROUP BY A.ID
        ORDER BY NUMERO_LIBRI DESC
""")
    db_utils.show_fetched_data(cursor.fetchall())

def query_prestiti_non_restituiti():
    cursor.execute("""
        SELECT P.utente ,L.titolo, P.data_prestito
        FROM PRESTITI AS P
        JOIN LIBRI AS L
        ON P.libro_id = L.ID
        WHERE P.data_restituzione = 'NULL'
""")
    
    db_utils.show_fetched_data(cursor.fetchall())

try:
    # Inizializzazione del database
    create_tables()
    insert_data(Autori, Libri, Prestiti)
    
    # Conferma delle modifiche
    conn.commit()
    print("Restituisce tutti i libri di un autore specifico (usa JOIN).")
    query_libri_per_autore(1)
    print("Restituisce i prestiti di un utente (usa JOIN).")
    query_prestiti_per_utente('Mario Rossi')
    print("Restituisce il numero di libri per genere (usa GROUP BY). Assicurati di avere almeno un genere con due libri")
    query_libri_per_genere()
    print("Restituisce gli autori ordinati per numero di libri (usa JOIN, GROUP BY, ORDER BY).")
    query_autori_con_piu_libri()
    print(" Restituisce i prestiti non ancora restituiti (data_restituzione IS NULL).")
    query_prestiti_non_restituiti()

finally:
    # Chiusura Connessione
    conn.close()

    