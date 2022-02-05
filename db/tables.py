from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Scouting'

TABLES = {}
TABLES['scouting'] = (
    "CREATE TABLE 'auton' ("
    "   `high`"
)