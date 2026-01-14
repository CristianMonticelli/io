from flask import Flask, render_template, request, redirect, url_for
import json
import random
app = Flask(__name__)
ricetta = [{}]
FILE_PATH = "ricetta.json"  
try:
    with open(FILE_PATH, 'r') as file:
        ricetta = json.load(file)
except FileNotFoundError:
    pass

@app.route('/')
def home():
    return "Ricetta App"

@app.route('/ricetta/<id>',methods=['GET','POST'])
def ricette(id=None):
    id = int(id)
    
    
    for r in ricetta:
            if id==r["id"]:
                
                return render_template("ricetta.html",ricetta_richiesta=r)
    
    
    
    file_json = "flashcards.json"
    with open(file_json, "w") as f:
        json.dump(flashcards, f)
    f.close()
    
    return 'non esiste una ricetta a questo id'
    
@app.route('/ricette',methods=['GET','POST'])
def ricette_link():
    return render_template("ricette.html",links=ricetta)
if __name__ == "__main__":
    app.run(debug=True, port=6611) 