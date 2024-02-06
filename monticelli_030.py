#1) def genera_cartella(id: int<str>)->dict:
#La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
#N.B.
#La cartella ha le seguenti caratteristiche:
#1) 3 righe e 9 colonne
#2) 15 numeri in totale (5 per riga)
#3) ogni colonna ha solo i numeri della decina di riferimento: 
#la prima dall'1 al 9, la seconda dal 10 al 19....l'ultima dall'80 al 90
import random
import os
def genera_cartella (cartelle:dict,nome_utente:str) -> dict:
    
    counter = 27      
    righe = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]
    
    while counter >0:
        numero = random.randint(1,90)
        if numero not in righe[0] and numero not in righe[1] and numero not in righe[2]: 
            if numero==90:
                posizione=(int(numero/10))-1
            else:
                posizione=(int(numero/10))
                for i in righe:
                    if i[posizione]==0:
                        i[posizione] = numero
                        counter-=1
                        break
                       
    for j in righe:
        spazi_vuoti =4
        while spazi_vuoti > 0:
            posizione_vuoto = random.randint(1,8)
            if j[posizione_vuoto]!=0:
                j[posizione_vuoto] = 0
                spazi_vuoti-=1
    
    #print(righe)
    cartelle[nome_utente] = {'cartella': righe,
                    'caselle_complete':[0,0,0],
                    'vincite':[]}
    
    return cartelle

    
#2) def estrai_numero(numeri_estratti: list[])->int:
#La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando 
#che non sia duplicato, 
#e restituisce tale numero come intero.        

def estrai_numero(numeri_estratti: list[int])->int:
    while True:
        numero_estratto = random.randint(1,90)
        if numero_estratto not in numeri_estratti:
            numeri_estratti.append(numero_estratto )
            input(f'''      nuovo numero (premi invio):         {numero_estratto}''')
            break
    
    return numero_estratto
#3) def controlla_cartella(cartella: dict, numeri_estratti[])->list[bool]:
#Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella. 
#Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si 
#riferisce alla tombola/bingo.
#es.
#[True, True, False, False, False] per una cartella che ha fatto terno(naturalmente per fare terno bisogna aver fatto anche ambo....)

def controlla_cartella(cartelle: dict, numero_estratto: int)->dict:
    
    vincite = []
    for z in cartelle:
        for e in range(3):
            for i in cartelle[z]['cartella'][e]:    
                if i == numero_estratto:
                    if numero_estratto==90:
                        posizione=(int(numero_estratto/10))-1
                    else:
                        posizione=(int(numero_estratto/10))
                    cartelle[z]['cartella'][e][posizione] = 'X'
                        
                    cartelle[z]['caselle_complete'][e]+=1  
        linee_complete =0                         
        for u in cartelle[z]['caselle_complete']:
            if u >= 2:
                if 'ambo' not in vincite:
                    vincite.append ('ambo')               
            if u >= 3:
                if 'terno' not in vincite:
                    vincite.append('terno')
            if u >= 4:
                if 'quaterno' not in vincite:
                    vincite.append('quaterno')
            if u == 5:
                linee_complete+=1
        if linee_complete ==1:
            vincite.append('cinquina')
        if linee_complete ==2:
            vincite.append('decina') 
        if linee_complete ==3:
            vincite.append('tombola' )       
            exit
        cartelle[z]['vincite'] = vincite
    return cartelle
tabellone = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]

cartelle={}
numeri_estratti=[]    
os.system('cls' if os.name == 'nt' else 'clear')   
input('''
                                    TOMBOLA  
                                                
                                     START
                            premere invio per iniziare...''')

os.system('cls' if os.name == 'nt' else 'clear')
numero_giocatori = int(input('numero giocatori:'))

for i in range(numero_giocatori):
    nome_utente = input('id:')
    cartelle= genera_cartella(cartelle,nome_utente)
    
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    proseguimento = input('''
                          premi invio per estrarre e visualizzare vincite e stato cartella/e
                                      digita S (e invio) per cocludere subito 
                          invece per visualizzare le cartelle e i vari dati digita C (e invio)
                                                    cosa scegli?:''')
    
    if proseguimento == 'S':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    elif proseguimento== 'C':
        print(f'''TABELLONE:
                    {tabellone[0]}
                    {tabellone[1]}
                    {tabellone[2]}
                    {tabellone[3]}
                    {tabellone[4]}
                    {tabellone[5]}
                    {tabellone[6]}
                    {tabellone[7]}
                    {tabellone[8]}''')
        for z in cartelle:
            
             
            print(f'''      cartella del giocatore:{z}
                
                    {cartelle[z]['cartella'][0]}                   
                    {cartelle[z]['cartella'][1]}                   
                    {cartelle[z]['cartella'][2]}                   
                    
                    cosa hai 'vinto':{cartelle[z]['vincite']}''')
            input('premere invio per proseguire:')
    numero_estratto = estrai_numero(numeri_estratti)
    riga = numero_estratto/10
    if int(riga)>=1:
        riga=(int(numero_estratto/10))-1
    else:
        riga=(int(numero_estratto/10))
    colonna =  (int(numero_estratto/10))-1
    tabellone[riga][colonna]  = numero_estratto
    cartelle = controlla_cartella(cartelle,numero_estratto)