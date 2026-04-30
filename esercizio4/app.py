"""
ESERCIZIO 4: Ricerca Prodotti con Flask
=========================================

OBIETTIVO:
- Creare un'applicazione Flask che gestisce una ricerca di prodotti
- L'utente inserisce un codice prodotto
- La pagina comunica con il server via AJAX (senza ricaricare la pagina)
- Il server restituisce i dati in JSON
- La pagina visualizza il risultato dinamicamente

FLUSSO:
1. L'utente digita un codice (es. A123)
2. JavaScript valida il codice
3. AJAX invia una richiesta GET a /prodotto
4. Flask interroga il database
5. Flask restituisce JSON con i dati
6. JavaScript visualizza il risultato senza ricaricare
"""

from flask import Flask, request, jsonify, render_template, g
import sqlite3
import re
import os
from random import randint
app = Flask(__name__)
DATABASE = 'prodotti.db'

# ============================================================================
# PARTE 1: GESTIONE DEL DATABASE
# ============================================================================

def get_db():
    """
    Funzione che ritorna la connessione al database.
    
    Usiamo g (global context di Flask) per tenere la connessione per 
    tutta la durata della richiesta HTTP, poi la chiudiamo automaticamente.
    
    row_factory = sqlite3.Row trasforma i risultati in oggetti
    che possiamo accedere come dizionari: row['colonna']
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


def get_prodotto_by_codice(codice):
    """Cerca un prodotto per codice nel database.

    Restituisce la riga (sqlite3.Row) se trovata, altrimenti None.
    """
    db = get_db()
    prodotto = db.execute(
        'SELECT * FROM prodotti WHERE codice = ?', (codice,)
    ).fetchone()
    return prodotto

@app.teardown_appcontext
def close_connection(exception):
    """
    Questa funzione viene chiamata automaticamente alla fine di ogni richiesta.
    Chiude la connessione al database.
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """
    Funzione che inizializza il database.
    - Se non esiste, lo crea
    - Se esiste già, aggiunge solo i dati nuovi (INSERT OR IGNORE)
    """
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())
        db.commit()
        print("Database inizializzato!")

# ============================================================================
# PARTE 2: ROUTE FLASK
# ============================================================================

@app.route('/')
def index():
    """
    ROUTE HOME: Quando l'utente accede a http://localhost:5000/
    Ritorniamo la pagina HTML principale
    """
    return render_template('index.html')

@app.route('/prodotto', methods=['GET'])
def get_prodotto():
    """
    ROUTE API: Quando riceve una richiesta GET da JavaScript
    
    PARAMETRI: codice (dalla query string: ?codice=A123)
    
    VALIDAZIONE: 
    - Il codice deve essere nel formato: 1 LETTERA + 3 NUMERI (es: A123, B456)
    - Usiamo una REGEX per validare: ^[A-Za-z]\d{3}$
      * ^ = inizio stringa
      * [A-Za-z] = una lettera maiuscola o minuscola
      * \d{3} = esattamente 3 cifre
      * $ = fine stringa
    
    RISPOSTA:
    - Se il formato è sbagliato: errore 400 (Bad Request)
    - Se il prodotto non esiste: errore 404 (Not Found)
    - Se tutto ok: JSON con prezzo, marca, modello
    """
    # Leggiamo e normalizziamo il parametro dalla URL
    codice = request.args.get('codice', '')
    codice = codice.strip().upper()

    # Validazione con regex (UNA LETTERA + 3 CIFRE)
    pattern = re.compile(r'^[A-Z]\d{3}$')
    if not pattern.match(codice):
        # Restituiamo sempre JSON coerente per gli errori
        return jsonify({'ok': False, 'errore': 'Codice non valido. Formato atteso: A123'}), 400

    # Interroghiamo il database tramite helper
    prodotto = get_prodotto_by_codice(codice)
    
    # Se non trovato
    if prodotto is None:
        return jsonify({'ok': False, 'errore': 'Prodotto non trovato'}), 404
    
    # Ritorniamo i dati in JSON
    return jsonify({
        'ok': True,
        'prezzo': prodotto['prezzo'],
        'marca': prodotto['marca'],
        'modello': prodotto['modello']
    })

# ============================================================================
# PARTE 3: AVVIO APPLICAZIONE
# ============================================================================

if __name__ == '__main__':
    # Se il database non esiste, lo creiamo
    if not os.path.exists(DATABASE):
        print("Creo il database...")
        init_db()
    else:
        print("Database già presente")
    
    # Avviamo il server Flask
    # debug=True significa che ricarica automaticamente quando cambiamo il codice
    porta = randint(5000, 5999)  # Scegliamo una porta casuale tra 5000 e 5999
    print(f"Server avviato su http://localhost:{porta}/")
    app.run(debug=True, port=porta)
