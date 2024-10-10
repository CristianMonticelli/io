import os
import json
my_list_numeri = []


with open('my_list_numeri.json', 'r') as f:
    my_list_numeri = json.load(f)

n = my_list_numeri[-1] +1
my_list_numeri.append(n)
with open('my_list_numeri.json', 'w') as f:
    json.dump(my_list_numeri, f)

os.mkdir(f'esercizio {n}')

with open(f'esercizio {n}/monticelli_00{str(n)}.py', 'w') as f:
    f.write('class ___:')

with open(f'esercizio {n}/monticelli_00{str(n)}.wsd', 'w') as f:
    f.write(f'''@startuml es{n}

    
    @enduml''')