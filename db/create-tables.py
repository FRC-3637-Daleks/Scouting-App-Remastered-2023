from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Scouting'

TABLES = {}
TABLES['Auton'] = (
    "CREATE TABLE `Auton` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1) DEFAULT 'X',"
    "   `High` int DEFAULT 0,"
    "   `Low` int DEFAULT 0,"
    "   `Missed` int DEFAULT 0,"
    "   `Off_Platform` VARCHAR(1) DEFAULT 'N',"
    "   `Basketball_Shots_Made` VARCHAR(1) DEFAULT 'N',"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

TABLES['Teleop'] = (
    "CREATE TABLE `Teleop` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1) DEFAULT 'X',"
    "   `Moved` VARCHAR(1) DEFAULT 'X',"
    "   `High` int DEFAULT 0,"
    "   `Low` int DEFAULT 0,"
    "   `Missed` int DEFAULT 0,"
    "   `Burst` int DEFAULT 0,"
    "   `Launchpad` VARCHAR(1) DEFAULT 'N',"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

TABLES['Defense'] = (
    "CREATE TABLE `Defense` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1) DEFAULT 'X',"
    "   `Blocked` VARCHAR(1) DEFAULT 'N',"
    "   `Held_balls` VARCHAR(1) DEFAULT 'N',"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

TABLES['Endgame'] = (
    "CREATE TABLE `Endgame` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1) DEFAULT 'X',"
    "   `Attempted_Climb` VARCHAR(1) DEFAULT 'N',"
    "   `Success_Tier` int DEFAULT 0,"
    "   `Prepared` VARCHAR(1) DEFAULT 'N',"
    "   `Climbing_Seconds` VARCHAR(1) DEFAULT 'N',"
    "   `Win` VARCHAR(4) DEFAULT 'X',"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

#todo: set max char of mediumtext in the index script

TABLES['Comments'] = (
    "CREATE TABLE `Comments` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1) DEFAULT 'X',"
    "   `Insert_Comments` MEDIUMTEXT,"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
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