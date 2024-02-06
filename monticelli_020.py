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
parameter = "Geeksforgeeks"
 
match parameter:
   
    case first  : 
        do_something(first)
     
    case second : 
          do_something(second)
         
    case third : 
        do_something(third)
        .............
        ............
    case n :
        do_something(n)
    case _  : 
          nothing_matched_function()
           