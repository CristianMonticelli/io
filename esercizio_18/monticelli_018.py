class Persona:
    def __init__ (self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,new_nome):
        self._nome= new_nome
    @property
    def cognome(self):
        return self._cognome
    @cognome.setter
    def cognome(self,new_cognome):
        self._cognome= new_cognome

class Allenatore(Persona):
    def __init__ (self, nome, cognome, specializzazione):
        super().__init__(nome,cognome)
        self._specializzazione = specializzazione
        self.corsi = []
        self.membri = []

    @property
    def specializzazione(self):
        return self._specializzazione
    @specializzazione.setter
    def specializzazione(self,new_specializzazione):
        self._specializzazione= new_specializzazione
    
    def assegna_membri(self,membro):
    
        if membro not in self.membri:
            self.membri.append(membro)
            membro.assegna_allenatore(self)
    def assegna_corsi(self,corso):
    
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.assegna_allenatore(self)
        
        
        
class Membro(Persona):
    def __init__ (self, nome, cognome, corsi):
        super().__init__(nome,cognome)
        self._corsi = corsi
        self.scheda = None
        self.allenatore = None
        self.corsi = []

    @property
    def corsi(self):
        return self._corsi
    @corsi.setter
    def corsi(self,new_corsi):
        self._corsi= new_corsi

    def assegna_scheda(self,scheda):
        if scheda == None:
            self.scheda = scheda
            scheda.aggiungi_membro(self)
    
    def assegna_allenatore(self,allenatore):
            if allenatore == None:
                self.allenatore = allenatore
                allenatore.assegna_membri(self)
    
    def iscriviti_corso(self,corso):
    
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.assegna_membri(self)

        
    
class Corso:
    def __init__ (self, nome, durata):  
        self._nome = nome
        self._durata = durata
        self.allenatore = None
        self.membri = []
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,new_nome):
        self._nome= new_nome
    @property
    def durata(self):
        return self._durata
    @durata.setter
    def durata(self,new_durata):
        self._durata= new_durata
    def assegna_allenatore(self,allenatore):
        if allenatore == None:
            self.allenatore = allenatore
            allenatore.assegna_corsi(self)
    
    def assegna_membri(self,membro):
    
        if membro not in self.membri:
            self.membri.append(membro)
            membro.assegna_membri(self)
    
class SchedaAllenamento:
    def __init__ (self,lista_esercizi):
        self._lista_esercizi = lista_esercizi
        self.membro = None
    @property
    def lista_esercizi(self):
        return self._lista_esercizi
    @lista_esercizi.setter
    def lista_esercizi(self,new_lista_esercizi):
        self._lista_esercizi= new_lista_esercizi

    def aggiungi_membro(self,membro):
        if membro == None:
            self.studenti = membro
            membro.assegna_scheda(self)

def main():
    # Creazione degli allenatori
    allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
    allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

    # Creazione dei membri
    membro1 = Membro("Anna", "Verdi")
    membro2 = Membro("Marco", "Neri")

    # Assegnazione degli allenatori ai membri
    membro1.set_allenatore(allenatore1)
    membro2.set_allenatore(allenatore2)

    # Creazione dei corsi
    corso1 = Corso("Pilates", "3 mesi", allenatore1)
    corso2 = Corso("HIIT", "6 mesi", allenatore1)
    corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

    # Iscrizione dei membri ai corsi
    membro1.iscrivi_corso(corso1)
    membro1.iscrivi_corso(corso2)
    membro2.iscrivi_corso(corso3)

    # Creazione delle schede di allenamento
    scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
    scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

    # Assegnazione delle schede di allenamento ai membri
    membro1.set_scheda_allenamento(scheda1)
    membro2.set_scheda_allenamento(scheda2)

    # Stampa delle informazioni
    print(membro1)
    print(membro2)

if __name__ == "__main__":
    main()