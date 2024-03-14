-- Use the database
USE hbtn_0d_usa;

-- Get the id of California from the states table
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- List all cities in California
SELECT * FROM cities WHERE state_id = @california_id ORDER BY id;
