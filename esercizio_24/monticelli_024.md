```mermaid
classDiagram
    class Film{
            +str titolo
            +str regista
            +str anno_di_uscita
            +str genere
            +int valutazione
            
            

        }
    class Libreria{
            +str titolo
    
            -Aggiungi_film
            -Rimuovi_film
            -Cercare_film
            -Visualizzare_tutti_film
            -Valutazione_media_film
        }
    
        Libreria"1" -- "n*" Film : raccoglie
    
```