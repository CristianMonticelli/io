import os

contenuto = ''


with open(f'monticelli_011.py', 'r') as file:
    # Leggi tutto il contenuto del file
    righe = file.readlines()

print(type(righe[0]))
for riga in righe:
    if 'class ' in riga:
        testo_modificato = riga.replace(":", "").strip()
        if '(' in testo_modificato:
            inizio = testo_modificato.find("(")
            fine = testo_modificato.find(")", inizio)

            if inizio != -1 and fine != -1:
                # Estrai il testo tra le parentesi
                testo_estratto = testo_modificato[inizio + 1:fine].strip()
                testo_modificato =testo_modificato.replace(testo_estratto, "").strip()
                testo_modificato =testo_modificato.replace('()', "").strip()
            

        contenuto += f'{testo_modificato}'+'{'

    if 'def __init__(' in riga:
        testo_modificato = riga.replace("def __init__", "").strip()
        testo_modificato = testo_modificato.replace('self,', "").strip()
        testo_modificato = testo_modificato.replace('):', "").strip()

#for riga in righe:
#    print(riga.strip())

with open(f'monticelli_011.wsd', 'a') as f:
    f.write(contenuto)
    


