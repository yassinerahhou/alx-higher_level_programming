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
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    result = cur.fetchall()
    for city in result:
        print(city)

    cur.close()
    db.close()
if __name__ == "__main__":
        myfun()

