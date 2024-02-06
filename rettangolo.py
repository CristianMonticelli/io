#!/usr/bin/env python3

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def solve(t):
    input() # prima riga vuota

    x1, y1 = map(int, input().strip().split())
    x2, y2 = map(int, input().strip().split())
    x3, y3 = map(int, input().strip().split())

    # 4 7
    # 1 7
    # 1 5
    if x1 != x2 and x1 != x3:
        x4 = x1
    elif x2 != x1 and x2 != x3:
        x4 = x2
    elif x3 != x1 and x3 != x2:
        x4 = x3

    if y1 != y2 and y1 != y3:
        y4 = y1
    elif y2 != y1 and y2 != y3:
        y4 = y2
    elif y3 != y1 and y3 != y2:
        y4 = y3
    
    print(f"Case #{t}: {x4} {y4}")


T = int(input().strip())

for t in range(1, T + 1):
    solve(t)

sys.stdout.close()