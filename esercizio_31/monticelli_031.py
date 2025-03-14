class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []
        self.corso = []
        self.tentetivo = []
    
    def risolvi_quiz(self, quiz):
        tentativo = TentativoQuiz(self, quiz)
        self.tentetivo.append(tentativo)
        for d in quiz.domande:
            print(quiz.d)
        #tentativo.rispondi()

class Corso:
    def __init__(self, titolo, quiz):
        self.titolo = titolo
        self.quiz = quiz
        self.studenti = []
    def valuta_tentativi(self):
        pass
    

class Quiz:
    def __init__(self, corso, domande):
        self.corso = corso
        self.domande = domande
        

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
    def __init__(self, studente, quiz):
        self.studente = studente
        self.quiz = quiz
        self.risposteDate = []
        self.valutazione = None

    def rispondi(self, domanda, risposta):
        risposta = Risposta(self.studente, domanda, risposta)
        self.risposte.append(risposta)
        if risposta.risposta == domanda.risposta:
            risposta.giusta = True
        else:
            risposta.giusta = False
    
    def valuta(self,valutazione):
        self.valutazione = valutazione

studente1 = Studente("Mario")
domanda1 = Domanda("Quanto fa 2+2?", ["1", "2", "3", "4"], "4")
domanda2 = Domanda("Quanto fa 3+3?", ["1", "2", "3", "6"], "6")
quiz1 = Quiz("Matematica", [domanda1, domanda2])
corso1 = Corso("Matematica", quiz1)

studente1.risolvi_quiz(quiz1)



        