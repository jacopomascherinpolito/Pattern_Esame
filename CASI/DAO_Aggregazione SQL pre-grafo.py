

SELECT a1.ActorID, a2.ActorID,
       -- Conto quanti film Commedia hanno in comune
       SUM(CASE WHEN genre = 'Comedy' THEN 1 ELSE 0 END) as n_comedy,
       -- Conto quanti film Drammatici hanno in comune
       SUM(CASE WHEN genre = 'Drama' THEN 1 ELSE 0 END) as n_drama
FROM movies m1, movies m2, ...
WHERE ...
GROUP BY a1.ActorID, a2.ActorID
HAVING n_comedy >= 3 AND n_drama >= 2