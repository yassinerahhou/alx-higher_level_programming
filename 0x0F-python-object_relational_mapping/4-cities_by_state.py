#!/usr/bin/python3
"""List All states inside hbtn_0e_0_usa db """

import MySQLdb
import sys


def myfun():
    ar = sys.argv
    db = MySQLdb.connect(host='localhost',
                         user=ar[1],
                         passwd=ar[2],
                         db=ar[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("""SELECT t2.id, t2.name, t1.name
                    FROM cities AS t2
                    JOIN states as t1
                    ON t1.id = t2.state_id ORDER BY id ASC""")

    result = cur.fetchall()
    for city in result:
        print(city)

    # cur.close()
    db.close()

if __name__ == "__main__":
    myfun()
