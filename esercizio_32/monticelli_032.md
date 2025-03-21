<!-- Piattaforma di Streaming Video
Immagina una piattaforma dove gli 'utenti' possono 'guardare video, creare playlist e seguire i loro canali preferiti'.

Ogni utente ha un suo profilo con nome, email e password, e può creare diverse playlist per organizzare i video che preferisce. L'utente ha anche un abbonamento che gli permette di accedere a contenuti esclusivi.

I video sono il cuore della piattaforma: hanno un titolo, una descrizione, un URL per lo streaming e una durata. Sotto ogni video, gli utenti possono lasciare commenti.

Le playlist sono raccolte di video create dagli utenti. Ogni playlist ha un nome e un creatore, e contiene una lista di video.

Ogni abbonamento ha un tipo, un prezzo e una data di inizio e fine.

I commenti sono messaggi lasciati dagli utenti sotto i video dopo averlo guardato. Ogni commento ha un autore, un testo, una data di pubblicazione ed è associato a uno specifico video.

In sintesi, la piattaforma gestisce utenti, video, playlist, abbonamenti e commenti, permettendo agli utenti di interagire tra loro e con i contenuti. -->

```mermaid
classDiagram
    class Utente {
        +nome: str
        +email: str
        +password: str

        +cronologia: list[Video]
        +playlist: list[Playlist]
        +abbonamenti: list[Abbonamento]
        +commenti: list[Commento]
    }

    class Video {
        +titolo: str
        +descrizione: str
        +url: str
        +durata: float
        +canale: Canale
        
        +commenti: list[Commanto]
    }
%% Le playlist sono raccolte di video create dagli utenti. Ogni playlist ha un nome e un creatore, e contiene una lista di video.
    class Playlist {
        +nome: str
        +creatore: Utente

        +video: list[Video]

    
    }

%% Ogni abbonamento ha un tipo, un prezzo e una data di inizio e fine.
    class Abbonamento {
        tipo: str
        prezzo: float
        dataInizio: date
        dataFine: date

    }

%% I commenti sono messaggi lasciati dagli utenti sotto i video dopo averlo guardato. Ogni commento ha un autore, un testo, una data di pubblicazione ed è associato a uno specifico video.

    class Commento {
        +autore: Utente
        +testo: str
        +dataPubblicazione: date
        +videoAssociato: Video
    
    }

%% In sintesi, la piattaforma gestisce utenti, video, playlist, abbonamenti e commenti, permettendo agli utenti di interagire tra loro e con i contenuti.

    

    class Canale{
        +nome: str
        +proprietrio: Utente
        +followers: list[Utente]
        +videoPubblicati: list[Video]
    
    }
    Playlist "*" --> "*" Video : contiene
    Utente "1" --> "*" Playlist : crea
    Utente "1" --> "1" Abbonamento : effettua
    Utente "1" --> "*" Commento : scrive
    Commento "*" --> "1" Video : sotto
    Utente "1" --> "1" Canale : crea
    Utente "*" <-- "*" Canale : seguito
    Video "1" <-- "1" Canale : pubblica
    Utente "*" --> "*" Video : vede

    %% class Piattaforma{
    %%     +nome: str

    %%     +utenti: list[Utente]
    %%     +video: list[Video]
    %%     +playlist: list[Playlist]
    %%     +abbonamenti: list[Abbonamento]
    %%     +commenti: list[Commento]

    %% }
    %% Piattaforma "1" --> "*" Playlist : gestisce
    %% Piattaforma "1" --> "*" Utente : gestisce
    %% Piattaforma "1" --> "*" Commento : gestisce
    %% Piattaforma "1" --> "*" Video : gestisce
    %% Piattaforma "1" --> "*" Abbonamento : gestisce
    %% Piattaforma "1" --> "*" Canale : gestisce
```