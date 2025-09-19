#Un'azienda di gestione ecologica ha creato un parco naturale che ospita diversi ecosistemi, tra cui foreste, zone umide e praterie. 
#Ogni ecosistema ha caratteristiche e esigenze ambientali differenti. Il parco è dotato di una rete di sensori che monitorano le condizioni ambientali e 
#di dispositivi che possono essere attivati o disattivati per ottimizzare la gestione e preservare l'equilibrio ecologico.

#Il sistema deve essere in grado di monitorare costantemente i parametri ambientali e gestire i dispositivi di controllo, 
#come irrigatori per mantenere il livello di umidità, ventilatori per migliorare la qualità dell'aria e luci per illuminare aree specifiche nelle ore notturne
#Ogni area del parco deve essere monitorata separatamente. Ogni area ha caratteristiche ambientali specifiche (temperatura, umidità, qualità dell'aria) 
#e dispositivi dedicati per gestirle.

#Il sistema deve monitorare i parametri ambientali in tempo reale per ogni zona e regolare automaticamente l'ambiente, se necessario, per mantenere le condizioni ottimali.
#I dispositivi di controllo (irrigatori, ventilatori, luci) devono essere gestiti in base ai dati rilevati dai sensori.
#Ogni zona può avere una serie di dispositivi attivi o disattivi, e il sistema deve permettere di monitorare e modificare lo stato di ciascun dispositivo.
#Il sistema deve monitorare i parametri ambientali per ciascuna zona (temperatura, umidità, qualità dell'aria).
#Il sistema deve attivare o disattivare i dispositivi per ogni zona in base alle necessità: Se la temperatura supera i 30°C, attivare i ventilatori.
#Se l'umidità scende sotto il 60%, attivare gli irrigatori.

#Se la qualità dell'aria scende sotto il 40%, attivare i ventilatori.
#Implementare una funzione che restituisca un dizionario con i parametri di ogni zona, e una che permetta di attivare o disattivare i dispositivi di ciascuna zona.
class ParcoNaturale:
    def __init__(self,nome):
        self.nome = nome
        self.ecosistemi = []
    
    def aggiungi_ecosistema(self,ecosistema):
        if ecosistema not in self.ecosistemi:
            self.ecosistemi.append(ecosistema)
            print('aggiunto')
     

class Ecosistema:
    def __init__(self,tipo,temperatura,umidità,qualità_aria):
        self.tipo = tipo
        self.temperatura = temperatura
        self.sensore_temperatura = []
        self.umidità = umidità
        self.sensore_umidità = []
        self.qualità_aria = qualità_aria
        self.sensore_qualità_aria = []

    def aggiungi_sensore(self,sensore):
        if type(sensore) == SensoreTemperatura:
            self.sensore_temperatura.append(sensore)
            sensore.assegna_ecosistema(self)
            print('aggiunto')

        if type(sensore) == SensoreUmidità:
            self.sensore_umidità.append(sensore)
            sensore.assegna_ecosistema(self)
            print('aggiunto')
        
        if type(sensore) == SensoreQualitàAria:
            self.sensore_qualità_aria.append(sensore)
            sensore.assegna_ecosistema(self)
            print('aggiunto')

        



class SensoreTemperatura:
    def __init__(self):
        self.ecosistema = None
        self.ventilatori = []
    def assegna_ecosistema(self,ecosistema):
        if ecosistema != self.ecosistema:
            self.ecosistema = ecosistema
    def monitora(self,valore):
        if self.ecosistema.temperatura < valore:
            for v in self.ventilatori:
                v.acceso = True
        else: 
            for v in self.ventilatori:
                v.spento = False
    def aggiungi_dispositivo(self,dispositivo):
        if dispositivo == 'ventilatore':
            self.ventilatori.append(dispositivo)

class SensoreUmidità:
    def __init__(self):
        self.ecosistema = None
        self.irrigatori = []
    def assegna_ecosistema(self,ecosistema):
        if ecosistema != self.ecosistema:
            self.ecosistema = ecosistema
    def monitora(self,valore):
  
        if self.ecosistema.umidità > valore:
            for i in self.irrigatori:
        
                i.acceso = True
        else: 
            for i in self.irrigatori:
                i.spento = False
    def aggiungi_dispositivo(self,dispositivo):
        if dispositivo.tipo == 'irrigatore':
            
            self.irrigatori.append(dispositivo)

class SensoreQualitàAria:
    def __init__(self):
        self.ecosistema = None
        self.ventilatori = []
    def assegna_ecosistema(self,ecosistema):
        if ecosistema != self.ecosistema:
            self.ecosistema = ecosistema
    def monitora(self,valore):
        if self.ecosistema.qualità_aria > valore:
            for v in self.ventilatori:
                v.acceso = True
        else: 
            for v in self.ventilatori:
                v.spento = False
    def aggiungi_dispositivo(self,dispositivo):
        if dispositivo == 'ventilatore':
            self.ventilatori.append(dispositivo)

class Dispositivo:
    def __init__(self,tipo):
        self.tipo = tipo
        self.acceso = False
    def acceso():
        self.acceso = True
        print('acceso')
    def spento():
        self.acceso = False
        print('spento')

parco = ParcoNaturale('Bernabiniland')

ecosistema1 = Ecosistema('foresta',40,60,90)

parco.aggiungi_ecosistema(ecosistema1)

sensoreumidita = SensoreUmidità()

ecosistema1.aggiungi_sensore(sensoreumidita)

irrigatore = Dispositivo('irrigatore')

sensoreumidita.aggiungi_dispositivo(irrigatore)
sensoreumidita.monitora(10)