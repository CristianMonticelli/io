class Auto:
    def __init__(self,marca,modello ):
        self._marca  = marca 
        self._modello = modello
    @property
    def marca(self):
        return self._marca
    @property
    def modello(self):
        return self._modello
    @marca.setter
    def marca(self,new_marca):
        self._marca = new_marca
    @modello.setter
    def modello(self,new_modello):
        self._modello = new_modello
    
class Motore:
    def __init__(self,numero_seriale ,tipo ):
        self._numero_seriale  = numero_seriale 
        self._tipo = tipo       
    @property
    def numero_seriale(self):
        return self._numero_seriale
    @property
    def tipo(self):
        return self._tipo
    @numero_seriale.setter
    def numero_seriale(self,new_numero_seriale):
        self._numero_seriale= new_numero_seriale
    @tipo.setter
    def tipo(self,new_tipo):
        self._tipo= new_tipo

# Creazione delle istanze
auto1 = Auto("Fiat", "500")
motore1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
auto1.associa_motore(motore1)

# Verifica dell'associazione
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")