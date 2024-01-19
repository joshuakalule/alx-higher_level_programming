-- lists all shows, and all genres linked to that show
	SELECT s.title, g.name
	  FROM tv_shows as s
 LEFT JOIN tv_show_genres as sg
	    ON s.id = sg.show_id
LEFT JOIN tv_genres as g
ON g.id = sg.genre_id
ORDER BY s.title, g.name;
