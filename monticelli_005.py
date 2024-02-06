
Esercizi IF
Angelo Galanti
•
Ieri
Consegna: Domani
# ESERCIZIO 5
# Write a program that asks the user for their age and prints out whether they are a child (age 0-12), teenager (age 13-19), adult (age 20-64), or senior (age 65+).

# ESERCIZIO 6
# 1. Ask the user for two numbers
# 2. Convert the user's input to integers
# 3. Use if-else statements and logical operators to determine whether the numbers are both even, both odd, or one even and one odd
# 4. Print out the result
Commenti sul corso
Il tuo lavoro
Assegnato

monticelli_005.py
Testo

Monticelli_006.py
Testo
Commenti privati
eta = int(input("srivin la tua età:"))
if eta >= 0 or eta <= 12:
    print("bambino/a")
elif eta >= 13 or eta <= 19:
    print("ragazzo/a")
elif eta >= 20 or eta <= 64:
    print("adulto")
elif eta > 65: 
    print("anzino")
else:
    print("non puoi mettere un eta inferiore a 0")