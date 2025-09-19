class Piatto:
    def __init__(self,nome,prezzo):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = True

    def get_nome_piatto(self):
        return self.nome

    def get_prezzo_piatto(self):
        return self.prezzo

    def is_disponibile (self):
        return self.disponibile

    def ordina (self):
        if self.is_disponibile():
            self.disponibile = False
            return True
        return False

    def disponibile (self):
        if self.is_disponibile():
            raise Exception('il piatto e disponibile')
        self.disponibile = True

    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"

class Antipasto(Piatto):
    def __init__(self,nome,prezzo,ingredienti,porzione):
        super().__init__(nome,prezzo)
        self.ingredienti = ingredienti
        self.porzione = porzione

    def get_ingredienti_piatto(self):
        return self.ingredienti

    def get_porzione_piatto(self):
        return self.porzione
    
    def __str__(self):
        #super.__str__(self)
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - {self.ingredienti} - {self.porzione}"
    
class Primo(Piatto):
    def __init__(self,nome,prezzo,tipo_pasta ,sugo):
        super().__init__(nome,prezzo)
        self.tipo_pasta  = tipo_pasta 
        self.sugo = sugo
    
    def get_tipo_pasta(self):
        return self.tipo_pasta

    def get_sugo(self):
        return self.sugo

    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} -{self.tipo_pasta} - {self.sugo}"

class Secondo(Piatto):
    def __init__(self,nome,prezzo,tipo_carne ,cottura):
        super().__init__(nome,prezzo)
        self.tipo_carne  = tipo_carne 
        self.cottura = cottura
    def get_tipo_carne(self):
        return self.tipo_carne

    def get_cottura(self):
        return self.cottura
    
    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - {self.tipo_carne} - {self.cottura}"

class Dolce(Piatto):
    def __init__(self,nome,prezzo,tipo_dolce ,calorie):
        super().__init__(nome,prezzo)
        self.tipo_dolce  = tipo_dolce 
        self.calorie = calorie
    def get_tipo_dolce(self):
        return self.tipo_dolce

    def get_calorie_piatto(self):
        return self.calorie
    
    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - {self.tipo_dolce} - {self.calorie}"

def calcola_conto(piatti_ordinati):
    conto_totale = 0
    for p in piatti_ordinati:
        
        conto_totale += p.prezzo
    return conto_totale

def stampa_menu(piatti_ordiunati):
    for p in piatti_ordinati:
        print(f'{type(p).__name__}: {p} ')
    # type(piatti_ordiunati[0]).__name__
# Esempio di utilizzo
antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")  # Output: Il conto totale è: 48.0€

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)