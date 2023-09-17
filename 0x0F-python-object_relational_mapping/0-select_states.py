#!/usr/bin/python3
"""print all states from hbtn_0e_0_usa database"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    sync = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name)
    cursor = sync.cursor()

    sql_coo = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(sql_coo)

    lines = cursor.fetchall()

    for line in lines:
        print(line)

    sync.close()
