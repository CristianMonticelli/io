class Casa:
    def __init__(self,indirizzo,proprietario):
        self._indirizzo = indirizzo
        self._proprietario = proprietario
        self.stanze = []

    @property
    def indirizzo(self):
        return self._indirizzo
    @property
    def proprietario(self):
        return self._proprietario
    @indirizzo.setter
    def indirizzo(self,new_indirizzo):
        self._indirizzo= new_indirizzo
    @proprietario.setter
    def proprietario(self,new_proprietario):
        self._proprietario= new_proprietario

    def stampa_stanze(self):
        for stanza in self.stanze:
            print(f'{stanza.nome} ({stanza.superficie} mq)')
        

    def aggiungi_stanza(self,stanza):
        
        self.stanze.append(stanza)
        stanza.associa_casa(self)

class Stanza:
    def __init__(self,nome,superficie):
        self._nome=nome
        self._superficie = superficie
        self.casa = None
    def associa_casa(self,casa):
        self.casa = casa

    @property
    def nome(self):
        return self._nome
    @property
    def superficie(self):
        return self._superficie
    @nome.setter
    def nome(self,new_nome):
        self._nome= new_nome
    @superficie.setter
    def superficie(self,new_superficie):
        self._superficie= new_superficie


# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

# Verifica dell'associazione
print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
    print(f"- {stanza.nome} ({stanza.superficie} mq)")