

# per ogni citta controllo se rispetta le condizioni per tutte le citta precedenti

def test():
    X = [1,2]
    Y = [2,1]
    t = 0 #numero citta
    for i in range(len(X)):
        print(f"Controllo citta {i} con coordinate {X[i]} e {Y[i]}")
        for j in range(i):
            print(f"j vale {j}")
            if X[i]>=X[j] and Y[i]>=Y[j] or X[i]<=X[j] and Y[i]<=Y[j]:
                continue
            else:
                return t
        t+=1

print(test())

# for x1,y1 in zip(X,Y):
    
#     for x2,y2 in zip(X[],Y):


#         if x1>=x2 and y1>=y2 or x1<=x2 and y1<=y2:
#             t+=1 #aggiunta citta
#             continue
#         else:
#             if stop==1:
#                 #fine tutto
#             X.remove(x2)
#             Y.remove(y2)
            
#     stop+=1
    
        


