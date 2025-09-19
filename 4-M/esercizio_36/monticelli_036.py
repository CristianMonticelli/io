from enum import Enum
from dataclasses import dataclass, field
from typing import List

class ClassePersonaggio(Enum):
    GUERRIERO = "Guerriero"
    MAGO = "Mago"
    LADRO = "Ladro"

class Direzione(Enum):
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"

class TipoOggetto(Enum):
    POZIONE = "Pozione"
    AMULETO = "Amuleto"
    CHIAVE = "Chiave"

@dataclass
class Oggetto:
    nome: str
    descrizione: str
    raccoglibile: bool
    tipo: TipoOggetto

@dataclass
class Giocatore:
    nome: str
    email: str
    personaggioSelezionato: "Personaggio | None" = None
    personaggi: List['Personaggio'] = field(default_factory=list)
    
    def creaPersonaggio(self, nomePersonaggio, classePersonaggio):
        personaggio = Personaggio(nomePersonaggio, classePersonaggio)
        if personaggio not in self.personaggi:
            self.personaggi.append(personaggio)
            return personaggio

    def selezionaPersonaggio(self, personaggio):
        if personaggio in self.personaggi:
            self.personaggioSelezionato = personaggio
            
@dataclass
class Personaggio:
    
    nomePersonaggio: str
    classePersonaggio: ClassePersonaggio
    livello: int = 1
    puntiVita: int = 100
    stanzaCorrente: "Stanza | None" = None
    inventario: List[Oggetto] = field(default_factory=list)

    def muovi(self, direzione: Direzione):
        pass

    def raccogliOggetto(self, oggetto: Oggetto):
        if oggetto.raccoglibile:
            self.inventario.append(oggetto)
            print(f"Oggetto {oggetto.nome} raccolto.")
            return True
        return False
    
    def usaOggetto(self, oggetto: Oggetto):
        if oggetto in self.inventario:
            self.inventario.remove(oggetto)
            print(f"Oggetto {oggetto.nome} usato.")
            return True
        return False

@dataclass
class Stanza:
    
    numeroStanza: int
    descrizioneStanza: str
    oggetti: List[Oggetto] = field(default_factory=list)
    #stanza
    stanzaUp: "Stanza | None" = None
    stanzaDown: "Stanza | None" = None
    stanzaLeft: "Stanza | None" = None
    stanzaRight: "Stanza | None" = None
    stanzaAperta: bool = False

    def descrivi_stanza(self):
        return f"Stanza {self.numeroStanza}: {self.descrizioneStanza}"

giocatore = Giocatore("Mario", "mariorossi@gmail.come")
personaggio = giocatore.creaPersonaggio("Mario", ClassePersonaggio.MAGO)
