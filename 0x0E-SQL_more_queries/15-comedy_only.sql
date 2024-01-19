-- lists all Comedy shows in the database hbtn_0d_tvshows
	SELECT s.title as title
	  FROM tv_shows as s
INNER JOIN tv_show_genres as sg
        ON s.id = sg.show_id
INNER JOIN tv_genres as g
		ON sg.genre_id = g.id
	 WHERE g.name = 'Comedy'
  ORDER BY s.title ASC;
