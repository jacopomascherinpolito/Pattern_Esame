# Pattern: Recuperare archi unici indipendentemente da come sono scritti nel DB
# utile per grafi non orientati

query = """
SELECT t1.id AS u, t2.id AS v, COUNT(*) as peso
FROM tabella t1, tabella t2
WHERE ...condizioni...
AND t1.id < t2.id  
GROUP BY t1.id, t2.id
"""