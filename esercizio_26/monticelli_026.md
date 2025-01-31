```mermaid
classDiagram
    class Veicolo{
        +marca: str
        +targa: str
        +modello: str
        +tipo_carburante: str
    }
    class Auto{
        +cavalli: int
    }
    class Camion{
        +portata: int
    }
    class Flotta{
        +veicoli: list[Veicolo]
        +aggiungi_veicoli(Veicolo): dict{bool}
        +visualizzare_informazioni(): void
    }
    Auto --|> Veicolo
    Camion --|> Veicolo
    Flotta "1" --> "n*" Veicolo : gestisce

    
```