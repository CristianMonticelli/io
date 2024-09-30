
import os
#1. Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
dipendenti = []
progetti=[]
dipendenti_progetti=[{'nome_dipendente':'mario',
                      'nome_progetto':'i',
                      'ore_lavorate':30,
                      },{}]
while True:
    choise1 = input('''
non sciere niente e premere invio per continuare ad aggiungere dipendenti.
quando hai finito scrivere basta.
...''')
    
    if choise1=='':
        dipendente={}
        nome_dipendente=input('nome:')
        ruolo_dipendente=input('ruolo:')
        stipendio_base_dipendente=float(input('stipendio_base:'))
        
        
        dipendente['nome_dipendente']=nome_dipendente
        dipendente['ruolo_dipendente']=ruolo_dipendente
        dipendente['stipendio_base_dipendente']=stipendio_base_dipendente
        
        dipendente['stipendio_totale']=0
        dipendenti.append[dipendente]

        os.system('cls' if os.name == 'nt' else 'clear')
    elif choise1=='basta':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
        
    else:
        print('!!!ATTENZIONE!!! la scielta fatta non è possibile')
        input('premere invio per continuare...')
        os.system('cls' if os.name == 'nt' else 'clear')
#2
for r in dipendenti:
    print(r['nome'])
input('premere invio per continuare...')
os.system('cls' if os.name == 'nt' else 'clear')
#fai nome:ore
#3/4
while True:
    choise2 = input('''
non sciere niente e premere invio per continuare ad aggiungere progetti.
quando hai finito scrivi basta.
...''')
    if choise2=='':
        progetto={}
        
        nome_progetto=input('nome:')
        budget_progetto=float(input('budget:'))
        retribuzione_per_oraria=float(input('retribuzione dipendenti oraria:'))
        durata = float(input('durata prevista:'))
        progetto['nome_progetto'] = nome_progetto
        progetto['budget_progetto'] = budget_progetto
        progetto['retribuzione_progetto'] = retribuzione_per_oraria
        progetto['durata_progetto'] = durata
        
        #print(progetto)
        for i in dipendenti:
            print(i['nome'])
            deve_lavorarci = input('deve_lavorarci (scrivere si o no)')
            if deve_lavorarci=='si':    
                dipendente_progetto={}
                dipendente_progetto['nome_dipendente']=i['nome']
                dipendente_progetto['nome_progetto']= nome_progetto

                ore_progetto_dipendente=float(input('quante ore ci deve lavorare:'))
                dipendente_progetto['ore_giornaliere_dipendente']=ore_progetto_dipendente

                retribuzione_per_durata = retribuzione_per_oraria*ore_progetto_dipendente
                stipendio_totale = i['stipendio_base']+retribuzione_per_durata
                budget_progetto -= retribuzione_per_durata
                i['stipendio_totale']+=stipendio_totale
                dipendente_progetto['ore_per_progetto'][nome_progetto] = durata*i['ore_giornaliere']
            

        progetto['budget_senza_stipendi'] = budget_progetto
        #print(progetto)

        #print(dipendenti)
        progetti.append(progetto)
        input('premere invio per continuare...')

        os.system('cls' if os.name == 'nt' else 'clear')
    elif choise2=='basta':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        print('!!!ATTENZIONE!!! la scielta fatta non è possibile')
        input('premere invio per continuare...')
        os.system('cls' if os.name == 'nt' else 'clear')
#print(progetti)
#5. Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
for o in dipendenti:
    print(f'''
          nome:{o['nome']}
          mansione:{o['ruolo']}
          stipendio iniziale:{o['stipendio_base']}->stipendio totale:{o['stipendio_totale']} 
          progetti e ore:{o['ore_per_progetto']}''')
input('premere invio per continuare...')

os.system('cls' if os.name == 'nt' else 'clear')    
#6. Stampa  le ore lavorate totali e il budget rimanente per ogni progetto.
for g in progetti:
    print(f'''
          progetto:{g['nome_progetto']}
          ore (previste):{g['durata_progetto']}
          budget:{g['budget_progetto']}->{g['budget_senza_stipendi']}
''')
input('premere invio per finire...')

os.system('cls' if os.name == 'nt' else 'clear')