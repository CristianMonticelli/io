class MaterialeBiblioteca:
    def __init__(self,titolo,anno_pubblicazione):
        self.titolo = titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = True 

    def prestito (self):
        if self.is_disponibile():
            self.disponibile = False
            return True
        return False
    def restituzione (self):
        if self.is_disponibile():
            raise Exception('il libro non e prestato')
        self.disponibile = True

    def get_titolo (self):
        return self.titolo

    def is_disponibile (self):
        return self.disponibile

    @staticmethod
    def ricerca (materiali, titolo):
        oggetti = []
        for materiale in materiali:
            if materiale.get_titolo() == titolo:
                oggetti.append(materiale)
        return oggetti
                #return materiale




class Libro(MaterialeBiblioteca):
    def __init__(self,titolo,anno_pubblicazione,autore,n_pagine):
        super().__init__(titolo,anno_pubblicazione)
        self.autore = autore
        self.n_pagine = n_pagine
    def get_autore (self):
        return self.autore
    def get_n_pagine (self):
        return  self.n_pagine


class Rivista(MaterialeBiblioteca):
    def __init__(self,titolo,anno_pubblicazione,n_edizione,mese_pubblicazione):
        super().__init__(titolo,anno_pubblicazione)
        self.n_edizione = n_edizione
        self.mese_pubblicazione = mese_pubblicazione
    def get_numero_edizione (self):
        return self.n_edizione
    def get_mese_pubblicazione (self):
        return self.mese_pubblicazione

class DVD(MaterialeBiblioteca):
    def __init__(self,titolo,anno_pubblicazione,regista,durata):
        super().__init__(titolo,anno_pubblicazione)
        self.regista = regista
        self.durata = durata
    def get_regista (self):
        return self.regista
    def get_durata (self):
        return self.durata

# Esempio di utilizzo
libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
print(libro.get_titolo())  # Output: Il Signore degli Anelli
print(libro.get_autore())  # Output: J.R.R. Tolkien
libro.prestito()
print(libro.is_disponibile())  # Output: False
libro.restituzione()
print(libro.is_disponibile())  # Output: True

rivista = Rivista("National Geographic", 2023, 5, "Maggio")
print(rivista.get_titolo())  # Output: National Geographic
print(rivista.get_numero_edizione())  # Output: 5

dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_titolo())  # Output: Inception
print(dvd.get_regista())  # Output: Christopher Nolan

materiali = [libro, rivista, dvd]
#risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
#print(risultato.get_titolo())  # Output: Inception

risultati = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
for materiale in risultati:
   print(materiale.get_titolo())  # Output: Inception