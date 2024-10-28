# Esempio di utilizzo
class ContoBancario:
    def __init__(self, numero_conto, intestatario, saldo):
        self.numero_conto = numero_conto
        self.intestatario = intestatario
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo  
    def deposita(self, euro):
        if euro>0:
            self.__saldo = self.__saldo+euro

    def preleva(self, euro):
        if euro<=self.__saldo:
            self.__saldo = self.__saldo-euro

# Esempio di utilizzo
conto = ContoBancario("123456789", "Mario Rossi", 1000.0)
print(conto.get_saldo())  # Output: 1000.0
conto.deposita(500.0)
print(conto.get_saldo())  # Output: 1500.0
conto.preleva(200.0)
print(conto.get_saldo())  # Output: 1300.0