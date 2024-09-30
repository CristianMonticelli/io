class Veicolo:
    numero_veicoli = 0
    def __init__(self, tipo, marca):
        Veicolo.numero_veicoli += 1
        self.marca = marca
        self.tipo = tipo
    @classmethod
    def get_numero_veicoli(cls):
        #return Veicolo.numero_veicoli
        return cls.numero_veicoli

# Esempio di utilizzo
print(Veicolo.get_numero_veicoli())  # Output: 0
auto1 = Veicolo("Auto", "Toyota")
auto2 = Veicolo("Moto", "Honda")
print(Veicolo.get_numero_veicoli())  # Output: 2