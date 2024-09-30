numero_numeri = int(input("quanti numeri ci sono da sommare?"))
totale=0
numero_cicli=1
for numero_cicli in range(numero_numeri) :
    numero_da_sommare = float(input(f"numero da sommare {numero_cicli}"))
    totale += numero_da_sommare
    
print(f"totale {totale}")
