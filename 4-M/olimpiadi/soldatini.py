N = 5
S =[1 ,1 ,0 ,0 ,1]
t=0
for i in range(N):
    numero_soldatini_salvati = 0
    #print(f'S[i]{S[i]}')
    numero_soldatini = 0
    if S[i] == 0:
        
        for j in range(i-1,-1,-1):
            if S[j]==0:
                break
            numero_soldatini+=1
            #print(f'S[j]{S[j]}')

        #print(numero_soldatini)
        for y in range(i+1,N):
            if S[y]==0:
                break
            numero_soldatini+=1
            #print(f'S[j]{S[j]}')
        #print(numero_soldatini)
        #print('fine')
    if numero_soldatini>numero_soldatini_salvati:
        t = i
        numero_soldatini_salvati=numero_soldatini
print(f"la miglior posizione e {t}")       
