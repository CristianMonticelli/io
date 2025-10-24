import sqlite3
from typing import List, Tuple
import db_utils
#Connessione: crea il file 'K.db' se non esiste
conn: sqlite3.Connection = sqlite3.connect('K.db')
#Creazione Cursore
cursor: sqlite3.Cursor = conn.cursor()