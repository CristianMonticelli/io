'''mermaid
    erDiagram
        negozio{
            int id PK
            string indirizzo
            string città
            int dipendente_ID FK
            int album_ID FK

        }

        dipendente{
            int id PK
            string nome
            string cognome
            int negozio_ID FK
        }

        album{
            int id PK
            string titolo
            float prezzo
            int artista_ID FK
            int righe_vendita_ID FK
        }

        artista{
            int id PK
            string nome
            string cognome
        }

        vendita {
        int id PK
        date data
        string negozio
        float importo_totale
        int negozio_ID FK
        int album_ID FK
        int righe_vendita_ID FK
        }

        riga_vendita{ 
            int album_ID FK
            int quantità
            int prezzo_unitario
    }
        dipendente ||--o{ negozio: lavorano
        negozio ||--o{ vendita: effettua
        negozio ||--o{ album: possiede
        riga_vendita }o--|| album: RIFERISCE
        vendita ||--o{ riga_vendita: contiene
        album }o--o{ artista: scritti


'''