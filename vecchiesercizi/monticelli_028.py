#Scrivere una funzione che passati come parametro la classe ambientale (euro 0, euro1,...., euro6), 
#i kW e gli anni passati dall'immatricolazione di un autoveicolo, calcoli il bollo auto e l'eventuale superbollo.
# Nel caso non sia previsto il superbollo si scelga se restituire 0 oppure None. Utilizzare la funzione in un programma di esempio.
#
#N.B.
#Creare una funzione specifica per il superbollo da usare nella funzione principale.
#es.
#def calcola_superbollo (kW:int, immatricolazione: int) ->float: ....
#
#Signature metodo principale:
#def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None: ....
#N.B.
#La funzione può eseguire un controllo sui dati inseriti in ingresso e in caso di dati non validi (es. negativi) restituisce None
#
#
#utilizzo:
#bollo, superbollo = calcola_bollo (.......................................
#
#Calcolo bollo:
#Euro 0 fino a 100 kW pagano 3 euro a kW e 4,50 euro per ogni kW oltre i 100
#Euro 1 fino a 100 kW pagano 2,9 euro a kW e 4,35 euro per ogni kW oltre i 100
#Euro 2 fino a 100 kW pagano 2,8 euro a kW e 4,20 euro per ogni kW oltre i 100
#Euro 3 fino a 100 kW pagano 2,7 euro a kW e 4,05 euro per ogni kW oltre i 100
#Euro 4 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 5 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 6 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Calcolo superbollo:
#Auto nuove e fino a 5 anni pagano 20 euro per ogni kW oltre i 185
#Dopo i primi 5 anni pagano 12 euro per ogni kW oltre i 185
#Dopo i 10 anni pagano 6 euro per ogni kW oltre i 185
#Dopo i 15 anni pagano 3 euro per ogni kW oltre i 185
#Dopo i 20 anni non pagano il superbollo



def calcola_superbollo (kW:float, anni_dallimmatricolazione: int) ->float | None:
    super_bollo =0
    if kW>185:
        kW=kW-185
        if anni_dallimmatricolazione>=20:
            super_bollo = 0
        elif anni_dallimmatricolazione>=15:
            super_bollo = kW*3
        elif anni_dallimmatricolazione>=10:
            super_bollo = kW*6
        elif anni_dallimmatricolazione>5:
            super_bollo = kW*12   
        else:
            super_bollo = kW*20

    return super_bollo



def calcola_bollo (classe_ambientale:str, kW:float, anni_dallimmatricolazione:int ) ->list[float] | None:
    bollo = 0
    if kW>=0:
        match classe_ambientale:
            case 'Euro 0':
                if kW<=100:
                    bollo=kW*3
                    
                else:
                    bollo=300+(4.50*(kW-100))

            case 'Euro 1':
                if kW<=100:
                    bollo=kW*2.9
                    
                else:
                    bollo=290+(4.35*(kW-100))

            case 'Euro 2':
                if kW<=100:
                    bollo=kW*2.8
                    
                else:
                    bollo=280+(4.20*(kW-100))

            case 'Euro 3':
                if kW<=100:
                    bollo=kW*2.7
                    
                else:
                    bollo=270+(4.05*(kW-100))

            case 'Euro 4':
                if kW<=100:
                    bollo=kW*2.58
                    
                else:
                    bollo=258+(3.87*(kW-100))

            case 'Euro 5':
                if kW<=100:
                    bollo=kW*2.58
                    
                else:
                    bollo=258+(3.87*(kW-100))

            case 'Euro 6':
                if kW<=100:
                    bollo=kW*2.58
                    
                else:
                    bollo=258+(3.87*(kW-100))
        

    else:
        print('!!!ATTENTION!!! non puoi mettere numeri inferiori a 0') 
        bollo == None
    
    return [bollo,calcola_superbollo(kW,anni_dallimmatricolazione)]
while True:
    print('''le classi ambientali sono:
        Euro 0
        Euro 1
        Euro 2
        Euro 3
        Euro 4
        Euro 5
        Euro 6''')

    classe_ambientale= input('classe ambientale scelta (riscrivere il nome di una classe es.Euro N):')
    if classe_ambientale in ['Euro 0','Euro 1','Euro 2','Euro 3','Euro 4','Euro 5','Euro 6']:
        break
    else:
        print("!!!ATTENTION!!! controlla di aver scritto bene l'opzione")
        input('premi invio per continuare...')
kW = float(input('kW'))
anni_dallimmatricolazione = int(input("anni dall'immatricolazione"))




super_bollo = calcola_superbollo(kW, anni_dallimmatricolazione)
bollo,super_bollo = calcola_bollo(classe_ambientale, kW, anni_dallimmatricolazione)
bollo_totale = bollo + super_bollo
print(f'''calcoli:
    Bollo:{bollo}
    Super bollo:{super_bollo}
    Totale bollo:{bollo_totale}''')




