class Pagamento:
    def __init__(self):
        pass
    def processa_pagamento():
        return f'Elaborazione pagamento generico'

class CartaDiCredito(Pagamento):
    def __init__(self,nome, conto, data, matricola):
        #super().__init__('CartaDiCredito', nome)
        self.nome = nome
        self.conto = conto
        self.data = data
        self.matricola = matricola
    def processa_pagamento(self):
        return f'Elaborazione pagamento con Carta di Credito per {self.nome}'

    

class PayPal(Pagamento):
    def __init__(self,email, password):
        #super().__init__('PayPal', email)
        self.email = email
        self.password = password
    def processa_pagamento(self):
        return f'Elaborazione pagamento con pay pal per {self.email }'

# Esempio di utilizzo
def effettua_pagamento(metodo_di_pagamento: Pagamento):
    print(metodo_di_pagamento.processa_pagamento())

pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  # Output: Elaborazione pagamento con Carta di Credito per Mario Rossi
effettua_pagamento(pagamento_paypal)  # Output: Elaborazione pagamento con PayPal per mario.rossi@example.com
