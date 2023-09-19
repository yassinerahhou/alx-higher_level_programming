#!/usr/bin/python3
"""List All states inside hbtn_0e_0_usa db """

import MySQLdb
import sys


if __name__ == "__main__":
    ar = sys.argv
    db = MySQLdb.connect(host='localhost',
                         user=ar[1],
                         passwd=ar[2],
                         db=ar[3],
                         port=3306)

    cur = db.cursor()
    ansr =  """SELECT c.name
                    FROM cities AS c
                    JOIN states AS s
                    ON c.state_id = s.id
                    WHERE BINARY s.name = %s
                    ORDER BY c.id ASC
                """
    cur.execute(ansr , (ar[4],))

    result = cur.fetchall()
        print(', '.join(tuple(row[0] for row in result)))
    # for city in result:
    #     print(city)

    # # cur.close()
    # db.close()
