#Il programma ci permette di gestire una flotta aziendale di 
# veicoli. Ogni veicolo ha una marca, un modello 
# e un tipo di carburante. Esistono due tipologie di veicoli: 
# *auto* e *camion*. Ogni veicolo può essere aggiunto alla 
# flotta, e il programma deve consentire di visualizzare le 
# informazioni sui veicoli.
#
#Requisiti:
#1. Creare una classe `Veicolo` con gli attributi di base: 
# `marca`, `modello` e `carburante`.
#2. Creare due sottoclassi: `Auto` e `Camion`. 
# Ogni sottoclasse deve semplicemente ereditare gli attributi 
# da `Veicolo`.
#3. La classe `Flotta` deve gestire una lista di veicoli, 
# permettere l’aggiunta di nuovi veicoli, e la visualizzazione 
# delle informazioni di tutti i veicoli.

class Veicolo:
    def __init__(self,marca,targa,modello,tipo_carburante):
        self.marca: str = marca
        self.targa: str = targa
        self.modello: str = modello
        self.tipo_carburante: str = tipo_carburante
    def __str__(self):
        return f'marca:{self.marca} targa:{self.targa} modello:{self.modello} tipo carburante:{self.tipo_carburante} '

class Auto(Veicolo):
    def __init__(self,marca,targa,modello,tipo_carburante,cavalli):
        super().__init__(marca,targa,modello,tipo_carburante)
        self.cavalli: int = cavalli
    def __str__(self):
        return f'{super.__str__()} cavalli{self.cavalli}CV'
      
class Camion(Veicolo):
    def __init__(self,marca,targa,modello,tipo_carburante,portata):
        super().__init__(marca,targa,modello,tipo_carburante)
        self.portata: int = portata
    def __str__(self):
        return f'{super.__str__()} portata{self.portata}Kg'
        
class Flotta:
    def __init__(self,nome):
        self.nome: str = nome
        self.veicoli: list[Veicolo] = []
    def aggiungi_veicoli(self,nuovo_veicolo):
        problemi = {"aggiunto":False,
                    "targa_gia_presente":False,
                    'carburante_sbagliato':False,
                    "veicolo_gia_presente":False}

        for v in self.veicoli:
            if v.targa == nuovo_veicolo.targa:
                problemi["targa_gia_presente"] = True
            if v==nuovo_veicolo:
                problemi["veicolo_gia_presente"] = True
        if nuovo_veicolo.tipo_carburante not in ['disel','benzina','elettrica']:
                problemi['carburante_sbagliato'] = True

        if nuovo_veicolo not in self.veicoli and problemi == {"aggiunto":False,
                    "targa_gia_presente":False,
                    'carburante_sbagliato':False,
                    "veicolo_gia_presente":False}:
            self.veicoli.append(nuovo_veicolo)
            problemi["aggiunto"] = True
        return problemi
    def visualizzare_informazioni(self):
        for v in self.veicoli:
            print(v)

flotta = Flotta('Bernabini')

auto1 = Auto('Toyota','cd123rt','Yaris','benzina','75')
auto2 = Auto('Ford','ca123rt','Focus','carbone','134')
auto3 = Auto('Lancia','cd123rt','Y','disel','104')
camion = Camion('Piaggio','al487jd','Ape','benzina','200')

print(flotta.aggiungi_veicoli(auto1))
print(flotta.aggiungi_veicoli(auto2))
print(flotta.aggiungi_veicoli(auto3))
print(flotta.aggiungi_veicoli(camion))
flotta.visualizzare_informazioni()

