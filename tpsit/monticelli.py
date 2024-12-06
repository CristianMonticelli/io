import os
import multiprocessing
def calcolaX():
    print("elab. parallela x=5+3")
    x = 5 + 3
    return x

def calcolaY():
    print("elab. parallela y=4-2")
    y = 4-2
    return y

if __name__ == "__main__":
    pid = os.fork()
    if pid == 0:
        print("sono il figlio")
        x = calcolaX()
        os._exit(x)
    else:
        print("sono il padre")
        y = calcolaY()
        os._exit(y)

pid, status = os.wait()

x = os.WEIXSTATUS(status)
y = os.WEIXSTATUS(status)

p = x*y
print(f'p ={p}')