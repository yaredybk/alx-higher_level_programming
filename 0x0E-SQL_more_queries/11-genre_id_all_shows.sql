-- lists all shows contained in the database hbtn_0d_tvshows.
--
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT ts.title AS title, tsg.genre_id AS genre_id
FROM tv_show_genres tsg
RIGHT JOIN tv_shows ts
ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id
