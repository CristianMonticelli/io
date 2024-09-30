#funzione 1 Scrivere una funzione che gestisca l'input di n valori 
#(con n scelto dall'utente) e li restituisca in una lista.
#def input_n () -> list[int]:
def input_n() -> list[int]:
    numero_numeri = int(input("quanti valori vuoi inserire:"))
    lista_valori = []
    for i in range(numero_numeri):
        numero = input(f'numero {i+1}: ')
        lista_valori.append(numero)
    return lista_valori
valori = input_n()
print(valori)

#Funzione 2:
#Scrivere una funzione alla quale passato un numero intero 
#restituisca True se esso è intero e False in caso contrario.
numero = int(input('numero da definire pari/disperi (true=pari e false=dispari)'))
def is_pari(numero: int) ->bool:
    numero = numero%2
    if numero==0:
        return True
    else:
        return False
numero_output = is_pari(numero)
print(numero_output)

#Funzione 3:
#Scrivere una funzione che data in input una lista.
# Calcoli la somma dei quadrati dei numeri pari presenti nella lista
# e restituisca tale valore.
lista_valori = [1,2,3]
def somma_quadrati (lista_valori: list[int]) -> int:
    somma = 0 
    for i in lista_valori:
        somma += i
    return somma
risultato = somma_quadrati(lista_valori)
print(risultato)