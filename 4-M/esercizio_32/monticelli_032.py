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
        self.canale = None
    
    def crea_canale(self, nome):
        if self.canale is not None:
            return False
        self.canale = Canale(nome, self)
        return True
    
    def carica_video(self, video):
        if self.canale is None:
            return False
        self.canale.video.append(video)
        return True
    
    def follow_canale(self, canale):
        canale.iscritti.append(self)
        
     
    def guarda_video(self, video):
        self.cronologia.append(video)
    
    def commenta_video(self, video, testo):
        commento = Commento(self, testo, video)
        self.commenti.append(commento)
        video.aggiungi_commento(commento)
    
    def crea_playlist(self, nome):
        if nome in self.playlist:
            return False
        playlist = Playlist(nome, self)
        self.playlist.append(playlist)
        return True
    
    def rimuovi_playlist(self, nome):
        for p in self.playlist:
            if nome == p.nome:
                self.playlist.remove(p)
                return True
        return False
    
    def aggiungi_video_playlist(self, video, playlist):
        for p in self.playlist:
            if playlist == p.nome:
                print("Playlist trovata")
                p.aggiungi_video(video)
                return True
        return False
    
    def rimuovi_video_playlist(self, video, playlist):
        for p in self.playlist:
            if playlist == p.nome:
                print("Playlist trovata")
                p.rimuovi_video(video)
                return True
        return False
    
    def fai_abbonamento(self, tipo, prezzo, durata, data_inizio, data_fine):
        abbonamento = Abbonamento(tipo, prezzo, durata, data_inizio, data_fine)
        self.abbonamento.append(abbonamento)
        print(f"Abbonamento {tipo} attivato")
        return True
       
        
        

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
        print(f"Commento aggiunto al video {commento.testo}")

class Playlist:
    def __init__(self, nome, creatore):
        self.nome = nome
        self.creatore = creatore
        self.video = []
        print(f"Playlist {nome} creata da {creatore.nome}")
    
    def aggiungi_video(self, video):
        self.video.append(video)
        print(f"Video {video.titolo} aggiunto alla playlist {self.nome}")
    
    def rimuovi_video(self, video):
        if video in self.video:
            self.video.remove(video)
            print(f"Video {video.titolo} rimosso dalla playlist {self.nome}")
            return True
        return False
    
    

class Abbonamento:
    def __init__(self, tipo, prezzo, durata, data_inizio, data_fine):
        self.tipo = tipo
        self.prezzo = prezzo
        self.durata = durata
        self.data_inizio = data_inizio
        self.data_fine = data_fine

class Commento:
    def __init__(self, autore: Utente, testo: str, video: Video):
        self.autore = autore
        self.testo = testo
        self.dataPubblicazione = datetime.datetime.now()
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

utente1.crea_playlist("Playlist1")

utente1.aggiungi_video_playlist(video1, "Playlist1")
utente1.aggiungi_video_playlist(video2, "Playlist1")

utente1.rimuovi_video_playlist(video1, "Playlist1")

utente1.fai_abbonamento("Premium", 9.99, 30, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=30))

utente1.crea_canale("Canale1")

utente1.carica_video(video1)

utente2.follow_canale(utente1.canale)