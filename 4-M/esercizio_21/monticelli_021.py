#Descrizione dell'esercizio
#Il sistema permette di gestire le prenotazioni in un albergo. 
#L'albergo ha diverse camere, e ogni camera ha un numero, un tipo 
# (singola, doppia, suite) e una disponibilità (occupata o libera). 
# Il sistema deve permettere di:

#- Aggiungere nuove camere all'albergo.
#- Prenotare una camera (verificando se è disponibile).
#- Visualizzare le camere disponibili.
#- Visualizzare le prenotazioni effettuate.
#
#Il sistema deve includere due classi principali:
#1. Camera: rappresenta una singola camera dell'albergo.
#2. Albergo: rappresenta l'albergo che gestisce le camere e le prenotazioni.
#
#Crea relativo diagramma UML

#1. Camera: rappresenta una singola camera dell'albergo.
class Camera:
    def __init__(self,numero,tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponibilità = True
        self.albergo = None

    def collega_albergo(self,albergo):
        if self.albergo == None:
            self.albergo = albergo
            #print(albergo.nome)
            print(self.numero)
        else:
            print('albergo gia assegnato')
    
    def prenota_camera(self):
        self.disponibilità = False

    def libera_camera(self):
        self.disponibilità = True
    
    def __str__(self):
        return f'camera:{self.numero} tipo:{self.tipo} disponibilita:{self.disponibilità}'
    


#2. Albergo: rappresenta l'albergo che gestisce le camere e le prenotazioni.
class Albergo:
    def __init__(self,nome):
        self.nome = nome
        self.camere = []
    
    #- Aggiungere nuove camere all'albergo.
    def aggiungi_camera(self,nuova_camera):
        if nuova_camera not in self.camere:
            self.camere.append(nuova_camera)
            nuova_camera.collega_albergo(self)
            #print(self.camere[0].numero)
        else:
            print(f'{nuova_camera} gia esistente')
    
    #- Prenotare una camera (verificando se è disponibile).
    def prenotare_camera(self,camera_desiderata):
        for c in self.camere:
            if camera_desiderata not in self.camere:
                print(f'{camera_desiderata} non esiste')
                pass
            if c == camera_desiderata:
                if camera_desiderata.disponibilità == True:
                    print(f'camera {camera_desiderata.numero} prenotata')
                    camera_desiderata.prenota_camera()
                elif camera_desiderata.disponibilità == False:
                    print(f'camera {camera_desiderata.numero} occupata')
        
            
#
    def libera_camera(self,camera_da_liberare):
        for c in self.camere:
            if camera_da_liberare not in self.camere:
                print(f'{camera_da_liberare} non esiste')
                pass
            if c == camera_da_liberare:
                
                if camera_da_liberare.disponibilità == False:
                    print(f'camera {camera_da_liberare.numero} liberata')
                    camera_da_liberare.libera_camera()
                elif camera_da_liberare.disponibilità == True:
                    print(f'camera {camera_da_liberare.numero} gia libera')
            

    #- Visualizzare le camere disponibili.
    def visualizzare_camere_disponibili(self):
        camere_disponibili = []
        for c in self.camere:
            if c.disponibilità == True:
                camere_disponibili.append(c)
        return camere_disponibili
    
    #- Visualizzare le prenotazioni effettuate.
    def visualizzare_prenotazioni_effettuate(self):
        camere_prenotate = []
        for c in self.camere:
            if c.disponibilità == False:
                camere_prenotate.append(c)
        return camere_prenotate



albergo = Albergo('Monsce')        
camera1 = Camera(1,'singola')
camera2 = Camera(2,'singola')
camera3 = Camera(3,'doppia')
camera4 = Camera(4,'singola')
camera5 = Camera(5,'suit')
#- Aggiungere nuove camere all'albergo.
print('Aggiungere--------------------------------------')
albergo.aggiungi_camera(camera1)
albergo.aggiungi_camera(camera1)
#- Prenotare una camera (verificando se è disponibile).
print('Prenotare--------------------------------------')
albergo.prenotare_camera(camera1)
albergo.prenotare_camera(camera1)
albergo.prenotare_camera(camera2)
print('libera--------------------------------------')
albergo.aggiungi_camera(camera3)
albergo.prenotare_camera(camera3)
albergo.libera_camera(camera3)

#- Visualizzare le camere disponibili.
print(' Visualizzare le camere disponibili--------------------------------------')
albergo.aggiungi_camera(camera4)
albergo.aggiungi_camera(camera5)

albergo.prenotare_camera(camera4)

camere_disponibili = albergo.visualizzare_camere_disponibili()
for c in camere_disponibili:
    print(c)

print('Visualizzare le prenotazioni effettuate--------------------------------------')

camere_prenotate = albergo.visualizzare_prenotazioni_effettuate()
for c in camere_prenotate:
    print(c)