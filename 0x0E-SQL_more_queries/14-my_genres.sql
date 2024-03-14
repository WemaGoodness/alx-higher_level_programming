-- Use the database
USE hbtn_0d_tvshows;

-- Get the id of Dexter from the tv_shows table
SET @dexter_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');

-- List all genres of Dexter
SELECT genres.name
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = @dexter_id
ORDER BY genres.name;
