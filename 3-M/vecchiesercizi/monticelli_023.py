import os
stanze = {}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    1) Creare una nuova stanza (id, denominazione, metratura) 
    2) Aggiungere un opera ad una stanza(titolo, artista, anno)
    3) Consultare le opere presenti in una stanza
    4) Consultare le stanze presenti
    5) Cercare le informazioni su un opera
    6) Cancellare un opera
    7) Cancellare una stanza solo se vuota
    8) uscire''')
    choise = int(input('chose your opion:'))

    if choise < 9 and choise > 0: 
       
        match choise:
            case 1:
                info_stanza = {}
                name_stanze = input('inserisci il nome della stanza:')
                metratura_stanze = input('inserisci il metratura della stanza:')
                denominazione_stanze = input('inserisci la denominazione della stanza:')
                info_stanza['metratura stanza ' ] = metratura_stanze
                info_stanza['denominazione stanze '] = denominazione_stanze
                info_stanza['opere presenti'] = []
                stanze[name_stanze] = info_stanza
                
            case 2:
                if len(stanze)>0:
                    
                    dettagli_opera = {}
                    title_opera= input('titiolo:')
                    artist_opera= input('autore:')
                    year_opera= input('anno:')
                    room_choice = input('in quale stanza?:')
                    
                    dettagli_opera['titolo'] = title_opera
                    dettagli_opera['artist'] = artist_opera
                    dettagli_opera['year'] = year_opera
                    
                    stanze[room_choice]['opere presenti'].append(dettagli_opera)
                    
                    print(stanze)
                else:
                    print('devi prima creare una stanza')
                    input('premi invio per continuare')

            case 3:
                room_choice = input('in quale stanza?:')
                if room_choice != stanze:
                    for i in stanze[room_choice]['opere presenti']:
                        print(stanze[room_choice]['opere presenti'])
                        input('premi invio per continuare')
                else:
                    print('la stanza non esiste')
                    input('premi invio per continuare')

            case 4:
                for k,v in stanze.items():
                    print(f"stanza :{k}\n{v['metratura stanza ']}\n{v['denominazione stanze ']}")
                    input('premi invio per continuare')

            case 5:
                chois_opera = input('di quale opera vuoi le informazioni?:')
                for k,v in stanze.items():                    
                    for opera in v['opere presenti']:
                        if opera['titolo']==chois_opera:
                            print(opera)
                            input('premi invio per continuare')
                        else:
                            break
            case 6:
                chois_opera = input('quale opera vuoi eliminare:')
                for z,s in stanze.items():
                    for opera in s['opere presenti']:
                        if opera['titolo']==chois_opera:
                            stanze[z]['opere presenti'].remove(opera)
                            
                        else:
                            break
                        
                        
            case 7:
                delate_room = input('quale stanza vuoi eliminare:')
                if  delate_room in stanze and len(stanze[delate_room])==0:
                    stanze.pop(delate_room)
                    
                elif delate_room in stanze:
                    print('le stanze piene non si possono eliminare')
                    input('premi invio per continuare...')
                else:
                    print('la stanza non esiste')
                    input('premi invio per continuare...')
                   
                
                   
            case 8:
                break
                
                
                
                
                
                
    else:
        print('ATTENTION! the option selected does not exist')
        input("press enter to continue...")