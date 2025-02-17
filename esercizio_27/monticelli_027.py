#Il sistema permette di gestire le prenotazioni di voli aerei. 
# Ogni volo ha un numero di volo, una destinazione, 
# una data e ora di partenza e un numero massimo di passeggeri. 
# Esistono due tipologie di prenotazioni: e . 
# Ogni prenotazione può essere aggiunta al sistema, 
# e il programma deve consentire di visualizzare le informazioni sui voli e le prenotazioni.
#
#
#Creare una classe Volo con gli attributi di base:
#
#numeroVolo
#destinazione
#dataOraPartenza: 
#numeroMassimoPasseggeri
#
#
#Creare una classe Prenotazione con gli attributi di base:
#
#nomePasseggero
#tipoClasse
#volo
#
#
#La classe SistemaPrenotazioni deve gestire:
#
#Una lista di voli.
#Una lista di prenotazioni.
#Permettere l’aggiunta di nuovi voli e prenotazioni.
#Visualizzare le informazioni di tutti i voli e le prenotazioni.
#Specifiche delle classi
class SistemaPrenotazioni:
    def __init__(self,nome_compagnia):
        self.nome_compagnia= nome_compagnia
        self.voli= []
        self.prenotazioni= []
    def aggiungi_voli(self,nuovo_volo):
        
        if nuovo_volo not in self.voli:
            self.voli.append(nuovo_volo)
            return True
        return False
    
    def aggiungi_prenotazioni(self,prenotazione,volo):
        problemi = {"prenotazione riuscita":False,
            'prenotazione gia esistente':False,
                    'volo_gia_pieno':False}
        if prenotazione not in self.prenotazioni:
            if volo.numero_max_passeggeri>0:
                volo.numero_max_passeggeri-=1
                prenotazione.assegna_volo(volo)
                problemi['prenotazione riuscita'] = True
                self.prenotazioni.append(prenotazione)
                return problemi
        if prenotazione in self.prenotazioni:
            problemi['prenotazione gia esistente'] = True
        if volo.numero_max_passeggeri == 0:
            problemi['volo_gia_pieno'] = True
        return problemi
    def visualizzare_informazioni_tutto(self):
        print(f'Voli:')
        for v in self.voli:
            print(v)
        print(f'Prenotazioni:')
        for p in self.prenotazioni:
            print(p)
        
class Prenotazione:
    def __init__(self,nome,classe):
        self.nome_passeggero = nome
        self.tipoClasse = classe
        self.volo = None
    def assegna_volo(self,volo):
        self.volo = volo
    def __str__(self):
        return f'nome passeggero:{self.nome_passeggero}, classe:{self.tipoClasse}'
class Volo:
    def __init__(self,numero_di_volo,destinazione,data_e_ora,numero_max_passeggeri):
        self.numero_di_volo=numero_di_volo
        self.destinazione = destinazione
        self.data_e_ora= data_e_ora
        self.numero_max_passeggeri= numero_max_passeggeri
    def __str__(self):
        return f'numero di volo:{self.numero_di_volo}, destinazione:{self.destinazione},data e ora:{self.data_e_ora}, numero max passeggeri:{self.numero_max_passeggeri}'

sistema_prenotazioni = SistemaPrenotazioni('Bernabini')
volo1 = Volo("104",'las vegas','11/06/2025',2)
volo2 = Volo("2",'los santos','14/12/2025',36)
volo3 = Volo("5",'nagasaki','31/12/2026',25)
prenotazione1 = Prenotazione('Angel',"economy")
prenotazione2 = Prenotazione('Spizzu',"business")
prenotazione3 = Prenotazione('Bernabini','luxury')
print(sistema_prenotazioni.aggiungi_voli(volo1))
print(sistema_prenotazioni.aggiungi_voli(volo1))
print(sistema_prenotazioni.aggiungi_voli(volo2))
print(sistema_prenotazioni.aggiungi_voli(volo3))

print(sistema_prenotazioni.aggiungi_prenotazioni(prenotazione1,volo1))
print(sistema_prenotazioni.aggiungi_prenotazioni(prenotazione2,volo1))
print(sistema_prenotazioni.aggiungi_prenotazioni(prenotazione3,volo1))

sistema_prenotazioni.visualizzare_informazioni_tutto()