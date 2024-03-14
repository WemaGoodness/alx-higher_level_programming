-- This script lists all records of the table second_table, ordered by score in descending order, and does not list rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;
