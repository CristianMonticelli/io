
class Studente:
    def __init__(self,nome,matricola):
        self._nome=nome
        self._matricola = matricola
        self.corsi = []

    def aggiungi_corso(self,corso):
        
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.aggiungi_studente(self)

    @property
    def nome(self):
        return self._nome
    @property
    def matricola(self):
        return self._matricola
    @nome.setter
    def nome(self,new_nome):
        self._nome= new_nome
    @matricola.setter
    def matricola(self,new_matricola):
        self._matricola= new_matricola

class Corso:
    def __init__(self,titolo,codice):
        self._titolo = titolo
        self._codice = codice
        self.studenti = []

    @property
    def titolo(self):
        return self._titolo
    @property
    def codice(self):
        return self._codice
    @titolo.setter
    def titolo(self,new_titolo):
        self._titolo= new_titolo
    @codice.setter
    def codice(self,new_codice):
        self._codice= new_codice

    def aggiungi_studente(self,studente):
        
        
        if studente not in self.studenti:
            self.studenti.append(studente)
            studente.aggiungi_corso(self)

# Creazione delle istanze di Studente
studente1 = Studente("Alice Rossi", "MAT123")
studente2 = Studente("Marco Bianchi", "MAT456")

# Creazione delle istanze di Corso
corso1 = Corso("Programmazione Python", "PY101")
corso2 = Corso("Database Relazionali", "DB201")
corso3 = Corso("Sistemi Operativi", "SO301")

# Associazione tra studenti e corsi
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso3)

# Verifica delle associazioni
print(f"{studente1.nome} è iscritto ai seguenti corsi:")
for corso in studente1.corsi:
    print(f"- {corso.titolo} ({corso.codice})")

print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
for studente in corso2.studenti:
    print(f"- {studente.nome} ({studente.matricola})")