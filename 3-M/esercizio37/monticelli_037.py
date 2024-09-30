from flask import Flask, render_template
import json

app = Flask(__name__)



@app.route("/")
def index():
    with open("links.json") as f:
        data = json.load(f)
    return render_template("dinamic.html", links=data)


if __name__ == "__main__":
    app.run() 
    