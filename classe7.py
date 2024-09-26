class MaterialeBibblioteca:
    def __init__(self,titolo,anno_pubblicazione,disponibile : True):
        self.titolo = titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = disponibile 

    def prestito (self):
        self.disponibile = False

    def restituisce (self):
        self.disponibile = True

    def get_titolo (self):
        return self.titolo

    def is_disponibile (self):
        return self.disponibile





class Libro:
    def __init__(self,autore,n_pagine):
        self.autore = autore
        self.n_pagine = n_pagine
    def get_autore (autore):
    def modifica_n_pagine (n_pagine):



class Rivista:
    def __init__(self,n_edizione,mese_pubblicazione):
        self.n_edizione = n_edizione
        self.mese_pubblicazione = mese_pubblicazione
    def modifica_edizione (n_edizione):
    def cambia_mese_pubblicazione (mese_pubblicazione):


class DVD:
    def __init__(self,regista,durata):
        self.regista = regista
        self.durata = durata
    def correggi_regista (regista):
        
    def modifica_durata (durata):


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
risultati = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
for materiale in risultati:
    print(materiale.get_titolo())  # Output: Inception