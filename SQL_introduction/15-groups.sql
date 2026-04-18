-- List the number of records with the same score
-- This script groups records by score and counts them, sorted by count
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
