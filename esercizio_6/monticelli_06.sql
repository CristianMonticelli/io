--1. Elenco di tutti i libri con titolo, anno e nome dell'autore (usa JOIN).
SELECT L.titolo, L.anno, A.nome, A.cognome
FROM LIBRI as L
JOIN AUTORI as A 
ON L.autore_id = A.id;

--2. Elenco di tutti i prestiti con titolo del libro, utente e data di prestito (usa JOIN).
SELECT L.titolo, P.utente, P.data_prestito
FROM PRESTITI as P
JOIN LIBRI as L
ON P.libro_id = L.id;

--3. Libri pubblicati dopo il 2020.
SELECT titolo, anno, genere
FROM LIBRI
WHERE anno > 2020;

--4. Numero di prestiti per ciascun utente (usa GROUP BY).
SELECT utente, COUNT(*) AS numero_prestiti
FROM PRESTITI
GROUP BY utente;

--5. Libri ordinati per genere e poi per anno (usa ORDER BY multiplo).
SELECT genere, titolo, anno
FROM LIBRI
ORDER BY genere, anno;

--6. Prestiti restituiti (dove data_restituzione non è NULL).
SELECT L.titolo, P.utente, P.data_restituzione
FROM PRESTITI AS P
JOIN LIBRI AS L
ON P.libro_id = L.id
WHERE P.data_restituzione IS NOT NULL;

--7. Autori e numero di libri, inclusi quelli senza libri (usa [LEFT JOIN](https://www.w3schools.com/sql/sql_join_left.asp) e GROUP BY).
SELECT A.nome, A.cognome, COUNT(L.id) AS numero_libri
FROM AUTORI AS A
LEFT JOIN LIBRI AS L
ON A.id = L.autore_id
GROUP BY A.id;