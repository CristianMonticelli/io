n1 = input("numero1:")
n2 = input("numero2:")
n3 = input("numero3:")
if n1>n2 and n1>n3:
    print("il piu grande è il numero1")
elif n2>n3 and n2>n1:
    print("il piu grande è il numero2")
elif n3>n2 and n3>n1:
    print("il piu grande è il numero3")
else: 
    print("non mettere numeri uguali")