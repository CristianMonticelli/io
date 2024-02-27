#1 creo una lista di dizionari con 3 chiavi per creare una rubrica
rubrica = [{
    'nome':'Fabio',
    'cognome':'Bilancioni',
    'numero_telefono':'333 555 6666'
},{
    'nome':'Cristian',
    'cognome':'Monticelli',
    'numero_telefono':'333 555 3333'
}
    
,
{
    'nome':'Diego',
    'cognome':'Torsani',
    'numero_telefono':'333 222 6666'
}
]
#2 stampo a video la rubrica
for i in rubrica:
    print(f'''nome:{i['nome']},cognome:{i['cognome']},numero tel.:{i['numero_telefono']}''')
#3 aggiungo un "contatto" alla lista
rubrica.append({
    'nome':'Kamil',
    'cognome':'Ibragimov',
    'numero_telefono':'333 989 6066'})
#4 controllo e se trovo che e' presente il contatto cambio numero
nome_da_cambiare = input('nome da cambiare:')
cognome_da_cambiare = input('cognome da cambiare:')

for i in rubrica:
    if i['nome']==nome_da_cambiare and i['cognome']==cognome_da_cambiare:
        nuovo_numero = input('numero da cambiare:')
        i['numero_telefono'] = nuovo_numero
    else:
        print('numero non trovato')
#5 ripetp il 2 con un numero cambiato
for i in rubrica:
    print(f'''nome:{i['nome']},cognome:{i['cognome']},numero tel.:{i['numero_telefono']}''')