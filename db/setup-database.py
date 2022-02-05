import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user="dalek", password="3637",
                            host="127.0.0.1")

    mycursor = cnx.cursor()
    mycursor.execute("CREATE DATABASE Scouting")
    mycursor.execute("SHOW DATABASES")
    
    for x in mycursor:
        print(x)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
