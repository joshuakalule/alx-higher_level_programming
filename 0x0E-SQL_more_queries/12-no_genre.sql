-- lists all shows contained in hbtn_0d_tvshows without a genre linked
	SELECT s.title, sg.genre_id
  	  FROM tv_shows AS s
 LEFT JOIN tv_show_genres AS sg
     	ON s.id = sg.show_id
	 WHERE sg.show_id IS NULL
  ORDER BY s.title ASC, sg.genre_id ASC;
