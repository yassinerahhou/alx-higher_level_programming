#!/usr/bin/python3
"""displays wheratches"""
import MySQLdb
import sys


def detectme():

    argvv = sys.argv
    db= MySQLdb.connect(user=argvv[1],
                        host='localhost',
                        port=3306,
                        passwd=argvv[2],
                        db=argvv[3])

    cur = db.cursor()
    cur.execute("""SELECT t2.id, t2.name, t1.name
                    FROM cities AS t2
                    JOIN states as t1
                    ON t1.id = t2.state_id ORDER BY id ASC""")
    result = cur.fetchall()
    for i in result:
        print(i)
    db.close()


if __name__ == "__main__":
    detectme()
