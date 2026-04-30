
from flask import Flask, request, Response, render_template, g
from xml.sax.saxutils import escape
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
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


def get_prodotto_by_codice(codice):
    db = get_db()
    prodotto = db.execute(
        'SELECT * FROM prodotti WHERE codice = ?', (codice,)
    ).fetchone()
    return prodotto

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
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
    return render_template('index.html')

@app.route('/prodotto', methods=['GET'])
def get_prodotto():
    # Leggiamo e normalizziamo il parametro dalla URL
    codice = request.args.get('codice', '')
    codice = codice.strip().upper()

    # Validazione con regex (UNA LETTERA + 3 CIFRE)
    pattern = re.compile(r'^[A-Z]\d{3}$')
    if not pattern.match(codice):
        # Restituiamo XML coerente per gli errori
        xml = f"<response ok=\"false\"><errore>{escape('Codice non valido. Formato atteso: A123')}</errore></response>"
        return Response(xml, status=400, mimetype='application/xml')

    # Interroghiamo il database tramite helper
    prodotto = get_prodotto_by_codice(codice)
    
    # Se non trovato
    if prodotto is None:
        xml = f"<response ok=\"false\"><errore>{escape('Prodotto non trovato')}</errore></response>"
        return Response(xml, status=404, mimetype='application/xml')
    
    # Ritorniamo i dati in XML
    xml = (
        '<response ok="true">'
        f'<codice>{escape(str(prodotto["codice"]))}</codice>'
        f'<prezzo>{escape(str(prodotto["prezzo"]))}</prezzo>'
        f'<marca>{escape(str(prodotto["marca"]))}</marca>'
        f'<modello>{escape(str(prodotto["modello"]))}</modello>'
        '</response>'
    )
    return Response(xml, mimetype='application/xml')

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
