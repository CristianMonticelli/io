class Ricetta:
    ...
    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"

class Primo(Ricetta):
    def __init__(self,nome,prezzo,tipo_pasta ,sugo):
        super().__init__(nome,prezzo)
        self.tipo_pasta  = tipo_pasta 
        self.sugo = sugo
    
    def get_tipo_pasta(self):
        return self.tipo_pasta
    
    @property
    def tipo_pasta (self) -> bool|str: 
        if self._titolo != None:
            
            return self._titolo
        return False

    def get_sugo(self):
        return self.sugo

    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} -{self.tipo_pasta} - {self.sugo}"

class Secondo(Ricetta):
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

class Dolce(Ricetta):
    def __init__(self,nome,prezzo,tipo_dolce ,calorie):
        super().__init__(nome,prezzo)
        self.tipo_dolce  = tipo_dolce 
        self.calorie = calorie
    def get_tipo_dolce(self):
        return self.tipo_dolce

    def get_calorie_Ricetta(self):
        return self.calorie
    
    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - {self.tipo_dolce} - {self.calorie}"

def stampa_menu(piatti_ordiunati):
    for p in piatti_ordinati:
        print(f'{type(p).__name__}: {p} ')
# Esempio di utilizzo
primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")

ricette = [primo, secondo, dolce]
ricette_possibili = verifica_ingredienti(ricette, ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"])
print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")

print("\nInformazioni sulle ricette:")
stampa_ricette(ricette)