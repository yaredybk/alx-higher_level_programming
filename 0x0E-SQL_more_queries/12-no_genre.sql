-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- 
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT ts.title AS title, tsg.genre_id AS genre_id
FROM tv_show_genres tsg
RIGHT JOIN tv_shows ts
ON ts.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY ts.title, tsg.genre_id
