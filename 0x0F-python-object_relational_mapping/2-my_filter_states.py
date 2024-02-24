#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) < 3:
        exit()

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)

    c = db.cursor()

    c.execute("""
              SELECT *
              FROM states
              WHERE states.name = '{}'
              ORDER BY states.id ASC;
              """.format(sys.argv[4]))

    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
