#1 metto in una lista 4 frutti
lista_frutti = ['mela','banana','uva','melone']

#2 metto a video tutti i singoli frutti
for i in lista_frutti:
    print(i)
print('----------')
#3 aggiungo un frutto
lista_frutti.append('kiwi')

#4 ripeto il 2 con un frutto in piu'
for i in lista_frutti:
    print(i)
print('----------')
#5 tolgo un frutto
lista_frutti.remove('banana')
#6 ripeto il 2 con un frutto tolto
for i in lista_frutti:
    print(i)
print('----------')
#7 stampo il terzo elemento a apice 2 perche' partiamo a contare da 0
print(lista_frutti[2])