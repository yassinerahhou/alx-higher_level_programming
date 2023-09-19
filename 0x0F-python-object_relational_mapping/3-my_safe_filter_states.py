#!/usr/bin/python3

import mysql.connector
import sys 
from sys import argv
if __name__ == "__main__":
    # this block will only execute when the script is run directly.
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
     # name_search = sys.argv[4]
    # This block establishes a connection to the MySQL database.
    #  It uses the MySQLdb.connect() method and provides the database connection details, including host, username, password, database name, and port.
    #  This connection object is stored in the db variable.

conn = MySQLdb.connect(host="localhost", 
                       port=3306,
                        user=username ,
                        passwd=password,
                        db=db_name         
                        )
cur = conn.cursor()
query_s ="SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cur.execute(query_s, (argv[4],))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
