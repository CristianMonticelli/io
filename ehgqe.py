import os

n = 1
while True:
    if os.path.exists(f'esercizio_{n}'):
        print(f"Il file '{n}' esiste.")
        n+=1
    else:
        print(f"Il file '{n}' non esiste.")
        break

os.mkdir(f'esercizio_{n}')

with open(f'esercizio_{n}/monticelli_0{str(n)}.py', 'w') as f:
    f.write('''import sqlite3
from typing import List, Tuple
import db_utils
#Connessione: crea il file 'K.db' se non esiste
conn: sqlite3.Connection = sqlite3.connect('K.db')
#Creazione Cursore
cursor: sqlite3.Cursor = conn.cursor()''')

with open(f'esercizio_{n}/monticelli_0{str(n)}.md', 'w') as f:
    f.write(f'''```mermaid
erDiagram


```''')
    
with open(f'esercizio_{n}/monticelli_0{str(n)}.db', 'w') as f:
    f.write(f'''
            ''')

with open(f'esercizio_{n}/monticelli_0{str(n)}.txt', 'w') as f:
    f.write(f'''
            ''')

with open(f'esercizio_{n}/monticelli_0{str(n)}.sql', 'w') as f:
    f.write(f'''
            CREATE TABLE X (
);

''')
    
# with open(f'esercizio_{n}/monticelli_0{str(n)}.md', 'w') as f:
#     f.write(f'''```mermaid
# classDiagram
#     class 
    
# ```''')
