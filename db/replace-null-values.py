import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

cnx = mysql.connector.connect(user="dalek", password="3637",
                        host="127.0.0.1",
                        database='Scouting')

cursor = cnx.cursor()

# I know there is a better way but I don't care. probably concatonating it
# or something...

#sql queries
#auton
autonColor = "UPDATE Auton SET Color = 'X' WHERE Color IS NULL;"
autonHigh = "UPDATE Auton SET High = 0 WHERE High IS NULL;"
autonLow = "UPDATE Auton SET Low = 0 WHERE Low IS NULL;"
autonMissed = "UPDATE Auton SET Missed = 0 WHERE Missed IS NULL;"
autonOffPlatform = "UPDATE Auton SET Off_Platform = 'N' WHERE Off_Platform IS NULL;"
autonBasketballShots = "UPDATE Auton SET Basketball_Shots_Made = 'N' WHERE Basketball_Shots_Made IS NULL;"

#teleop
teleopColor = "UPDATE Teleop SET Color = 'X' WHERE Color IS NULL;"
teleopMoved = "UPDATE Teleop SET Moved = 'X' WHERE Moved IS NULL;"
teleopHigh = "UPDATE Teleop SET High = 0 WHERE High IS NULL;"
teleopLow = "UPDATE Teleop SET Low = 0 WHERE Low IS NULL;"
teleopMissed = "UPDATE Teleop SET Missed = 0 WHERE Missed IS NULL;"
teleopBurst = "UPDATE Teleop SET Burst = 0 WHERE Burst IS NULL;"
teleopLaunchpad = "UPDATE Teleop SET Launchpad = 0 WHERE Launchpad IS NULL;"

#endgame
endgameColor = "UPDATE Endgame SET Color = 'X' WHERE Color IS NULL;"
endgameClimb = "UPDATE Endgame SET Attempted_Climb = 'X' WHERE Attempted_Climb IS NULL;"
endgameSuccessTier = "UPDATE Endgame SET Success_Tier = 0 WHERE Success_Tier IS NULL;"
endgamePrepared = "UPDATE Endgame SET Prepared = 'X' WHERE Prepared IS NULL;"
endgameClimbingSeconds = "UPDATE Endgame SET Climbing_Seconds = 'X' WHERE Climbing_Seconds IS NULL;"
endgameWin = "UPDATE Endgame SET Win = 'X' WHERE Win IS NULL;"

#defense
defenseColor = "UPDATE Defense SET Color = 'X' WHERE Color IS NULL;"
defenseAttemptedBlock = "UPDATE Defense SET Blocked = 'X' WHERE Blocked IS NULL;"
defenseHeldBalls = "UPDATE Defense SET Held_balls = 'X' WHERE Held_balls IS NULL;"

#comments
commentsColor = "UPDATE Comments SET Color = 'X' WHERE Color IS NULL;"
commentsComments = "UPDATE Comments SET Insert_Comments = 'X' WHERE Insert_Comments IS NULL;"

cursor.execute(autonColor)
print("Finished High in Auton!")

cursor.execute(autonHigh)
print("Finished High in Auton!")

cursor.execute(autonLow)
print("Finished Low in Auton!")

cursor.execute(autonMissed)
print("Finished Missed in Auton!")

cursor.execute(autonOffPlatform)
print("Finished Off_Platform in Auton!")

cursor.execute(autonBasketballShots)
print("Finished Basketball shots in Auton!")
                        
cursor.execute(teleopColor)
print("Finished Color in Teleop!")

cursor.execute(teleopMoved)
print("Finished Moved in Teleop!")

cursor.execute(teleopHigh)
print("Finished Moved in Teleop!")
                                    
cursor.execute(teleopLow)
print("Finished Low in Teleop!")

cursor.execute(teleopMissed)
print("Finished Missed in Teleop!")

cursor.execute(teleopBurst)
print("Finished Burst in Teleop!")

cursor.execute(teleopLaunchpad)
print("Finished Launchpad in Teleop!")

#endgame
cursor.execute(endgameColor)
print("Finished Color in Endgame!")

cursor.execute(endgameClimb)
print("Finished Climb in Endgame!")

cursor.execute(endgameSuccessTier)
print("Finished Success Tier in Endgame!")

cursor.execute(endgamePrepared)
print("Finished Prepared in Endgame!")

cursor.execute(endgameClimbingSeconds)
print("Finished Climbing Seconds in Endgame!")

cursor.execute(endgameWin)
print("Finished Win in Endgame!")

#Defense
cursor.execute(defenseColor)
print("Finished Color in Defense!")

cursor.execute(defenseAttemptedBlock)
print("Finished Attempted Block in Defense!")

cursor.execute(defenseHeldBalls)
print("Finished Held Balls in Defense!")

#comments
cursor.execute(commentsColor)
print("Finished Color in Comments!")

cursor.execute(commentsComments)
print("Finished Comments in Comments!")

print("DONE! :D")

cnx.commit()
cursor.close()
cnx.close()