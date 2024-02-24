#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""
import MySQLdb
import sys

if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit()

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    c = db.cursor()

    c.execute("""
              SELECT cities.id, cities.name, states.name
              FROM cities INNER JOIN states
                ON cities.state_id = states.id
              ORDER BY cities.id ASC;
              """)
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
