from typing import List, Tuple
import requests
import json

def show_fetched_data(results: List[Tuple]):
    #Stampa i risultati di una query del database.
    for row in results:
        print(row)


def get_model(url):
    try:
        response = requests.get(url)
        # Controlliamo se la richiesta è andata a buon fine (status code 200 OK)
        response.raise_for_status()  # Solleva un'eccezione per status code 4xx o 5xx
        # Estraiamo i dati JSON dalla risposta
        dati = response.json()
        # Usiamo i dati
        print("--- Dati Ricevuti ---")
        # Usiamo json.dumps per una stampa "bella" (pretty-print) del dizionario
        print(json.dumps(dati, indent=4))
        return dati
    except requests.exceptions.HTTPError as err:
        print(f"Errore HTTP: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Errore durante la richiesta: {err}")

def posts_model(url, nuovo):
    try:
        #Eseguiamo la richiesta POST, passando i dati con il parametro `json`
        response = requests.post(url, json=nuovo)

        # Controlliamo lo status code
        response.raise_for_status()

        # Analizziamo la risposta del server
        post_creato = response.json()
        
        print("--- Nuovo Creato ---")
        print(f"Status Code: {response.status_code} (Created!)")
        return post_creato
    except requests.exceptions.RequestException as err:
        print(f"Errore durante la richiesta: {err}")

def put_model(url, aggiornato):
    try:
        response = requests.put(url, aggiornato)

        # Controlliamo lo status code
        response.raise_for_status()

        # Analizziamo la risposta del server
        post_creato = response.json()
        
        print("--- Todos modificato ---")
        print(f"Status Code: {response.status_code} (modificato!)")
        return post_creato
    except requests.exceptions.RequestException as err:
        print(f"Errore durante la richiesta: {err}")