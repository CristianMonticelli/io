import threading
import os

# Vettore condiviso
vector = []

# Lock per sincronizzare l'accesso al vettore
lock = threading.Lock()
n = input('n')
def fill_odd_numbers():
    global vector
    
    global n
    
    for i in range(1, n, 2):
        with lock:
            vector.append(i)
        print(f"Added odd number: {i}")

def fill_even_numbers():
    global vector
    global n
    for i in range(0, n+1, 2):
        with lock:
            vector.append(i)
        print(f"Added even number: {i}")

if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=fill_odd_numbers, name='t1')
    t2 = threading.Thread(target=fill_even_numbers, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final vector:", vector)