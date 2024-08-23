from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

#radice
@app.route('/')
def home():
    return "Flashcard App"

#passaggio dati
@app.route("/nome_pagina")
def Welcome_to_italy(): 
    messaggio = "yuyu"  #dato
    return render_template("file_da_usare.html",messaggio=messaggio)

#apertura 'stanza'
if __name__ == "__main__":
    app.run(debug=True, port=random.randint(2000,5000)) 