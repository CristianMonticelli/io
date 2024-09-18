# Esempio di utilizzo
class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome
        self.eta = eta
        self.citta = citta
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}")
    def descrizione(self):
        print(f'Ho {self.eta} anni e vivo a {self.citta}')

persona = Persona("Mario", 30, "Roma")
persona.saluta()  # Output: Ciao, mi chiamo Mario.
persona.descrizione()  # Output: Ho 30 anni e vivo a Roma.