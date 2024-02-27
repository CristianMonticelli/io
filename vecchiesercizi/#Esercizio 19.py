#Esercizio 19
#Dato in input un numero scritto con sistema di numerazione decimale (intero), calcolare la sua conversione in binario.
# Dato che la stampa a video del numero deve avvenire in ordine inverso da quello del calcolo, usare una lista per stampare il valore corretto.
numero_decimale = int(input("numero decimale"))
list=[]
while numero_decimale==0:
    binario2=numero_decimale%2
    numero_decimale=numero_decimale//2
    list.append[0](binario2)
print(list)