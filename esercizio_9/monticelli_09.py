import requests
import json

# Definiamo l'URL dell'endpoint a cui vogliamo fare la richie

url = f"https://jsonplaceholder.typicode.com/posts/"
try:
    # 1. Eseguiamo la richiesta GET
    response = requests.get(url)
    # 2. Controlliamo se la richiesta è andata a buon fine (status code 200 OK)
    response.raise_for_status()  # Solleva un'eccezione per status code 4xx o 5xx
    # 3. Estraiamo i dati JSON dalla risposta
    # Il metodo .json() converte automaticamente il corpo della risposta da stringa JSON a dizionario Python
    dati_utente = response.json()
    # 4. Usiamo i dati
    print("--- Dati Utente Ricevuti ---")
    # Usiamo json.dumps per una stampa "bella" (pretty-print) del dizionario
    print(json.dumps(dati_utente, indent=4))
    print("\n--- Post dell'utente 1 ---")
    print(f"userId: {dati_utente['userId']}")
    print(f"id: {dati_utente['id']}")
    print(f"title: {dati_utente['title']}")
    print(f"body: {dati_utente['body']}")
except requests.exceptions.HTTPError as err:
    print(f"Errore HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Errore durante la richiesta: {err}")