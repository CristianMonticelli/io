from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.repositories import canale_repo

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    channels_py: list[dict] = canale_repo.get_canale()
    categoria_py: list[dict] = canale_repo.get_categoria()
    
    return render_template('index.html', channels_html=channels_py, categoria_html=categoria_py)




@bp.route('/channel_detail/<int:id>')
def channel_detail(id):
    channel_detail = canale_repo.get_canale_id(id)
    video = canale_repo.get_video_id(id)
    categoria_py: list[dict] = canale_repo.get_categoria()

    return render_template('channel_detail.html', channel=channel_detail, videos=video, categoria_html=categoria_py)

@bp.route("/url_crea", methods=("GET", "POST"))
def create_channel():
    if request.method == "POST":
        nome = request.form["nome"]
        numero_iscritti = request.form.get("numero_iscritti", 0, type=int)
        categoria = request.form["categoria"]
        error = None

        if not nome:
            error = "Il nome è obbligatorio."
        if not categoria:
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il canale
            canale_repo.create_channel(nome, numero_iscritti, categoria)
            return redirect(url_for("main.index"))
    categories_py: list[dict] = canale_repo.get_categoria()
    return render_template("blog/create_channel.html",  categories_html=categories_py)


@bp.route("/create_video", methods=("GET", "POST"))
def create_video():
    if request.method == "POST":
        canale_id = request.form["canale_id"]
        titolo = request.form["titolo"]
        durata = request.form["durata"]
        immagine = request.form["immagine"]

        error = None

        if not titolo:
            error = "Il nome è obbligatorio."
        if not durata:
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il canale
            canale_repo.create_video(canale_id, titolo, durata, immagine)
            return redirect(url_for("main.index"))
    channels_py: list[dict] = canale_repo.get_canale()
    
    return render_template("blog/create_video.html",  channels_html=channels_py)
