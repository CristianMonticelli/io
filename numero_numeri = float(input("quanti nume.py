numero_numeri = float(input("quanti numeri ci sono da sommare?"))
totale=0
for totale in range(numero_numeri) :
    numero_da_sommare = float(input("numero da sommare"))
    totale += numero_da_sommare
    
print(f"totale {totale}")
