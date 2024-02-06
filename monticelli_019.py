#Esercizio 19
#Dato in input un numero scritto con sistema di numerazione decimale (intero), calcolare la sua conversione in binario.
# Dato che la stampa a video del numero deve avvenire in ordine inverso da quello del calcolo, usare una lista per stampare il valore corretto.
numero_decimale = int(input("numero decimale: "))
lista = []

while numero_decimale != 0:
    binario = numero_decimale % 2
    numero_decimale = numero_decimale // 2
    lista.append(binario)
    
lista.reverse()

for x in lista:
  print(x,end = "")
print(" is your number in binary")
