-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- 
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
SELECT ts.title AS title, SUM(tsr.rate) AS rating
FROM tv_show_ratings tsr
JOIN tv_shows ts
ON tsr.show_id = ts.id
GROUP BY ts.title
ORDER BY rating DESC;
