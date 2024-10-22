class Calcolatrice:
    @staticmethod
    def addizione(valore_1, valore_2):
        addizione = valore_1 + valore_2
        return addizione
    @staticmethod
    def sottrazione(valore_1, valore_2):
        sottrazione = valore_1 - valore_2
        return sottrazione
    @staticmethod
    def moltiplicazione(valore_1, valore_2):
        moltiplicazione = valore_1 * valore_2
        return moltiplicazione
    @staticmethod
    def divisione(valore_1, valore_2):
        divisione = valore_1 / valore_2
        return divisione

# Esempio di utilizzo
print(Calcolatrice.addizione(10, 5))       # Output: 15
print(Calcolatrice.sottrazione(10, 5))     # Output: 5
print(Calcolatrice.moltiplicazione(10, 5)) # Output: 50
print(Calcolatrice.divisione(10, 5))       # Output: 2.0