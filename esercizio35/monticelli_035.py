from flask import Flask,render_template
import json
app = Flask(__name__)
@app.route("/")
def Welcome():
    return "<p>Welcome to our Weather Application!</p>"

@app.route("/cities")
def Welcome_to_italy(): 
    messaggio = "yuyu"  
    return render_template("file.html",messaggio=messaggio)

@app.route("/meteo/")
@app.route("/meteo/<cities>")
def meteo(cities=None):
    return f"Weather for {cities}"

def read_json ():
    with open("meteo.json", "r") as file_json:
        try:        
            mylist = json.load(file_json)    
        except:        
            mylist = []
    
    return mylist

@app.route("/meteo_dinamico/")
@app.route("/meteo_dinamico/<citta>")
def meteo(citta=None):
    lista_citta = read_json()
    return f"{lista_citta[citta]}"