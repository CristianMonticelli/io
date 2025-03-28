class ElementoMenu:
    def __init__(self, codice, nome, prezzo, tempo_preparazione, allergeni):
        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo
        self.tempo_preparazione = tempo_preparazione
        self.allergeni = allergeni
        self.disponibilita = True
    
    def set_diponibile(self):
        if self.disponibilita == True:
            self.disponibilita = False
        if self.disponibilita == False:
            self.disponibilita = True
            
class PrimoPiatto:
    def __init__(self,pasta,vegetariano, codice, nome, prezzo, tempo_preparazione, allergeni):
        super().__init__(codice, nome, prezzo, tempo_preparazione, allergeni)
        self.pasta = pasta
        self.vegetariano = vegetariano

class SecondoPiatto:
    def __init__(self,cottura, codice, nome, prezzo, tempo_preparazione, allergeni):
        super().__init__(codice, nome, prezzo, tempo_preparazione, allergeni)
        self.cottura = cottura

class Ordine:
    def __init__(self,numero_ordine, data_ora, stato,elementi):
        self.numero_ordine= numero_ordine
        self.data_ora= data_ora
        self.stato= stato
        self.elementi= elementi

class Tavolo:
    def __init__(self,numero, posti, stato):
        self.numero= numero
        self.posti= posti
        self.stato= stato
        
        
        
    