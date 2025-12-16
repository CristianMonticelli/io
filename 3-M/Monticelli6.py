#creiamo un dizionario di dizionari con una lista
studi_medici = {
    'Dr_Cappelli':{
        'nome':'Roberto Cappelli',
        'specializzazione':'Pediatra',
        'pazienti':['Luca','Antonio']
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
#stampiamo il paziente antonio

print(f"{studi_medici['Dr_Cappelli']['pazienti'][1]}")

       