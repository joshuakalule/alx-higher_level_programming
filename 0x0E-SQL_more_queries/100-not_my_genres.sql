-- list all genres not linked to the show Dexter
	SELECT g.name
      FROM tv_genres AS g
	 WHERE g.id NOT IN (
           SELECT sg.genre_id
	         FROM tv_show_genres AS sg
       INNER JOIN tv_shows AS s
  		       ON s.id = sg.show_id
		    WHERE s.title = 'Dexter')
  ORDER BY g.name ASC;
