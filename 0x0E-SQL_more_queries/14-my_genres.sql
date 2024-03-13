-- lists all genres of the show Dexter.
--
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tg.name AS name
FROM tv_show_genres tsg
JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE tsg.show_id = (
	SELECT id
	FROM tv_shows
	WHERE title = 'Dexter'
)
