import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin@123",
    database="r2schools")

print(mydb)
