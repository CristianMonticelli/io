n1 = int(input("numero1"))
n2 = int(input("numero2"))
n3 = n1 % 2
n4 = n2 % 2
if  n3 == 1 and n4 == 1:
    print("sono dispari")
elif n3 == 0 and n4 == 0:
    print("sono pari")
elif n3 == 1 and n4 == 0:
    print("solo il primo è dispari")
else: 
    print("solo il primo è pari")