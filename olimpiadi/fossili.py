a1=15
b1=20 
c1=7
a2=43
b2=500
c2 =30
inizio= 0
if a1>b1 and a1>c1:
    inizio=a1
if c1>b1 and c1>a1:
    inizio=c1
if b1>a1 and b1>c1:
    inizio=b1
fine=0
if a2<b2 and a2<c2:
    fine=a2
if c2<b2 and c2<a2:
    fine=c2
if b2 <a2 and b2<c2:
    fine=b2
t = fine-inizio
print(t)