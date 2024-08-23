N = 6
prima = [1,3, 1, 2, 1, 1]
dopo = [1,3, 0, 2, 1, 1]
t = 0
for i in range(N):
    if prima[i]!=dopo[i]:
        t+=1
print(t)

