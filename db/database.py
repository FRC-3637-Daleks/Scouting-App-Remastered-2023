#!/usr/bin/python3

print ("Content-type: text/plain\r\n\r\n")
print ("Hello World!")


import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode
import requests
import cgi


#setup connector
cnx = mysql.connector.connect(user="dalek", password="3637",
                        host="127.0.0.1",
                        database='Scouting')

#setup cursor to execute queries
cursor = cnx.cursor()

#get form data from html form and store in variables for use in sql query
data=cgi.FieldStorage()
newData=str(data)
print ("<p>", newData, "</p>")
#get team number from form
TEAM=data.getvalue('teamId')
print ("<p>The team number is %s</p>" % TEAM)

#auton high shots
AHS=data.getvalue('AHS')
#auton low shots
ALS=data.getvalue('ALS')
#auton balls missed
ABM=data.getvalue('ABM')
#this one is for Off_Platform, radio buttons
AP=data.getvalue('autonPlatform')
#auton basketball radio buttons
AB=data.getvalue('autonBasketball')

#teleop
#teleop high shots
THS=data.getvalue('THS')
#teleop low shots
TLS=data.getvalue('TLS')
#teleop balls missed
TBM=data.getvalue('TBM')
#teleop burst shots
TBS=data.getvalue('TBS')
#teleop launchpad radio buttons
TLP=data.getvalue('teleopLaunchpad')


#Endgame Climb, radio buttons 
EAC =data.getvalue('endgameAttemptedClimb')
#endgame climb tier input
ECT = data.getvalue('ECT')
# Prepared in Endgame, radio buttons
EPE = data.getvalue('endgamePrepared')
# Climb faster than x seconds, radio buttons
ECXS = data.getvalue('endgameClimbTime')

# defense attempted to block others, radio buttons
DAB = data.getvalue('defenseAttemptedBlock')
# defense held balls, radio buttons
DHB = data.getvalue('defenseHeldBalls')

#comments
COMMENTS = data.getvalue('comments')


try:
 
    add_Auton = "INSERT INTO Auton (Team, High, Low, Missed, Off_Platform, Basketball_Shots_Made) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(add_Auton, (TEAM, AHS, ALS, ABM, AP, AB))

except:
    print ("<p>Error adding Auton data</p>")

finally:

    try:

        add_Teleop = "INSERT INTO Teleop (Team, High, Low, Missed, Burst, Launchpad) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(add_Teleop, (TEAM, THS, TLS, TBM, TBS, TLP))

    except:
        print ("<p>Error adding Teleop data</p>")
    
    finally:

        try:

            add_Endgame = "INSERT INTO Endgame (Team, Attempted_Climb, Success_Tier, Prepared, Climbing_Seconds) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(add_Endgame, (TEAM, EAC, ECT, EPE, ECXS))

        except:
            print ("<p>Error adding Endgame data</p>")

        finally:

            try:

                add_Defense = "INSERT INTO Defense (Team, Blocked, Held_balls) VALUES (%s, %s, %s)"
                cursor.execute(add_Defense, (TEAM, DAB, DHB))

            except:
                print ("<p>Error adding Defense data</p>")

            finally:
                
                try:

                    add_Comments = "INSERT INTO Comments (Team, Insert_Comments) VALUES (%s, %s)"
                    cursor.execute(add_Comments, (TEAM, COMMENTS))

                except:
                    print ("<p>Error adding Comments data</p>")

                finally:

                    print("IT NO WORKY")
                    cnx.commit()
                    cursor.commit()
                    cursor.close()
                    cnx.close()