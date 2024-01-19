-- lists all shows without the genre Comedy
  SELECT s.title
    FROM tv_shows AS s
   WHERE s.id NOT IN (
	         SELECT sg.show_id
	           FROM tv_show_genres AS sg
	   	 INNER JOIN tv_genres AS g
	             ON g.id = sg.genre_id
	          WHERE g.name = 'Comedy')
ORDER BY s.title;
