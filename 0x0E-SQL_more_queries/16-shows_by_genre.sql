-- list all shows in database 'hbtn_0d_tvshows'
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
INNER JOIN tv_genres ON tv_genre.id='tv_show_genres.genre_id'
GROUP BY tv_genres.name ORDER BY number_shows DESC;
