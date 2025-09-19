#Gestione di una libreria di film. Ogni film ha un titolo, un regista, un anno di uscita, 
# un genere (azione, commedia, drammatico, horror, documentario) e una valutazione (da 1 a 10). 
# Il sistema deve permettere di:
#Aggiungere nuovi film alla libreria.
#Cercare film per titolo o regista.
#Visualizzare tutti i film presenti nella libreria.
#Calcolare la valutazione media dei film.
#Il sistema deve includere due classi principali:
#: rappresenta un singolo film nella libreria.
#: gestisce i film e le operazioni associate.


#Crea relativo diagramma UML e codice.

class Libreria:
    def __init__(self,titolo):
        self.titolo = titolo
        self.film = []
    #Aggiungere nuovi film alla libreria.
    def aggiungi_film(self,nuovo_film):
        if nuovo_film not in self.film:
            self.film.append(nuovo_film)
            print('film aggiunto')
        else:
            print(f'film gia presente {nuovo_film}')
    
    def rimuovi_film(self,film_da_rimuovere):
        if film_da_rimuovere in self.film:
            self.film.remove(film_da_rimuovere)
            print('film tolto')
        else:
            print(f'film non presente {film_da_rimuovere}')
    
    #Cercare film per titolo o regista.
    def cerca_film(self,titolo,regista):
        film_stesso_regista_o_titolo = []
        if titolo != None:
            for t in self.film:
                if titolo == t.titolo:
                    film_stesso_regista_o_titolo.append(t)
        if regista != None:
            for r in self.film:
                
                if regista == r.regista:
                    film_stesso_regista_o_titolo.append(r)
        return film_stesso_regista_o_titolo
    #Visualizzare tutti i film presenti nella libreria.
    def visualizzare_tutti_film(self):
        for f in self.film:
            print(f)
    
    #Calcolare la valutazione media dei film.
    def valutazione_media_film(self):
        media = 0
        for f in self.film:
            media += f.valutazione
        media /= len(self.film)
        return f'media {media}'


        


class Film:
    def __init__(self,titolo,regista,anno,genere,valutazione):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere
        self.valutazione = valutazione
    def __str__(self):
        return f'titolo:{self.titolo} regista:{self.regista} anno:{self.anno} genere:{self.genere} valutazione:{self.valutazione} '

libreria = Libreria('Monsce')
film1 = Film('Titanic','James Cameron','1997','Romantico/Avventura',2)
film2 = Film('Robinson Crusoe','Rod Hardy','1997',' Avventura/Azione',4)
film3 = Film('La minaccia fantasma','George Lucas','1999','Sci-fi',9)
film4 = Film("L'Impero colpisce ancora",'George Lucas','1980','Sci-fi',8)
print('---------')
libreria.aggiungi_film(film1)
libreria.aggiungi_film(film2)
libreria.aggiungi_film(film3)
libreria.aggiungi_film(film4)


print('---------')
#libreria.rimuovi_film(film1)

lista_film = libreria.cerca_film(None,'George Lucas')
for f in lista_film:
    print(f)

print('---------')
libreria.visualizzare_tutti_film()

print('---------')
print(libreria.valutazione_media_film())