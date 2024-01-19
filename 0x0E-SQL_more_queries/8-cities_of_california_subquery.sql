-- lists all the cities of California that can be found hbtn_0d_usa
 SELECT id, name
   FROM cities
  WHERE cities.state_id = (
		SELECT id
		  FROM states
		 WHERE name = 'California');
