from flask import Flask, render_template, request
import json
app = Flask(__name__)
ricette = []
FILE_PATH = "ricetta.json"  
try:
    with open(FILE_PATH, 'r') as file:
        ricette = json.load(file)
except FileNotFoundError:
    pass

print(ricette)
id = int(input('id:'))

for ricetta in ricette:
    if ricetta['id']==id:
        print(ricetta)
    

@app.route('/ricetta')
def indice():
    file_json = "ricetta.json"
    with open(file_json, "w") as f:
      json.dump(ricette, f)
    f.close()
    return render_template('ricetta.html',ricette=ricette)
    
#@app.route('/ricetta/<id>')
#def ricetta(id=None):
#    return type(ricette)
    #for ricetta in ricette:
    #    if ricetta['id']==id:
    #        return f"{ricetta}"
#
#
#
#
#
file_json = "ricetta.json"
with open(file_json, "w") as f:
  json.dump(ricette, f)
f.close()
    