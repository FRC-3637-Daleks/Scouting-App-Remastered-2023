from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Scouting'

TABLES = {}
TABLES['Auton'] = (
    "CREATE TABLE `Auton` ("
    "   `Team` VARCHAR(10) NOT NULL,"
    "   `High` int NOT NULL,"
    "   `Low` int NOT NULL,"
    "   `Missed` int NOT NULL,"
    "   `Off_Platform` VARCHAR(1) NOT NULL,"
    "   `Basketball_Shots_Made` int NOT NULL,"
    "   PRIMARY KEY (`Team`)"
    ")"
)

TABLES['Teleop'] = (
    "CREATE TABLE `Teleop` ("
    "   `Team` VARCHAR(10) NOT NULL,"
    "   `High` int NOT NULL,"
    "   `Low` int NOT NULL,"
    "   `Missed` int NOT NULL,"
    "   `Burst` int NOT NULL,"
    "   `Launchpad` VARCHAR(1) NOT NULL,"
    "   PRIMARY KEY (`Team`)"
    ")"
)

TABLES['Defense'] = (
    "CREATE TABLE `Defense` ("
    "   `Team` VARCHAR(10) NOT NULL,"
    "   `Blocked` VARCHAR(1) NOT NULL,"
    "   `Held_balls` VARCHAR(1) NOT NULL,"
    "   PRIMARY KEY (`Team`)"
    ")"
)

TABLES['Endgame'] = (
    "CREATE TABLE `Endgame` ("
    "   `Team` VARCHAR(10) NOT NULL,"
    "   `Attempted_Climb` VARCHAR(1) NOT NULL,"
    "   `Success_Tier` int NOT NULL,"
    "   `Prepared` VARCHAR(1) NOT NULL,"
    "   `Climbing_Seconds` int NOT NULL,"
    "   PRIMARY KEY (`Team`)"    
    ")"
)

TABLES['Comments'] = (
    "CREATE TABLE `Comments` ("
    "   `Team` VARCHAR(10) NOT NULL,"
    "   `Insert_Comments` MEDIUMTEXT,"
    "   PRIMARY KEY (`Team`)"
    ")"
)

cnx = mysql.connector.connect(user="dalek", password="3637",
                        host="127.0.0.1",
                        database='Scouting')

cursor = cnx.cursor()

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("That table already exists!")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()