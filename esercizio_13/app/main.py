from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.repositories import canale_repo

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # 1. Prendiamo i canali veri dal database
    channels_py: list[dict] = canale_repo.get_canale()
    
    # 2. Passiamo la variabile 'canali' al template
    return render_template('index.html', channels_html=channels_py)
pass


@bp.route('/create', methods=('GET', 'POST'))
def create():
    # Protezione: Se non sei loggato, vai al login
  

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Il titolo è obbligatorio.'

        if error is not None:
            flash(error)
        else:
            # Creiamo il post usando l'ID dell'utente loggato (g.user['id'])
            post_repository.create_post(title, body, g.user['id'])
            return redirect(url_for('main.index'))

    return render_template('blog/create.html')

@bp.route('/channel_detail/<int:id>')
def channel_detail(id):
    # 1. Recupera il post dal DB
    channel = canale_repo.get_canale_id(id)

    # 2. Se non esiste -> Errore 404 Not Found
    if channel is None:
        abort(404, f"Il post id {id} non esiste.")
    return render_template('channel_detail.html', channel=channel)
