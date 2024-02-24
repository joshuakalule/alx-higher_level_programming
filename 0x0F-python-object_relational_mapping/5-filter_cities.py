#!/usr/bin/python3
"""Lists all cities from named state"""
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
              SELECT cities.name
              FROM cities INNER JOIN states
                ON cities.state_id = states.id
              WHERE states.name = %s
              ORDER BY cities.id ASC;
              """, (sys.argv[4],))

    cities = list()
    for row in c.fetchall():
        if (len(row) >= 1):
            cities.append(row[0])
    print(", ".join(cities))

    c.close()
    db.close()
