import requests
import json
import db_utils

    
def todos_utenti(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    dati_utente = db_utils.get_model(url)
    print("\n--- Todos dell'utente 1 ---")
    print(dati_utente)
    completate = 0
    non_completate = 0
    for todo in dati_utente:
        if todo['completed'] == False:
            non_completate += 1
        else:
            completate += 1
    print(f"Todos: {len(dati_utente)}")
    print(f"Totale Todos completate: {completate}")
    print(f"Totale Todos non completate: {non_completate}")
    
# Trova il primo todo incompleto (ovvero con completed: false).
def trova_primo_todo_incompleto(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    dati_utente = db_utils.get_model(url)
    for todo in dati_utente:
        if todo['completed'] == False:
            print("\n--- Primo Todo Incompleto ---")
            print(json.dumps(todo, indent=4))
            return todo
    print("Tutti i todos sono completati.")
    return None

#Se trovato, marca quel todo come completato utilizzando una richiesta PUT. 
# Altrimenti, segnala che non ci sono tutti incompleti.
def marca_todo_completato(user_id):
    todo_incompleto = trova_primo_todo_incompleto(user_id)
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos/{todo_incompleto['id']}"
    db_utils.get_model(url)
    try:
        response = requests.put(url, parametri={'completed': True})



        # Controlliamo lo status code
        response.raise_for_status()

        # Analizziamo la risposta del server
        post_creato = response.json()
        
        print("--- Todos modificato ---")
        print(f"Status Code: {response.status_code} (modificato!)")
        return post_creato
    except requests.exceptions.RequestException as err:
        print(f"Errore durante la richiesta: {err}")
    
if __name__ == "__main__":
    todos_utenti(1)
    trova_primo_todo_incompleto(1)
    marca_todo_completato(1)
    