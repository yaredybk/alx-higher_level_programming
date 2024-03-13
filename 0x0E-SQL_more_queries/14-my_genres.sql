-- lists all genres of the show Dexter.
--
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tg.name AS name
FROM tv_show_genres tsg
JOIN tv_genres tg
ON tg.id = tsg.genre_id
JOIN tv_shows ts
ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter';
