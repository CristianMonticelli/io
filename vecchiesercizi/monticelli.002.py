anno = int(input("anno"))
if anno<2100 and anno>0:
 
    if anno%400==0:
        print("bisestile")
      
    elif anno%4==0 and anno%100!=0:
        print("bisestile")
       
    else:
     print ("non valido")

else:
    print("errore")

 