#uso le virgolette come accenti perche' dovrei cambiare tastiera
#1 creiamo un dizionario di dizionari con una lista
studi_medici = {
    'Dr_Cappelli':{
        'nome':'Roberto Cappelli',
        'specializzazione':'Pediatra',
        'pazienti':['Luca','Lukaku']
    },
    'Dr_Torsani':{
        'nome':'Diego Torsani',
        'specializzazione':'Cardiologo',
        'pazienti':['Gabriele','Alessandro']
    },
    'Dr_Cecchini':{
        'nome':'Monica Cecchini',
        'specializzazione':'Dermatologo',
        'pazienti':['Angelo','Diego']
    }
}
#2 stampiamo a video tutti i singoli 
for i,j in studi_medici.items():
    print(f"{i}")
    for k in j.items():
        print(k)
#3 aggiungiamo un paziente
studi_medici['Dr_Cecchini']['pazienti'].append('Andrea')
#4 rifacciamo il 2 la lista aggiornata
for i,j in studi_medici.items():
    print(f"{i}")
    for k in j.items():
        print(k)