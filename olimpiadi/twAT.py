N = 5
V = [4,5,90,5,10]
T = 0
while True:
    N=5
    T+=1
    for i in V:
        resto = T%i
        print(f'{T}%{i}resto {resto}')
        if resto==0:
            N-=1
            
    if N == 0:
        break
    
print(T)