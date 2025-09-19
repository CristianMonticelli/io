import math

class Frazione:
    def __init__ (self,numeratore:int,denominatore:int):

        self.numeratore = numeratore
        self.denominatore = denominatore
    
    def __add__(self, altro:int) -> int:
        return Frazione(self.numeratore + altro.numeratore, self.denominatore)

    def __sub__ (self, altro:int) -> int:
        return Frazione(self.numeratore - altro.numeratore, self.denominatore)
    
    def __mul__ (self, altro:int) -> int:
        return Frazione(self.numeratore * altro.numeratore, self.denominatore * altro.denominatore)

    def __str__ (self) -> str:
        return f'Punto di coordinate ({self.numeratore}, {self.denominatore})'

# Esempio di utilizzo
f1 = Frazione(3, 4)
f2 = Frazione(2, 4)

# Addizione
f3 = f1 + f2
print(f3)  # Output: Frazione(5, 4)

# Sottrazione
f4 = f1 - f2
print(f4)  # Output: Frazione(1, 4)

# Moltiplicazione
f5 = f1 * f2
print(f5)  # Output: Frazione(6, 16)

# Rappresentazione
print(f1)  # Output: Frazione(3, 4)