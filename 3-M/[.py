N= 5
S = 11001

migliore_posizione = 0
for y in N:
    numero_soldatini = 0
    if S[y] ==0:
        while True:
            if S[y-1]==1:
                numero_soldatini+=1
            else:
                break
print(numero_soldatini)



   
