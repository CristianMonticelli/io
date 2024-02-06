voto_1 = int(input("voto1"))
voto_2 =int( input("voto2"))
voto_3= int(input("voto3"))
voto_4 = int(input("voto4"))
voto_5 = int(input("voto5"))
valido_1=0
sufficente1=0
if voto_1>0 and voto_1<11 :
    valido_1=1
    if voto_1>5 and voto_1<11:
        sufficente1=1
    else:
        sufficente1=0


sufficente2=0
valido_2=0
if voto_2>0 and voto_2<11 :
    valido_2=1
    if voto_2>5 and voto_2<11:
        sufficente2=1
    else:
        sufficente2=0


sufficente3=0
valido_3=0
if voto_3>0 and voto_3<11 :
    valido_3=1
    if voto_3>5 and voto_3<11:
        sufficente3=1
    else:
        sufficente3=0


sufficente4=0
valido_4=0
if voto_4>0 and voto_4<11 :
    valido_4=1
    if voto_4>5 and voto_4<11:
        sufficente4=1
    else:
        sufficente4=0


sufficente5=0
valido_5=0
if voto_5>0 and voto_5<11 :
    valido_5=1
    if voto_5>5 and voto_5<11:
        sufficente5=1
    else:
        sufficente5=0

print("voti validi" + str(valido_5 + valido_1 + valido_2 + valido_4 + valido_3))
print(f"voti sufficenti  {sufficente1 +sufficente2+sufficente3+sufficente4+sufficente5}")
