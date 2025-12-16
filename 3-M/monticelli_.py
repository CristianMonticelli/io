#ESERCIZIO 20

#Scrivere un programma che permetta la gestione di una lista della spesa. Esso deve prevedere un menu così formato:

#"""
#Scegliere l'opzione desiderata:
#1) Visualizza lista
#2) Aggiungi item e quantità
#3) Modifica quantità di un item
#4) Rimuovi item
#5) Esci
#Scelta:_

#"""
#Per la lista della spesa si consiglia l'utilizzo di due liste, una per gli elementi una per le quantità
import os
fine = 0
lista_spesa = []
lista_quantità = []
while fine == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''Scegliere l'opzione desiderata:
1) Visualizza lista
2) Aggiungi item e quantità
3) Modifica quantità di un item
4) Rimuovi item
5) Esci ''')
    
    
    scelta_opzione = input("scrivi il numero:")
    
    match scelta_opzione:
    
        case '1': 
            for i in range(len(lista_spesa)):
                print(lista_spesa[i] + " " + str(lista_quantità[i]) )
                input("premere invio per continuare...")
        case '2': 
            oggetto_da_aggiungere = input('cosa vuoi aggiungere alla lista:')
            quantità_oggetto = input("quantità oggetto:")
            lista_spesa.append(oggetto_da_aggiungere) 
            lista_quantità.append(quantità_oggetto)
        case '3' : 
            for i in range(len(lista_spesa)):
                print(lista_spesa[i] + " " + str(lista_quantità[i]) )
            oggetto_da_modificare = input('di quale elemento vuoi modificare la quantità?')
            nuova_quantità = input('nuova quantità')
            index = lista_spesa.index(oggetto_da_modificare)
            lista_quantità[index] = nuova_quantità
        case '4' :
            print(lista_spesa)
            oggetto_da_rimuovere = input('cosa vuoi modificare alla lista')
            index = lista_spesa.index(oggetto_da_rimuovere)
            lista_spesa.remove(oggetto_da_rimuovere)
            lista_quantità.pop(index)

        case '5' : 
            print('finito')
            fine = 1
           