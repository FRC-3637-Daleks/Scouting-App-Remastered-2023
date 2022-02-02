import mysql.connector
from mysql.connector import (connection)

cnx = mysql.connector.connect(user="test", password="3637",
                            host="127.0.0.1",
                            database="mysql")
cnx.close()
