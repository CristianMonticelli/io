#Il sistema permette di gestire il noleggio di automobili presso un'agenzia di autonoleggio. 
# L'agenzia dispone di diverse automobili, 
# e ogni automobile ha un numero di targa, un modello, una categoria 
# (economica, media, lusso) e una disponibilità (noleggiata o disponibile). 
# Il sistema deve permettere di:
#
#1)Aggiungere nuove automobili all'agenzia.
#2)Noleggiare un'auto (verificando se è disponibile).
#3)Visualizzare le automobili disponibili.
#4)Visualizzare i noleggi effettuati.
#
#Il sistema deve includere due classi principali:
#- Automobile: rappresenta una singola auto disponibile presso l'agenzia.
#- AgenziaNoleggio: gestisce le automobili e i noleggi.
#
#Crea relativo diagramma UML
from datetime import datetime, timedelta
import random
class Autonoleggio:
    def __init__(self,nome):
        self.nome = nome
        self.noleggi = []
        self.auto = []
    
    def aggiungere_automobile(self, nuova_auto):
        if nuova_auto not in self.auto:
            self.auto.append(nuova_auto)
            print(f'auto aggiunta {nuova_auto}')
        else:
            print('auto gia presente')
    
    def noleggia_auto(self, auto_scelta, data_oggi, data_fine_noleggio):
        if auto_scelta in self.auto:
            if auto_scelta.disponibilità == True:
                self.noleggi.append(Noleggio(self.nome,auto_scelta, data_oggi, data_fine_noleggio))
                print(f'auto noleggiata {auto_scelta}')
            else:
                print('auto gia noleggiata')
        else:
            print('auto inesistaente')
    
    def automobili_disponibili(self):
        for auto in self.auto:
            if auto.disponibilità == True:
                print(auto)
    
    def noleggi_effettuati(self):
        for noleggio in self.noleggi:
            print(noleggio.automobile)
    
    def noleggio_finito(self, auto_scelta):
        if auto_scelta in self.auto:
            auto_scelta.auto_restituita()
        else:
            print('auto inesistente')



class Auto:
    def __init__(self, numero_targa, modello, categoria):
        self.numero_targa = numero_targa
        self.modello = modello
        self.categoria = categoria
        self.disponibilità = True
        
    def auto_noleggiata(self):
        self.disponibilità = False
    
    def auto_restituita(self):
        self.disponibilità = True
    
    def __str__(self):
        return f'{self.numero_targa} {self.modello} {self.categoria} '

class Noleggio:
    def __init__(self, autonoleggio, automobile, inizio, fine_noleggio):
        self.autonoleggio = autonoleggio
        self.automobile = automobile
        self.inizio = inizio
        self.fine_noleggio = fine_noleggio
        automobile.auto_noleggiata()
        #print(automobile)
    
    def __str__(self):
        return f'{self.autonoleggio} {self.automobile} {self.inizio} {self.fine_noleggio}'
    

#1)Aggiungere nuove automobili all'agenzia.
autonoleggio = Autonoleggio('Da Roberto')
auto1 = Auto("cd123sp", 'lancia Y', "economica")
autonoleggio.aggiungere_automobile(auto1)
autonoleggio.aggiungere_automobile(auto1)

#2)Noleggiare un'auto (verificando se è disponibile).
data_corrente = datetime.now()

# Somma di un giorno
data_futura = data_corrente + timedelta(days=random.randint(1, 100))

# Formattazione delle date
data_corrente_str = data_corrente.strftime('%Y-%m-%d %H:%M')
data_futura_str = data_futura.strftime('%Y-%m-%d %H:%M')

# Utilizzo delle date nel metodo noleggia_auto
autonoleggio.noleggia_auto(auto1, data_corrente_str, data_futura_str)

autonoleggio.noleggio_finito(auto1)
#3)Visualizzare le automobili disponibili.
auto2 = Auto("df386cj", 'toyota yaris', "lusso")
autonoleggio.aggiungere_automobile(auto2)
autonoleggio.automobili_disponibili()

#4)Visualizzare i noleggi effettuati.
autonoleggio.noleggi_effettuati()