# ESERCIZIO CRUD TEMPLATE - DOCUMENTAZIONE AGGIORNATA

## 📊 Struttura del Progetto

```
esercizio_crud_template/
├── app/
│   ├── __init__.py                 # Configurazione Flask e Database
│   ├── main.py                     # Routes (GET, POST per CRUD)
│   ├── schema.sql                  # Definizione tabella 'items'
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── item_repository.py      # Funzioni database (SELECT, INSERT, UPDATE, DELETE)
│   └── templates/
│       ├── base.html               # Template base con styling
│       ├── index.html              # Lista di item
│       ├── create.html             # Form creazione
│       ├── update.html             # Form modifica
│       └── view.html               # Dettagli singolo item
├── run.py                          # Entry point (avvia Flask)
└── README.md
```

---

## 🗄️ DATABASE (schema.sql)

**Tabella: `items`**
```sql
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Chiave primaria auto-incrementante
    name TEXT NOT NULL,                    -- Nome item (obbligatorio)
    description TEXT,                      -- Descrizione (opzionale)
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Data creazione automatica
);
```

**Dati di esempio:** 5 item pre-caricati (Laptop, Mouse, Tastiera, Monitor, Cuffie)

---

## 🔧 REPOSITORY (item_repository.py)

Contiene tutte le funzioni per interagire con il database:

### 1. **get_all_items()**
- Recupera TUTTI gli item
- Ordina per data creazione (decrescente = più recenti prima)
- Usato in: `main.index()`

### 2. **get_item_by_id(item_id)**
- Recupera UN item per ID
- Torna `None` se non esiste
- Usato in: `main.view_item()`, `main.update()`, `main.delete()`

### 3. **create_item(name, description)**
- Inserisce nuovo item nel database
- Effettua `db.commit()` per salvare
- Usato in: `main.create()` (POST)

### 4. **update_item(item_id, name, description)**
- Modifica item esistente
- Usato in: `main.update()` (POST)

### 5. **delete_item(item_id)**
- Elimina item dal database
- Usato in: `main.delete()` (POST)

---

## 🛣️ ROUTES (main.py)

| Route | Metodo | Cosa Fa | Template |
|-------|--------|---------|----------|
| `/` | GET | Lista tutti gli item | `index.html` |
| `/create` | GET | Mostra form vuoto | `create.html` |
| `/create` | POST | Salva nuovo item → Redirect home | - |
| `/item/<id>` | GET | Mostra dettagli item | `view.html` |
| `/update/<id>` | GET | Mostra form pre-compilato | `update.html` |
| `/update/<id>` | POST | Salva modifiche → Redirect dettagli | - |
| `/delete/<id>` | POST | Elimina item → Redirect home | - |

### Flusso Tipico (Create):
```
GET /create → Mostra form
    ↓ (utente compila form)
POST /create → Salva nel DB
    ↓
Redirect a / (homepage)
```

### Flusso Tipico (Update):
```
GET /update/5 → Mostra form con dati item 5
    ↓ (utente modifica)
POST /update/5 → Aggiorna item 5 nel DB
    ↓
Redirect a /item/5 (dettagli)
```

---

## 🎨 TEMPLATES HTML

### base.html
- **Cosa è:** Template padre con CSS e struttura
- **Contiene:**
  - Barra di navigazione (Home + Nuovo)
  - Sistema flash messages (mostra errori/successi)
  - CSS completo (tabelle, form, bottoni)
  - Block `{% block content %}` per i contenuti specifici

### index.html
- **Mostra:** Tabella con lista di item
- **Colonne:** ID | Nome | Azioni (Visualizza, Modifica, Elimina)
- **Azioni:**
  - `Visualizza` → GET `/item/<id>`
  - `Modifica` → GET `/update/<id>`
  - `Elimina` → POST `/delete/<id>` (con conferma)

### create.html
- **Form con campi:**
  - `name` (TEXT - obbligatorio)
  - `description` (TEXTAREA)
- **Bottoni:** Salva | Annulla

### update.html
- **Form con campi pre-compilati** (legge valori da `item`)
- **Salva modifiche** → Torna ai dettagli

### view.html
- **Mostra:**
  - ID
  - Nome
  - Descrizione
  - Data di creazione
- **Azioni:** Modifica | Elimina | Torna alla lista

---

## 🚀 COME AVVIARE

### 1. Installare dipendenze
```bash
pip install flask
```

### 2. Avviare l'app
```bash
cd esercizio_crud_template
python run.py
```

Vai su: **http://localhost:5000**

### 3. Il database si inizializza automaticamente
- Al primo avvio, `schema.sql` crea la tabella `items`
- Viene pre-caricata con 5 item di esempio

---

## ✅ FUNZIONALITÀ AGGIORNATE

✅ **CREATE** - Crea nuovo item con form validato  
✅ **READ** - Visualizza lista e dettagli item  
✅ **UPDATE** - Modifica item con form pre-compilato  
✅ **DELETE** - Elimina con conferma  
✅ **Flash Messages** - Mostra successi/errori  
✅ **Validazione** - Campo nome obbligatorio  
✅ **Design** - Interfaccia moderna e responsive  
✅ **Tabella creata** - Con dati di esempio  

---

## 💡 COSA AGGIUNGERE DOMANI (Opzionale)

Se vuoi estendere:

1. **Ricerca** - Aggiungi `/search?q=...` per cercare per nome
2. **Filtri** - Per categoria o data
3. **Paginazione** - Limite item per pagina
4. **Ordinamento** - Ordina per nome/data
5. **Autenticazione** - Login/Logout (come in monticelli)
6. **Commenti** - Per ogni item (come post_comments in monticelli)
7. **Validazioni avanzate** - Email, numeri, ecc.
8. **API REST** - Aggiungi endpoint JSON

---

## 🔍 ERRORI COMUNI & SOLUZIONI

| Errore | Causa | Soluzione |
|--------|-------|-----------|
| "table items does not exist" | schema.sql non eseguito | Eliminare `app.db` e riavviare |
| Item form non salva | Campo `name` vuoto o mancante | Compilare il campo nome |
| 404 su `/item/999` | ID non esiste | Controllare ID da homepage |
| "No such column" | Typo nel nome colonna | Controllare schema.sql |

---

**Creato:** 27 Gennaio 2026  
**Pronto per la verifica di domani!** ✅
