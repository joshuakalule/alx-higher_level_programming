-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
   SELECT g.name, SUM(r.rate) AS rating
     FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg
       ON sg.genre_id = g.id
LEFT JOIN tv_shows AS s
       ON sg.show_id = s.id
LEFT JOIN tv_show_ratings AS r
       ON s.id = r.show_id
 GROUP BY g.name
 ORDER BY rating DESC;
