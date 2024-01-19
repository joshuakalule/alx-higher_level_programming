-- lists all genres from hbtn_0d_tvshows
-- displays the number of shows linked to each
	SELECT g.name as genre, COUNT(sg.genre_id) as number_of_shows
      FROM tv_genres as g
INNER JOIN tv_show_genres as sg
		ON g.id = sg.genre_id
  GROUP BY g.id
  ORDER BY number_of_shows DESC;
