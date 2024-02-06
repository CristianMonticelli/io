#1 creo un dizionario vuoto
registro_voti = {}
#2
registro_voti['Gabriele'] = 40
registro_voti['Luca'] = 80
registro_voti['Giorgio'] = 90
#3 stampo tutti i singoli soggetti
for i in registro_voti.items():
    print(i)
print('----------')
#4 aggiungo un soggetto
registro_voti['Cristian'] = 99
#5 ripeto il 2 con uno studente in piu'
for i in registro_voti.items():
    print(i)
print('----------')
#6 controllo se ce un preciso studente
studente_da_cercare = input('nome dello studente:')
for i in registro_voti:
    if studente_da_cercare==i:
        print("lo studente e' presente") #uso le virgolette come accenti perche' dovrei cambiare tastiera
    