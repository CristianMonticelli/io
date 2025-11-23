import requests
import json

# L'URL dell'endpoint per la creazione dei post
url = "https://jsonplaceholder.typicode.com/posts"

# 1. Prepariamo i dati da inviare nel corpo della richiesta.
# Deve essere un dizionario Python che verrà convertito in JSON.
nuovo_post = {
    'title': 'Il Mio Nuovo Post',
    'body': 'Questo è il contenuto del mio primo post creato tramite API!',
    'userId': 1
}

try:
    # 2. Eseguiamo la richiesta POST, passando i dati con il parametro `json`
    response = requests.post(url, json=nuovo_post)

    # 3. Controlliamo lo status code
    # Per una creazione, ci aspettiamo uno status code 201 (Created)
    response.raise_for_status()

    # 4. Analizziamo la risposta del server
    # Di solito, l'API restituisce l'oggetto che abbiamo creato, con l'ID assegnato dal server
    post_creato = response.json()

    print("--- Risposta dal Server ---")
    print(f"Status Code: {response.status_code} (Created!)")
    print(json.dumps(post_creato, indent=20))
    print(f"\nIl nostro post è stato creato con ID: {post_creato['id']}")

except requests.exceptions.RequestException as err:
    print(f"Errore durante la richiesta: {err}")