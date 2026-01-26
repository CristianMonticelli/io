# CRUD Template - Guida per la Verifica

## Cosa hai trovato

Una struttura Flask CRUD completa ma **vuota** pronta da riempire domani:

### 📁 Struttura
```
esercizio_crud_template/
├── run.py                          # Avvia l'app
├── app/
│   ├── __init__.py                # Configura Flask e Database
│   ├── main.py                    # Routes CRUD (GET, POST, UPDATE, DELETE)
│   ├── schema.sql                 # Schema database VUOTO
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── item_repository.py    # Query SQL (TODO)
│   └── templates/
│       ├── base.html              # Template base con CSS
│       ├── index.html             # Lista item
│       ├── create.html            # Form creazione
│       ├── view.html              # Dettagli item
│       └── update.html            # Form modifica
```

## 🔧 Cosa devi fare domani

1. **schema.sql** → Definisci la tabella con i campi che servono
   ```sql
   CREATE TABLE items (
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       description TEXT,
       -- AGGIUNGI I TUOI CAMPI
   );
   ```

2. **item_repository.py** → Implementa le query SQL nei TODO
   - `get_all_items()` - SELECT
   - `get_item_by_id()` - SELECT WHERE
   - `create_item()` - INSERT
   - `update_item()` - UPDATE
   - `delete_item()` - DELETE

3. **main.py** → Completa i TODO dei form
   - Leggi i dati da `request.form`
   - Chiama le funzioni del repository

4. **create.html e update.html** → Aggiungi gli `<input>` per i tuoi campi

## ▶️ Come avviare

```bash
cd esercizio_crud_template
python run.py
# Vai su http://localhost:5000
```

## 📝 Riepilogo TODO

- [ ] Modifica `schema.sql` con la tua tabella
- [ ] Implementa le 5 query in `item_repository.py`
- [ ] Completa i form nei template HTML
- [ ] Completa i TODO in `main.py`
- [ ] Testa tutto funziona

Struttura già collegata ✅ Database pronto ✅ HTML già bello ✅
