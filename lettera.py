#!/usr/bin/env python3

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')


def solve(t):
    input() # prima riga vuota

    N = int(input().strip())
    W = list(map(int, input().strip().split()))

    # aggiungi codice...
    K1, K2 = 42, 69

    print(f"Case #{t}: {K1} {K2}")


T = int(input().strip())

for t in range(1, T + 1):
    solve(t)