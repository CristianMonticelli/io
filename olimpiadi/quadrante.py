#!/usr/bin/env python3

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')


def solve(t):
    input() # prima riga vuota
    
    N = int(input().strip())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().strip().split())
        X.append(x)
        Y.append(y)


    risposta = 0 #numero citta
    for i in range(len(X)):
        print(f"Controllo citta {i} con coordinate {X[i]} e {Y[i]}")
        for j in range(i):
            print(f"j vale {j}")
            if X[i]>=X[j] and Y[i]>=Y[j] or X[i]<=X[j] and Y[i]<=Y[j]:
                continue
            else:
                return risposta
        risposta+=1

    

    print(f"Case #{t}: {risposta}")


T = int(input().strip())

for t in range(1, T + 1):
    solve(t)

sys.stdout.close()