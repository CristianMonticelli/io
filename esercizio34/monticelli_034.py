import argparse
import matplotlib.pyplot as plt
#Esercizio 34 - Traccia una funzione con matplotlib e argparse
#In questo esercizio utilizzerai il modulo argparse per accettare argomenti della riga di comando e il modulo matplotlib per tracciare funzioni matematiche.
#
#Creerai uno script denominato plot_functions.py che accetta un numero n e uno o più tipi di funzioni come argomenti. I tipi di funzioni possono essere "lineari", "polinomiali" o "esponenziali".
#
#Lo script dovrebbe poter essere eseguito in questo modo:
#
#python plot_functions.py  --polinomiale --numero esponenziale
#
#Le funzioni da tracciare sono le seguenti:
#
#Lineare: 
#Polinomio: y = x^n
#Esponenziale: y = n^x
#Per ogni funzione specificata, lo script dovrebbe generare un grafico utilizzando matplotlib. I valori x dovrebbero essere un elenco di valori compresi tra 0 e 10 (inclusi). I valori y dovrebbero essere calcolati in base al tipo di funzione e al numero di input n.
#
#Ricorda di etichettare l'asse x, l'asse y e fornire un titolo per ogni grafico. Mostra tutti i grafici alla fine.

def linear(n):
    xpoints = [i for i in range(1, 11)] # 1 .. 10
    ypoints = [n * i for i in range(1, 11)] # y = n * x 

    plt.plot(xpoints, ypoints) 
    plt.savefig("linear.png")
    return 

def polinomial(n):
    xpoints = [i for i in range(1, 11)] # 1 .. 10
    ypoints = [(i)**n for i in range(1, 11)] # y = n * x 

    plt.plot(xpoints, ypoints) 
    plt.savefig("polinomial.png")
    return 

def exponenzial(n):
    xpoints = [i for i in range(1, 11)] # 1 .. 10
    ypoints = [(i for i in range(1, 11))**n] # y = n * x 

    plt.plot(xpoints, ypoints) 
    plt.savefig("exponenzial.png")
    return 

def main():
    parser = argparse.ArgumentParser(description="Square or cube a number")
    parser.add_argument("number", type=int, help="The number to be grafic")
    
    parser.add_argument("--linear", action="store_true", help="Square the number")
    parser.add_argument("--polinomial", action="store_true", help="Square the number")
    args = parser.parse_args()
    number = args.number
    linear(number)
    polinomial(number)
    exponenzial(number)


if __name__ == "__main__":
    main()