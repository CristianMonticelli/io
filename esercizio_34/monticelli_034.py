import datetime
class Utente:
    def __init__(self, id_utente, nome_utente, email):
        self.id = id_utente
        self.nome = nome_utente
        self.email = email
        
        self.progetti = []
    
    def crea_progetto(self, titolo: str, genere: str):
        id = 0
        if self.progetti == []:
            pass
        else:
            for i in self.progetti:
                if id == i.id:
                    id+=1
                else: 
                    break
        progetto = ProgettoMusicale(id, titolo, datetime.datetime.now, genere)
        self.progetti.append(progetto)
        print(self.progetti)
        
    
    def conta_progetti_totali(self):
        print(len(self.progetti))
        #return len(self.progetti)
    
    def strumento_piu_usato(self):
        progetti_per_genere = self.progetti_per_genere()
        strumento_piu_usato = None
        for p in progetti_per_genere:
            if strumento_piu_usato == None:
                strumento_piu_usato= progetti_per_genere[p]
            
            if len(strumento_piu_usato) < len(progetti_per_genere[p]):
                strumento_piu_usato = progetti_per_genere[p]
            
    def progetti_per_genere(self):
        progetti_per_genere = {}
        for p in self.progetti:
            if p.genere_musicale in progetti_per_genere:
                progetti_per_genere[p.genere_musicale].append(p)
            else:
                progetti_per_genere[p.genere_musicale] = [p]
        print(progetti_per_genere)
        #return progetti_per_genere
    
class ProgettoMusicale:
    def __init__(self, id_progetto, titolo_progetto, data_creazione, genere_musicale):
        self.id = id_progetto
        self.titolo = titolo_progetto
        self.data_creazione = data_creazione
        self.genere_musicale = genere_musicale
        
        self.tracce = []
    
    def aggiungi_traccia(self, nome_traccia, durata_secondi, volume_db):
        id = 0
        if self.tracce == []:
            pass
        else:
            for i in self.tracce:
                if id == i.id:
                    id+=1
                else: 
                    break
        traccia = TracciaAudio(id, nome_traccia, durata_secondi, volume_db )
        self.tracce.append(traccia)
        print(self.tracce)

class TracciaAudio:
    def __init__(self, id_traccia, nome_traccia, durata_secondi, volume_db):
        self.id = id_traccia
        self.nome = nome_traccia
        self.durata_secondi = durata_secondi
        self.volume_db = volume_db
        
        self.sequenza_note_manuali = None
        self.strumento_utilizzato = None
        self.effetti_applicati = []
        
    def aggiungi_strumento(self,strumento):
        if self.strumento_utilizzato == None:
            self.strumento_utilizzato == strumento
        
    def applica_effetto(self, effetto):
        if effetto not in self.effetti_applicati:
            self.effetti_applicati.append(effetto)
    
    def rimuovi_effetto(self, effetto):
        if effetto in self.effetti_applicati:
            self.effetti_applicati.remove(effetto)
    
    def imposta_sequenza_note(self, note):
        if self.sequenza_note_manuali == None:
            self.sequenza_note_manuali == note
            
    def modifica_volume(self, nuovo_volume_db):
            self.volume_db == nuovo_volume_db
    
class StrumentoVirtuale:
    def __init__(self, id_strumento, nome_strumento, tipo_strumento_virtuale):
        self.id = id_strumento
        self.nome = nome_strumento
        self.tipo_strumento_virtuale = tipo_strumento_virtuale
    
    def suona_nota(self, nota, durata):
        while durata>0:
            durata-=1
            print(nota)
            
class EffettoAudio:
    def __init__(self,id_effetto,nome_effetto,tipo_effetto_audio):
        self.id_effetto = id_effetto
        self.nome_effetto = nome_effetto
        self.tipo_effetto_audio =  tipo_effetto_audio
        
utente = Utente(0, 'Fabio', 'fabio.bila79@gmai.com')
utente.crea_progetto('ciao', 'lirico')
utente.progetti[0].aggiungi_traccia('ciao', 40, 34)

strumento = StrumentoVirtuale('6784', 'chitarra', 'elettrica')
strumento.suona_nota('do', 2)

utente.progetti_per_genere()
utente.conta_progetti_totali()
utente.strumento_piu_usato()