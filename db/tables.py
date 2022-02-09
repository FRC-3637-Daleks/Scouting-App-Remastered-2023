from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Scouting'

TABLES = {}
TABLES['Scouting'] = (
    "CREATE TABLE `Auton` ("
    "`Team` VARCHAR(10) NOT NULL, "
    "`High` int NOT NULL, "
    "`Low` int NOT NULL, "
    "`Missed` int NOT NULL, "
    "`Off_Platform` VARCHAR(1) NOT NULL, "
    "`Basketball_Shots_Made` int NOT NULL, "
)

TABLES['Teleop'] = (
    "CREATE TABLE `Teleop` ("
    "`Team` VARCHAR(10) NOT NULL, "
    "`High` int NOT NULL, "
    "`Low` int NOT NULL, "
    "`Missed` int NOT NULL, "
    "`Burst` int NOT NULL, "
    "`Launchpad` VARCHAR(1) NOT NULL, "
)

TABLES['Defense'] = (
    "CREATE TABLE `Defense` ("
    "`Team` VARCHAR(10) NOT NULL, "
    "`Blocked` VARCHAR(1) NOT NULL, "
    "`Held_balls` VARCHAR(1) NOT NULL, "
)

TABLES['Endgame'] = (
    "CREATE TABLE `Endgame` ("
    "`Team` VARCHAR(10) NOT NULL, "
    "`Attempted_Climb` VARCHAR(1) NOT NULL, "
    "`Success_Tier` int NOT NULL, "
    "`Prepared` VARCHAR(1) NOT NULL, "
    "`Climbing_Seconds` int NOT NULL, "
)

TABLES['Comments'] = (
    "CREATE TABLE `Comments` ("
    "`Team` VARCHAR(10) NOT NULL, "
    "`Insert_Comments` MEDIUMTEXT, "
)