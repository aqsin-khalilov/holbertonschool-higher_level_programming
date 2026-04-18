-- List all records with a name
-- This script lists records with score and name, ordered by score, excluding rows without names
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != "" ORDER BY score DESC;
