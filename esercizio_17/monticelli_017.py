class Insegnante:
    def __init__(self,nome,cognome,strumento):
        self._nome=nome
        self._cognome = cognome
        self._strumento = strumento

        self.studenti = []

    def aggiungi_studente(self,studente):
        
        if studente not in self.studenti:
            self.studenti.append(studente)
            studente.set_insegnante(self)
    
    @property
    def nome(self):
        return self._nome
    @property
    def cognome(self):
        return self._cognome
    @nome.setter
    def nome(self,new_nome):
        self._nome= new_nome
    @cognome.setter
    def cognome(self,new_cognome):
        self._cognome= new_cognome

    @property
    def strumento(self):
        return self._strumento
    @strumento.setter
    def strumento(self,new_strumento):
        self._strumento= new_strumento


class Studente:
    def __init__(self,nome,cognome):
        self._nome=nome
        self._cognome = cognome
        self.corsi = []
        self.insegnanti = None

    def iscrivi_corso(self,corso):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.aggiungi_studente(self)
    
    def set_insegnante(self,insegnante):
            if insegnante == None:
                self.insegnante = insegnante
                insegnante.aggiungi_studente(self)


    @property
    def nome(self):
        return self._nome
    @property
    def cognome(self):
        return self._cognome
    @nome.setter
    def nome(self,new_nome):
        self._nome= new_nome
    @cognome.setter
    def cognome(self,new_cognome):
        self._cognome= new_cognome
    
    def __str__(self):
        return f"{self._nome} - {self._cognome}"


class Corso:
    def __init__(self,nome,durata):
        self._nome = nome
        self._durata = durata
        self.studenti = []

    @property
    def nome(self):
        return self._nome
    @property
    def durata(self):
        return self._durata
    @nome.setter
    def nome(self,new_nome):
        self._nome= new_nome
    @durata.setter
    def durata(self,new_durata):
        self._durata= new_durata

    def aggiungi_studente(self,studente):
        if studente not in self.studenti:
            self.studenti.append(studente)
            studente.iscrivi_corso(self)


def main():
    # Creazione degli insegnanti
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    # Creazione degli studenti
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    # Assegnazione degli insegnanti agli studenti
    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)

    # Creazione dei corsi
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    # Iscrizione degli studenti ai corsi
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Stampa delle informazioni
    print(studente1)
    print(studente2)

if __name__ == "__main__":
    main()