from flask import Flask, render_template, request, redirect, url_for
import json
import random
app = Flask(__name__)
flashcards = [{}]
FILE_PATH = "flashcards.json"  
try:
    with open(FILE_PATH, 'r') as file:
        flashcards = json.load(file)
except FileNotFoundError:
    pass

@app.route('/')
def home():
    return "Flashcard App"


# @app.route('/flashcards')
# def index():
#     return render_template('monticelli_039.html',flashcard=None)

@app.route('/flashcards/<id>',methods=['GET','POST'])
def login(id=None):
    id = int(id)
    for _flashcard in flashcards:
            if id==_flashcard["id"]:
                 flashcard=_flashcard
                 
    if request.method=='POST':
        answer = request.form['answer']
        if answer.lower()==flashcard['answer'].lower():
             message='giusto'
        else:
             message='sbagliato'
        return render_template("monticelli_039.html",flashcard=flashcard,message=message)
    else:    
        return render_template("monticelli_039.html",flashcard=flashcard,message=None)
            
    
    file_json = "flashcards.json"
    with open(file_json, "w") as f:
        json.dump(flashcards, f)
    f.close()
    
    return 'non esiste una domandacon questo id'

@app.route('/flashcards/random',methods=['GET','POST'])
def random_test():
    flashcard=random.choices(flashcards)
    print(flashcard[0])
    
    
    file_json = "flashcards.json"
    with open(file_json, "w") as f:
        json.dump(flashcards, f)
    f.close()
    
    return redirect(url_for('login', id=flashcard[0]["id"]))
    # return render_template('monticelli_039.html', flashcard=flashcard[0])

if __name__ == "__main__":
    app.run(debug=True, port=6783) 