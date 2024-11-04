class Ricetta:
    def __init__(self,nome,tempo_cottura,ingredienti,difficolta):
        self.nome = nome
        self.tempo_cottura = tempo_cottura
        self.ingredienti = ingredienti
        self.disponibile = True
        self.difficolta = difficolta
  
    def aggiungi_ingrediente(self,ingrediente):
        self.ingredienti.append(ingrediente)
    
    def __str__(self):
        return f"{self.nome} - {self.tempo_cottura} min - Difficoltà: {self.difficolta}"

class Primo(Ricetta):
    def __init__(self,nome,tempo_cottura,ingredienti,difficolta,tipo_pasta ,sugo):
        super().__init__(nome,tempo_cottura,ingredienti,difficolta)
        self.tipo_pasta  = tipo_pasta 
        self.sugo = sugo
    
    
    #@property
    #def tipo_pasta (self): 
    #    if self._titolo != None:
    #        
    #        return self._titolo
    #    return False
    #@property
    #def sugo(self):
    #    return self.sugo

    def __str__(self):
        return f"{self.nome} - {self.tempo_cottura} min - Difficoltà: {self.difficolta}"

class Secondo(Ricetta):
    def __init__(self,nome,tempo_cottura,ingredienti,difficolta,tipo_carne ,cottura):
        super().__init__(nome,tempo_cottura,ingredienti,difficolta)
        self.tipo_carne  = tipo_carne 
        self.cottura = cottura
    #@property
    #def tipo_carne(self):
    #    return self.tipo_carne
    #@property
    #def cottura(self):
    #    return self.cottura
    
    def __str__(self):
        return f"{self.nome} - {self.tempo_cottura} min - Difficoltà: {self.difficolta}"

class Dolce(Ricetta):
    def __init__(self,nome,tempo_cottura,ingredienti,difficolta ,calorie,tipo_dolce):
        super().__init__(nome,tempo_cottura,ingredienti,difficolta)
        self.tipo_dolce  = tipo_dolce 
        self.calorie = calorie
    #
    #@property
    #
    #def tipo_dolce(self):
    #
    #    return self.tipo_dolce
    #
    #@property
    #
    #def calorie_Ricetta(self):
    #
    #    return self.calorie
    
    def __str__(self):
        return f"{self.nome} - {self.tempo_cottura} min - Difficoltà: {self.difficolta}"

def stampa_ricette(piatti_ordinati):
    for p in piatti_ordinati:
        print(f'{type(p).__name__}: {p} ')

def verifica_ingredienti(ricette,ingredienti):
    ricette_possibili = []
    for ricetta in ricette:
        ingredienti_ricetta = ricetta.ingredienti
        for ingrediente in ingredienti:
            if ingrediente in ingredienti_ricetta:
                ingredienti_ricetta.remove(ingrediente)
                if ingredienti_ricetta == []:
                    ricette_possibili.append(ricetta)
    return ricette_possibili
# Esempio di utilizzo
primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")

ricette = [primo, secondo, dolce]
ricette_possibili = verifica_ingredienti(ricette, ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"])
print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")

print("\nInformazioni sulle ricette:")
stampa_ricette(ricette)