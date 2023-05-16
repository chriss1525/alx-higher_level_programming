-- check similar scores
-- store by number of similar scores
SELECT score,
    COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;