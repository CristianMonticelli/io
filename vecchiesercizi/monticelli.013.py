#Scrivere 10 volte la parola "ciao", sommare i numeri da 10 a 20 (compresi gli estremi), sommare i numeri pari fino a 30 (30 incluso) e moltiplicare i numeri da 1 a 10
for parole in range (10):
    print("ciao")
    
somma_da_10=0
for numeri in range(9,21):
    somma_da_10+=10+numeri
print(f"somma dei numeri da 10 a 20 ={somma_da_10}")

somma_fino_30=0
for numeri_pari in (0,30,2):
    somma_fino_30+=numeri_pari
print(f"somma numeri pari fino 30{somma_fino_30}")
    
