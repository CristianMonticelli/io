from flask import Flask, render_template
import json

app = Flask(__name__)



@app.route("/")
def index():
    with open("studenti.json") as f:
        studenti = json.load(f)
    return render_template("dinamic.html", studenti=studenti)


if __name__ == "__main__":
    app.run(port=5104, debug=True) 
    