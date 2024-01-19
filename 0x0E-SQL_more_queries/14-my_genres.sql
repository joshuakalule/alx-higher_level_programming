-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
	SELECT g.name FROM tv_genres as g
INNER JOIN tv_show_genres as sg
		ON g.id = sg.genre_id
INNER JOIN tv_shows as s
		ON s.id = sg.show_id
	 WHERE s.title = 'Dexter'
  ORDER BY g.name ASC;
