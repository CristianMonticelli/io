from math import sqrt
def my_input() -> list[int]:
    a = int(input('a'))
    b = int(input('b'))
    c = int(input('c'))
    return [a,b,c]

def calc(a: int,b: int,c: int) -> float | None:
    delta = b*b-4*a*c
    return delta
    
        
    

def variabili(a,b,delta) -> list[float]:
    if delta<0:
        return None
    elif delta==0:
        x1=(-b)/(a*2)
        x2==x1
        return x1,x2
    else:
        x1 = (-b + (delta**0.5))/(a*2)
        x2 = (-b - (delta**0.5))/(a*2)
        return[x1,x2]


def my_output(ris_finale : list[float]):
    for i in ris_finale:
        print(i)

x,y,z = my_input()
ris = calc(x,y,z)
ris_finale = variabili(ris)
print(ris)
print(ris_finale)

