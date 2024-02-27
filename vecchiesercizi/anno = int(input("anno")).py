anno = int(input("anno"))
if anno<2100 and anno>0:
    anno1=anno%4 
    anno2=anno%100
    if anno_1<4 and anno_2>100:
        print("bisestile")
    else:
        print("non bisestile")
else:
    print ("non bisestile")