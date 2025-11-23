import requests
import json
import db_utils

    
def post_utenti(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/posts"
    dati_utente = db_utils.get_model(url)
    print("\n--- Post dell'utente 1 ---")
    for post in dati_utente:
        print(f"ID Post: {post['userId']}, Titolo: {post['title']}")
    
def commenti(posts_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{posts_id}/comments"
    dati_utente = db_utils.get_model(url)
    print("--- Commenti per il primo post ---")
    for comment in dati_utente:
        print(f"ID Commenti: {comment['id']}, Titolo: {comment['name']}")

def nuovo_commento(nuovo_comment):
    url = "https://jsonplaceholder.typicode.com/comments"
    post_creato = db_utils.posts_model(url, nuovo_comment)
    print(json.dumps(post_creato, indent=20))
    print(f"\nIl nostro post è stato creato con ID: {post_creato['id']}")

    
if __name__ == "__main__":
    post_utenti(1)
    commenti(1)
    nuovo_commento({
    "postId": 1,
    "id": 501,
    "name": "Nuovo Commentatore",
    "email": "nuovo@example.com",
    "body": "Questo è un commento aggiunto tramite API!"
})