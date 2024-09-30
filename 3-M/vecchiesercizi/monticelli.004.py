ore = int(input("ore"))
costo=0
if ore>24:
    print ("non valido")
else:
    if ore<=6:
        if ore>=1:
            costo=costo+1.5
        if ore>1 and ore<5:
            costo=costo+((ore-1))
        if ore>4 and ore<=6:
            costo=costo+((ore-4)*0.5)
    else:
        costo=6

print(f"costo={costo}")
