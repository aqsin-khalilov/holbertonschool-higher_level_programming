-- List records with score >= 10
-- This script lists records with score and name, ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
