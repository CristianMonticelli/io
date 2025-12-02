import utils
import requests
import json

# def todos_utenti():
#     url = f"http://localhost:3001"
#     dati_utente = utils.get_model(url)
#     print(f"{dati_utente}")
# todos_utenti()

def libriAutore(id):
    url = f"http://localhost:3001/books/?author_id={id}"
    dati_utente = utils.get_model(url)
    print(dati_utente)
    for dato in dati_utente:
        print(f"- {dato['title']} ({dato['pages']}) ")
    
def aggiungilibriAutore(nuovo):
    url = f"http://localhost:3001/books"
    dati_utente = utils.posts_model(url, nuovo)
    print(json.dumps(dati_utente, indent=20))
    print(dati_utente)
    
    
def nuovo_commento(nuovo_comment):
    url = "https://jsonplaceholder.typicode.com/comments"
    post_creato = utils.posts_model(url, nuovo_comment)
    print(json.dumps(post_creato, indent=20))
    print(f"\nIl nostro post è stato creato con ID: {post_creato['id']}")

    
if __name__ == "__main__":
   
    aggiungilibriAutore({ "id": 1006, "author_id": 3, "genre_id": 101, "title": "Casali e i 7 ladroni", "pages": 104, "available": False })
# print("Libri di Daniele Pennac:")
# libriAutore(1)

# aggiungilibriAutore({ "id": 1006, "author_id": 3, "genre_id": 101, "title": "Casali e i 7 ladroni", "pages": 104, "available": False })
