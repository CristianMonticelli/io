class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []
        self.corsi = []
        self.tentativi = []
    
    def verifica_corso(self, corso):
        if corso in self.corsi:
            tentativo = TentativoQuiz(self, corso)
            self.tentativi.append(tentativo)
            for d in corso.domande:
                print(d.testo)
                print(d.opzioniPossibili)
                risposta = input("Inserisci la risposta: ")
                tentativo.rispondi(d, risposta)
        else:
            print("Non sei iscritto a questo corso")

class Corso:
    def __init__(self, titolo, domande):
        self.titolo = titolo
        self.domande = domande
        self.studenti = []

    def valuta_tentativi(self):
        for studente in self.studenti:
            valutazione = 0
            giuste = 0
            print("Studente: ", studente.nome)
            for t in studente.tentativi:
                for r in t.risposteDate:
                    if r.giusta == True:
                        giuste += 1
                valutazione = (10 / len(self.domande)) * giuste
                print("Valutazione: ", valutazione)
            
        
    
# ho cavato questa classe perchè era superfluo visto che aveva solo la lista di domande come attributo
# class Quiz:
#     def __init__(self, corso, domande):
#         self.corso = corso
#         self.domande = domande
        

class Domanda:
    def __init__(self, testo, opzioniPossibili, risposta):
        self.testo = testo
        self.opzioniPossibili = opzioniPossibili
        self.risposta = risposta

class Risposta:
    def __init__(self, domanda, risposta):
        self.domanda = domanda
        self.risposta = risposta
        self.giusta = None

class TentativoQuiz:
    def __init__(self, studente,corso):
        self.studente = studente
        self.corso = corso
        self.risposteDate = []
        self.valutazione = None

    def rispondi(self, domanda, risposta):
        risposta = Risposta(domanda, risposta)
        self.risposteDate.append(risposta)
        if risposta.risposta == domanda.risposta:
            risposta.giusta = True
        else:
            risposta.giusta = False
    
    def valuta(self,valutazione):
        self.valutazione = valutazione

studente1 = Studente("Mario")
studente2 = Studente("Luca")
studente3 = Studente("Giovanni")
domanda1 = Domanda("Quanto fa 2+2?", ["1", "2", "3", "4"], "4")
domanda2 = Domanda("Quanto fa 3+3?", ["1", "2", "3", "6"], "6")
domanda3 = Domanda("Quanto fa 4+4?", ["1", "2", "3", "8"], "8")
domanda4 = Domanda("Quanto fa 5+5?", ["1", "2", "3", "10"], "10")
domanda5 = Domanda("Quanto fa 6+6?", ["1", "2", "3", "12"], "12")



corso1 = Corso("Matematica", [domanda1, domanda2, domanda3, domanda4, domanda5])

studente1.verifica_corso(corso1)
studente2.verifica_corso(corso1)
studente3.verifica_corso(corso1)

print(studente1.tentativi[0].risposteDate[0].giusta)

corso1.studenti.append(studente1)
corso1.studenti.append(studente2)
corso1.studenti.append(studente3)
corso1.valuta_tentativi()