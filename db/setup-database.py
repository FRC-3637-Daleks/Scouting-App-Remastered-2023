import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

cnx = mysql.connector.connect(user="test", password="3637",
                            host="127.0.0.1")

mycursor = cnx.cursor()
mycursor.execute("CREATE DATABASE scouting")
mycursor.execute("SHOW DATABASES")
    
for x in mycursor:
    print(x)

cnx.close()
