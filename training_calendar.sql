SELECT sport, discipline, COUNT(*) AS count, SUM(distance) AS total, ROUND(AVG(distance), 1) AS average
FROM read_csv('/dev/stdin', header = true, auto_detect = false, columns = {'date': 'DATE', 'sport': 'VARCHAR', 'discipline': 'VARCHAR', 'distance': 'DECIMAL(4,1)'})
GROUP BY GROUPING SETS ((sport), (sport, discipline))
HAVING GROUPING(discipline) = 0 OR COUNT(DISTINCT discipline) > 1
ORDER BY sport, discipline
;