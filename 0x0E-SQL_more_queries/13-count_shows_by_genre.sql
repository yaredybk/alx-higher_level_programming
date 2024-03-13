-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- 
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
SELECT tg.name AS genre, COUNT(tsg.genre_id) AS number_of_shows
FROM tv_show_genres tsg
JOIN tv_genres tg
ON tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC
