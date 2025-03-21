# Piattaforma di Streaming Video
# Immagina una piattaforma dove gli 'utenti' possono 'guardare video, creare playlist e seguire i loro canali preferiti'.

# Ogni utente ha un suo profilo con nome, email e password, e può creare diverse playlist per organizzare i video che preferisce. L'utente ha anche un abbonamento che gli permette di accedere a contenuti esclusivi.

# I video sono il cuore della piattaforma: hanno un titolo, una descrizione, un URL per lo streaming e una durata. Sotto ogni video, gli utenti possono lasciare commenti.

# Le playlist sono raccolte di video create dagli utenti. Ogni playlist ha un nome e un creatore, e contiene una lista di video.

# Ogni abbonamento ha un tipo, un prezzo e una data di inizio e fine.

# I commenti sono messaggi lasciati dagli utenti sotto i video dopo averlo guardato. Ogni commento ha un autore, un testo, una data di pubblicazione ed è associato a uno specifico video.

# In sintesi, la piattaforma gestisce utenti, video, playlist, abbonamenti e commenti, permettendo agli utenti di interagire tra loro e con i contenuti.
import datetime
class Utente:
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password
        self.playlist = []
        self.abbonamento = []
        self.cronologia = []
        self.commenti = []
     
    def guarda_video(self, video):
        self.cronologia.append(video)
    
    def commenta_video(self, video, testo):
        commento = Commento(self, testo, video)
        self.commenti.append(commento)
        video.aggiungi_commento(commento)

class Video:
    def __init__(self, titolo, descrizione, url, durata, canale):
        self.titolo = titolo
        self.descrizione = descrizione
        self.url = url
        self.durata = durata
        self.canali = canale
        self.commenti = []
    
    def aggiungi_commento(self, commento):
        self.commenti.append(commento)
        #print(f"Commento aggiunto al video {commento.testo}")

class Playlist:
    def __init__(self, nome, creatore):
        self.nome = nome
        self.creatore = creatore
        self.video = []

class Abbonamento:
    def __init__(self, tipo, prezzo, data_inizio, data_fine):
        self.tipo = tipo
        self.prezzo = prezzo
        self.data_inizio = data_inizio
        self.data_fine = data_fine

class Commento:
    def __init__(self, autore, testo, video):
        self.autore = autore
        self.testo = testo
        self.dataPubblicazione = datetime.now()
        self.video = video

class Piattaforma:
    def __init__(self, nome):
        self.nome = nome
        self.utenti = []
        self.video = []
        self.playlist = []
        self.abbonamenti = []
        self.commenti = []
        self.canali = []

class Canale:
    def __init__(self, nome, proprietario):
        self.nome = nome
        self.proprietario = proprietario
        self.video = []
        self.iscritti = []

# Creazione di una piattaforma
piattaforma = Piattaforma("Solo divertimento")

# Creazione di utenti
utente1 = Utente("Lorenzo", "lorenzo.spizzo@gmail.com", "password123")
utente2 = Utente("Alessandro", "alessandro.sancho@isis.com", "password456")

# Creazione di video
video1 = Video("Video divertente", "Un video molto divertente", "https://www.youtube.com/watch?v=123456", 120, "Canale1")
video2 = Video("Video interessante", "Un video molto interessante", "https://www.youtube.com/watch?v=789012", 180, "Canale2")

utente1.guarda_video(video1)

utente1.commenta_video(video1, "Bellissimo video!")
