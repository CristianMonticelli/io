import os
import sqlite3
from flask import Flask, g

def get_db():
    """Ritorna la connessione al database"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('app.db')
        db.row_factory = sqlite3.Row
    return db

def init_app(app):
    """Inizializza l'app Flask"""
    # Chiudi il DB alla fine della request
    app.teardown_appcontext(close_db)
    
    # Inizializza il DB
    with app.app_context():
        init_db()

def close_db(exception):
    """Chiude il database"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Crea le tabelle dal file schema.sql"""
    db = get_db()
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql')) as f:
        db.executescript(f.read())
    db.commit()

def create_app():
    """Factory per creare l'app Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    
    init_app(app)
    
    from app import main
    app.register_blueprint(main.bp)
    
    return app
