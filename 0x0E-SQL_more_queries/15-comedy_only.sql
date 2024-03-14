-- Use the database
USE hbtn_0d_tvshows;

-- Get the id of Comedy from the genres table
SET @comedy_id = (SELECT id FROM genres WHERE name = 'Comedy');

-- List all Comedy shows
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = @comedy_id
ORDER BY tv_shows.title;
