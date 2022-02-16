#!/usr/bin/python3

print ("Content-type: text/html\n")
print ("Hello World!")

import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode
import requests
import cgi

cnx = mysql.connector.connect(user="dalek", password="3637",
                        host="127.0.0.1",
                        database='Scouting')

cursor = cnx.cursor()

data=cgi.FieldStorage()
AHS=data.getvalue('AHS')
ALS=data.getvalue('ALS')


sql = "INSERT INTO Auton (Team, High, Low, Missed, Off_Platform, Basketball_Shots_Made) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.execute(sql, ('3637', AHS, ALS, '0', '0', '0', '0'))

print(AHS)
print(ALS)

cursor.close()
cnx.close()