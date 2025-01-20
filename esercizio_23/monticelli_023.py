#Un social network di fotografia (instagram). 
# Gli utenti possono registrarsi, creare un profilo, caricare foto, seguire altri utenti. 
# Ogni foto ha un titolo, una descrizione. Gli utenti possono creare album per organizzare le loro foto.
#Classi Principali:
#Utente: nome utente, email, password, profilo (immagine, biografia)
#Foto: ID, titolo, descrizione, data caricamento, utente (chi l'ha caricata), album (a quale album appartiene)
#Album: titolo, descrizione, utente (chi l'ha creato), foto (lista di foto)
#Relazioni:
#Un utente può caricare molte foto (relazione uno-a-molti).
#Una foto può avere molti commenti (relazione uno-a-molti).
#Un commento appartiene a un utente e a una foto (relazione molti-a-molti).
#Una foto appartiene a un album (relazione uno-a-molti).
#Un album appartiene a un utente (relazione uno-a-molti).
from datetime import datetime
class Utente:
    def __init__(self,nome_utente, email, password, profilo): 
        self.nome_utente = nome_utente
        self.email = email
        self.password = password
        self.profilo = profilo
        self.foto = []
        self.album = []
        self.seguiti = []
    
    def caricare_foto(self,foto):
        if foto not in self.foto:
            self.foto.append(foto)
            foto.postata(datetime.now().strftime('%Y-%m-%d %H:%M'),self.nome_utente)
            #print(self.foto)
    
    def segui_utenti(self,utente):
        if utente not in self.seguiti:
            self.seguiti.append(utente)
            #print(self.seguiti)
    
    def crea_album(self,album):
        if album not in self.album:
            self.album.append(album)
            album.utente = self
    
    def inserisci_foto_in_album(self,album,foto):
        if album in self.album:
            if foto not in album.foto:
                album.aggiungi_foto(foto)
            


class Foto:
    def __init__(self,ID,titolo,descrizione):
        self.ID = ID
        self.titolo = titolo
        self.descrizione = descrizione
        self.data_caricamento = None
        self.utente = None
        self.album = None
        self.commenti = []
    def postata(self,data_caricamento,utente):
        self.data_caricamento =data_caricamento
        self.utente = utente
        
        
    
class Album:
    def __init__(self,titolo,descrizione):
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = None
        self.foto = []

    def aggiungi_foto(self,foto):
        self.foto.append(foto)
        
        

class Commento:
    def __init__(self,testo,autore):
        self.testo = testo
        self.autore = autore
        self.foto = None
    def assegna_commento(self,foto):
        self.foto = foto
        foto.commenti.append(self)

utente1 = Utente('Alessio', 'alessiosancio99@gmail.com','!@#$','Roblox pro player')
foto1 = Foto(6653,'forza taverna','il taverba grande squadra inbattibile')
foto2 = Foto(5653,'ciao','post')
foto3 = Foto(7653,'scrivania','molto resistente')

album1 = Album('raccolta','trenini')
utente2 = Utente('Nick', 'nickoloemilia94@gmail.com','!#@#$','I play every day clash royal')

utente1.caricare_foto(foto1)
utente1.segui_utenti(utente2)

utente1.crea_album(album1)

utente1.inserisci_foto_in_album(album1,foto2)

commento1 = Commento('meglio un tavolo', utente2)
commento1.assegna_commento(foto3)
        