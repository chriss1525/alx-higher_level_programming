-- list all records of second_table
-- records are orderd by score
SELECT `score`,
    `name`
FROM second_table
WHERE score >= 10
ORDER BY `score` DESC;