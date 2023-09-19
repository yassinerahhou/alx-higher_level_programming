#!/usr/bin/python3
"""List All states inside hbtn_0e_0_usa db """

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute(("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id"""))

    result = cur.fetchall()
    for city in result:
        print(city)

    cur.close()
    db.close()
