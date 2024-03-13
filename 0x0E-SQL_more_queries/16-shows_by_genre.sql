-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
--
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT ts.title AS title, tg.name AS name
FROM tv_show_genres tsg
RIGHT JOIN tv_shows ts
ON ts.id = tsg.show_id
JOIN tv_genres tg
ON tg.id = tsg.genre_id
ORDER BY ts.title, tg.name;
