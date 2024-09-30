class Dipendenti:
    def __init__(self, nome, stipendio):
        self.nome = nome
        self.stipendio = stipendio

    def get_nome(self):
        return self.nome
    
    def get_stipendio(self):
        return self.stipendio


class Manager(Dipendenti):
    def __init__(self, nome, stipendio,team):
        super().__init__(nome, stipendio)
        self.team = team
    
    def get_numero_di_team(self):
        return self.team
    
class Sviluppatore(Dipendenti):
    def __init__(self, nome, stipendio, linguaggio):
        super().__init__(nome, stipendio)
        self.linguaggio = linguaggio
    
    def get_linguaggio_di_programmazione(self):
        return self.linguaggio
    

# Esempio di utilizzo
manager = Manager("Alice", 50000, 3)
print(manager.get_nome())  # Output: Alice
print(manager.get_stipendio())  # Output: 50000
print(manager.get_numero_di_team())  # Output: 3

sviluppatore = Sviluppatore("Bob", 40000, "Python")
print(sviluppatore.get_nome())  # Output: Bob
print(sviluppatore.get_stipendio())  # Output: 40000
print(sviluppatore.get_linguaggio_di_programmazione())  # Output: Python