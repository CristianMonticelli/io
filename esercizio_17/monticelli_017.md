```mermaid
classDiagram
    class Insegante {
        -nome : string
        -cognome : string
        -strumento : string
        
    }
    
    class Studente {
        -nome : string
        -cognome : string
        
    }

    class Corso {
        -nome : string
        -durata : int
    }
    

    

    Insegante "1" --> "n" Studente : insegna
    Studente "n" --> "n" Corso : iscritti

    



```
