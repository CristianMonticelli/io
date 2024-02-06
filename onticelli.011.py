#ESERCIZIO 11
#In una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effettuare secondo la seguente tabella:
#n.1-19 0,10 euro, n.20-100 0,08 euro, piu di 100 0,05 euro. 
#Inoltre se le fotocopie sono da rilegare viene aggiunto un costo di 1,80 euro.
#Dati in input il numero di fotocopie da effettuare, il nome del cliente e un indicazione che segnali se il plico è da rilegare, calcola il costo totale e stampa il seguente prospetto:
#Gentile Sig. ___ il suo preventivo è di ___ euro compresa la rilegatura. L'ultima riga è da scrivere solo se è richiesta la rilegatura
copie = int(input("numero fotocopie:"))
nome = input("nome e cognome:")
rilegare = input("sono da rilevare?:")
ris=0
if rilegare=="si":
    ris+=1.80
    compresa="compresa la rilegatura" 
else:
    compresa=" "
    


if copie >= 1 and copie<=19:
    ris=ris+=copie*0.10
    print(f"Gentile Sig. {nome} il suo preventivo è di {ris:.2f} euro {compresa}")
elif copie >= 20 and copie<=100:
    ris=ris+=copie*0.08
    print(f"Gentile Sig. {nome} il suo preventivo è di {ris:.2f} euro {compresa}")
elif copie >100:
    ris=ris+= copie*0.05
    print(f"Gentile Sig. {nome} il suo preventivo è di {ris:.2f} euro {compresa}")
else:
    print("ERRORE minimo una copia")