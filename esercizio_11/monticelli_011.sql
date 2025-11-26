SELECT A.region, H.denomination, B.beekeeper_name
FROM Production as P
JOIN Apiary as A
ON P.apiary_code = A.code
JOIN Beekeeper as B
ON A.beekeeper_id = B.id
JOIN Honey as H
ON P.honey_id = H.id
WHERE H.denomination LIKE '%DOP%';

SELECT region, COUNT(*) as numeroApiari
FROM Apiary
GROUP BY region;

SELECT T.denomination, sum(*) as quantitaTipologia
FROM Production as P
JOIN Honey as H
ON P.honey_id = H.id
JOIN Typologi as T
ON H.typology_id = T.id
GROUP BY T.denomination 