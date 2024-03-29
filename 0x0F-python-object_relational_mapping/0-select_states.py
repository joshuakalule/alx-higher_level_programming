#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) < 3:
        exit()

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    c = db.cursor()

    c.execute("""
                      SELECT *
                      FROM states
                      ORDER BY 'states.id' ASC
                      """)

    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
