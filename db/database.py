#!/usr/bin/python3

print ("Content-type: text/html\r\n\r\n")
print ("<h1>Redirecting...</h1>")
# change redirect url to current ip address of server running
redirectURL = "/display"
# the content 3 is how many seconds that page should last
print('    <meta http-equiv="refresh" content="3;url='+str(redirectURL)+'" />') 


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

#get color
TC=data.getvalue('teamColor')

TEAM=data.getvalue('teamId')
print ("<p>The team number is %s</p>" % TEAM)

#get match number
MN=data.getvalue('matchNumber')

#auton high cube/cones placed
AHCP=data.getvalue('AHCP')
#auton mid cube/cones placed
AMCP=data.getvalue('AMCP')
#auton low cube/cones placed
ALCP=data.getvalue('ALCP')
#this one is for on platform, radio buttons
AP=data.getvalue('autonPlatform')
#auton Out of Community radio buttons
AOC=data.getvalue('autonOutOfComminity')

#teleop
#teleop robot move, radio buttons
TM=data.getvalue('teleopMove')
#teleop high cube/cones placed
THCP=data.getvalue('THCP')
#teleop mid cube/cones placed
TMCP=data.getvalue('TMCP')
#teleop low cube/cones placed
TLCP=data.getvalue('TLCP')


#Endgame charge status, radio buttons 
ECS =data.getvalue('endgameChargeStatus')
# Did they win? radio buttons
WIN = data.getvalue('endgameWin')

# defense attempted to block others, radio buttons
DAB = data.getvalue('defenseAttemptedBlock')

#comments
COMMENTS = data.getvalue('comments')

#pit scouting stuff
PIT_ID = data.getvalue('PITID')
WEIGHT = data.getvalue('PSW')
LENGTH = data.getvalue('PSL')
WIDTH = data.getvalue('PSWD')
INTAKE_DESC = data.getvalue('PSID')
SCORING_DESC = data.getvalue('PSSD')
DRIVE_DESC = data.getvalue('PSDD')
AUTON_DESC = data.getvalue('PSAD')
DEFENSE = data.getvalue('DEF')
TRIPLE_BALANCE = data.getvalue('TB')
PREFERRED_PIECE = data.getvalue('PP')
COMMENTS_DESC = data.getvalue('PSCD')
PHOTO = data.getvalue('PSP')


try:
 
    add_Auton = "INSERT INTO Auton (Team, Match_Number, Color, High, Mid, Low, Left_Platform, Out_of_Community) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(add_Auton, (TEAM, MN, TC, AHCP, AMCP, ALCP, AP, AOC))

except:
    print ("<p>Error adding Auton data</p>")

finally:

    try:

        add_Teleop = "INSERT INTO Teleop (Team, Match_Number, Color, Moved, High, Mid, Low) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(add_Teleop, (TEAM, MN, TC, TM, THCP, TMCP, TLCP))

    except:
        print ("<p>Error adding Teleop data</p>")
    
    finally:

        try:

            add_Endgame = "INSERT INTO Endgame (Team, Match_Number, Color, Charge_Status, Win) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(add_Endgame, (TEAM, MN, TC, ECS, WIN))

        except:
            print ("<p>Error adding Endgame data</p>")

        finally:

            try:

                add_Defense = "INSERT INTO Defense (Team, Match_Number, Color, Blocked_Others) VALUES (%s, %s, %s, %s)"
                cursor.execute(add_Defense, (TEAM, MN, TC, DAB))

            except:
                print ("<p>Error adding Defense data</p>")

            finally:
                
                try:

                    add_Comments = "INSERT INTO Comments (Team, Match_Number, Color, Insert_Comments) VALUES (%s, %s, %s, %s)"
                    cursor.execute(add_Comments, (TEAM, MN, TC, COMMENTS))

                except:
                    print ("<p>Error adding Comments data</p>")

                finally:

                    try:
                        add_Pit = "INSERT INTO Pit (Pit_Id, Length, Width, Weight, Intake, Scoring, Drivebase, Auton, Defense, Triple_Balance, Preferred_Piece, Comments, Photo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(add_Pit, (PIT_ID, LENGTH, WIDTH, WEIGHT, INTAKE_DESC, SCORING_DESC, DRIVE_DESC, AUTON_DESC, DEFENSE, TRIPLE_BALANCE, PREFERRED_PIECE, COMMENTS_DESC, PHOTO))
                    
                    except:
                        print("<p>Error adding Pit data</p>")
                    
                    finally:
                        print("<p>DONE :D</p>")
                        cnx.commit()
                        cursor.close()
                        cnx.close()