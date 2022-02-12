import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

cnx = mysql.connector.connect(user="dalek", password="3637",
                        host="127.0.0.1",
                        database='Scouting')

cursor = cnx.cursor()


cursor.close()
cnx.close()