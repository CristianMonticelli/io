import os


n = 1
while True:
    if os.path.exists(f'esercizio_{n}'):
        print(f"Il file '{n}' esiste.")
        n+=1
    else:
        print(f"Il file '{n}' non esiste.")
        break

os.mkdir(f'esercizio_{n}')

with open(f'esercizio_{n}/monticelli_0{str(n)}.py', 'w') as f:
    f.write('class ___:')

with open(f'esercizio_{n}/monticelli_0{str(n)}.wsd', 'w') as f:
    f.write(f'''@startuml es{n}

    
@enduml''')

