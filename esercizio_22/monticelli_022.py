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
class Autonoleggio:
    def __init__(self,nome):
        self.nome = nome
        self.noleggi = []
        self.auto = []
    
    def aggiungere_automobile(self, nuova_auto):
        if nuova_auto not in self.auto:
            self.auto.append(nuova_auto)
            print(self.auto)
        else:
            print('auto gia presente')
    
    def noleggia_auto(self, auto_scelta, data_oggi, data_fine_noleggio):
        if auto_scelta in self.auto:
            if auto_scelta.disponibilità == True:
                self.noleggi.append(Noleggio(self.nome,auto_scelta, data_oggi, data_fine_noleggio))
            else:
                print('auto gia noleggiata')
        else:
            print('auto inesistaente')



class Auto:
    def __init__(self, numero_targa, modello, categoria):
        self.numero_targa = numero_targa
        self.modello = modello
        self.categoria = categoria
        self.disponibilità = True
        
    def auto_noleggiata(self):
        self.disponibilità = False

class Noleggio:
    def __init__(self, autonoleggio, automobile, inizio, fine_noleggio):
        self.autonoleggio = autonoleggio
        self.automobile = automobile
        self.inizio = inizio
        self.fine_noleggio = fine_noleggio
        automobile.auto_noleggiata()
        print(automobile)
    
    
autonoleggio = Autonoleggio('Da Roberto')
auto1 = Auto("cd123sp", 'lancia Y', "economica")
autonoleggio.aggiungere_automobile(auto1)
autonoleggio.aggiungere_automobile(auto1)

autonoleggio.noleggia_auto(auto1)