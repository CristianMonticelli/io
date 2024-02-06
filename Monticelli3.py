#1 creo un dizionario di liste per le attivita' della settimana
attivita_pianificate={
    "lunedi'":['lavoro'],
    "martedi'":['lavoro','shopping'],
    "mercoledi'":['allenamento','ripetizioni latino'],
    "giovedi'":['pranzo di lavoro','lavoro'],
    "venerdi'":['ripetizioni latino'],
    "sabato":['allenamento'],
    "domenica":['messa']
    }
#2 stampo i giorni con le rispettive attivita'
for i,j in attivita_pianificate.items():
    print(f"{i}:{j}")
print('----------')
#3 aggiungo un attivita' a sabato
attivita_pianificate['sabato'].append('escursione')
#4 ripeto il due con un'attivita' in piu'
for i,j in attivita_pianificate.items():
    print(f"{i}:{j}")
print('----------')