#Esercizio 17
#Scrivere un programma che passati in input n valori popoli una lista. In seguito chiede all'utente di inserire un valore in modo tale da 
#verificare che esso sia presente nella lista. Stampare a video ("Valore presente"/"Valore non presente").
n_valori = int(input("numero valori"))
numero_da_trovare = int(input("numero da trovare"))
list=[]
for i in range(n_valori):
    list.append(i)

if numero_da_trovare in list:
    print(f"il numero {numero_da_trovare} è presente")
else:
    print(f"il numero {numero_da_trovare} non è presente")