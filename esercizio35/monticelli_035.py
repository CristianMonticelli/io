from flask import Flask,render_template
import json
app = Flask(__name__)
@app.route("/")
def Welcome():
    return "<p>Welcome to our Weather Application!</p>"

@app.route("/cities")
def Welcome_to_italy():    
    return render_template("file.html")
