# Spiegazione - Ricerca Prodotti

Questo documento spiega il funzionamento della pagina `templates/index.html` nella cartella `esercizio4`.

## Scopo
La pagina permette di cercare un prodotto inserendo un codice nel formato "Una lettera + tre cifre" (es. A123). Alla pressione del pulsante "Cerca" o del tasto Invio viene effettuata una richiesta all'endpoint `/prodotto?codice=...` e vengono mostrati i dettagli del prodotto ricevuti dal server.

## Validazione
- L'input è validato lato client con la regex `^[A-Za-z]\d{3}$`.
- Se il formato non è corretto, viene mostrato un alert e la richiesta non viene inviata.

## Chiamata al server
- La funzione `cercaProdotto` usa `fetch` con `async/await`.
- Il codice viene passato tramite `encodeURIComponent` per evitare problemi con caratteri speciali.
- Si aspetta una risposta JSON con almeno questi campi:
  - `prezzo` (numero o stringa)
  - `marca` (stringa)
  - `modello` (stringa)

Nota: il server normalizza il codice in maiuscolo prima di cercarlo nel DB e le risposte JSON includono ora una chiave `ok` boolean per indicare successo o fallimento.

Esempio di risposta attesa (200 OK):

```json
{
  "ok": true,
  "prezzo": 1200,
  "marca": "Dell",
  "modello": "XPS 13"
}
```

In caso di errore l'API può restituire uno JSON del tipo:

```json
{
  "ok": false,
  "errore": "Prodotto non trovato"
}
```

## Gestione errori
- Se la risposta HTTP non è ok (status 4xx/5xx), il client cerca il campo `errore` nel JSON e lo mostra; altrimenti mostra un messaggio generico "Errore nella risposta del server.".
- Errori di rete vengono catturati e mostrati come "Errore di rete. Riprovare.".

## Miglioramenti introdotti
- Codice più leggibile usando `async/await` invece di `XMLHttpRequest`.
- Gestione degli errori di rete e parsing JSON più robusta.
- Supporto per invio tramite tasto Enter.
- Funzione `pulisci` aggiornata per riportare il focus sull'input.

## Come testare
1. Inizializza il database (una tantum):

```bash
cd esercizio4
python3 init_db.py
```

2. Avvia l'app:

```bash
cd esercizio4
python3 run.py
```

3. Apri il browser su `http://localhost:5002/` e inserisci un codice valido (es. A123) e premi Cerca o Invio.

## Note
- Il server deve restituire header `Content-Type: application/json` per le risposte JSON.
- Se vuoi posso aggiungere un minimo CSS o migliorare l'accessibilità (aria-live per aggiornamenti dinamici, messaggi più descrittivi, ecc.).
