import random

#creazione mazzo
def crea_mazzo (semi:list, valori:list) ->list[dict]:
    mazzo = []
    for i in semi:
        for y in valori:
            mazzo.append({'seme':i,
                        'valore':y})
    
    return mazzo


#mescola mazzo
def mischia_mazzo(mazzo: list[dict]) -> list[dict]:
    for i in range(random.randint(5,10)):
        random.shuffle(mazzo)
    #print(mazzo)
    return mazzo


#estrarre carta
def estrai_carta(mazzo:list[dict]) -> dict|None:
    if mazzo == []:
        carta_pescata= None
    else:    
        carta_pescata =random.choice(mazzo)
    
        mazzo.remove(carta_pescata)
    
    return carta_pescata


def turno_giocatore (mazzo:list[dict]) -> float | None:
    mano_giocatore = 0

    
    
    while True:
        choise = input('vuoi estrarre (s/n):')
        if choise == 'n':
            break

        elif choise== 's':
            carta_pescata=estrai_carta(mazzo)
            if carta_pescata == None:
                print('carte finite')
                mano_giocatore=21.0

                break
            print(f'carta pescata:{carta_pescata}')
            if int(carta_pescata['valore'])>=8 and int(carta_pescata['valore'])<=10:
                mano_giocatore += 0.5
            else:
                mano_giocatore += int(carta_pescata['valore'])

            if mano_giocatore > 7.5:
                print('hai perso tutto')
                mano_giocatore = None
                break
        else:
            input('''
              non hai scritto s/n
              premere invio per continuare:''')
    
    return mano_giocatore



def turno_banco(mazzo:list[dict], punteggio_giocatore:float) -> float:
    mano_banco = 0 
    while True:
        carta_pescata=estrai_carta(mazzo)
        if carta_pescata == None:
            print('carte finite')
            mano_banco=21.0
            
            break

        if int(carta_pescata['valore'])>=8 and int(carta_pescata['valore'])<=10:
            mano_banco += 0.5
        else:
            mano_banco += int(carta_pescata['valore'])
        if  mano_banco> 7.5:
            print(f'il banco a perso con:{mano_banco}')
            mano_banco = None
            break
        if mano_banco>punteggio_giocatore:
            print(f'banco vince con:{mano_banco}')
            
            break

        
        
        
        
    return mano_banco
    





user_name = input('nome giocatore:')
semi = ['coppe','denari','spade','bastoni']
valori = [1,2,3,4,5,6,7,8,9,10]
puntata = input('puntata giocatore (€):')

#creazione mazzo
carte_non_mischiate = crea_mazzo(semi,valori)
carte_mischiate = mischia_mazzo(carte_non_mischiate)

#gioco giocatore
while True:
    

    mano = turno_giocatore(carte_mischiate)

    if mano != None:
        banco = turno_banco(carte_mischiate,mano)
    else:
        print('vittoria del banco a tavolino')
    if mano == 21.0 or banco == 21.0:
        print('carte esurite')













