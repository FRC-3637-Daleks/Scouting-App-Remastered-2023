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
autonHighCube = "UPDATE Auton SET High_Cube = 0 WHERE High_Cube IS NULL;"
autonHighCone = "UPDATE Auton SET High_Cone = 0 WHERE High_Cone IS NULL;"
autonMidCube = "UPDATE Auton SET Mid_Cube = 0 WHERE Mid_Cube IS NULL;"
autonMidCone = "UPDATE Auton SET Mid_Cone = 0 WHERE Mid_Cone IS NULL;"
autonLowCube = "UPDATE Auton SET Low_Cube = 0 WHERE Low_Cube IS NULL;"
autonLowCone = "UPDATE Auton SET Low_Cone = 0 WHERE Low_Cone IS NULL;"
autonOffPlatform = "UPDATE Auton SET Left_Platform = 'N' WHERE Left_Platform IS NULL;"
autonOutOfCommunity = "UPDATE Auton SET Out_of_Community = 'N' WHERE Out_of_Community IS NULL;"

#teleop
teleopColor = "UPDATE Teleop SET Color = 'X' WHERE Color IS NULL;"
teleopMoved = "UPDATE Teleop SET Moved = 'X' WHERE Moved IS NULL;"
teleopHighCube = "UPDATE Teleop SET High_Cube = 0 WHERE High_Cube IS NULL;"
teleopHighCone = "UPDATE Teleop SET High_Cone = 0 WHERE High_Cone IS NULL;"
teleopMidCube = "UPDATE Teleop SET Mid_Cube = 0 WHERE Mid_Cube IS NULL;"
teleopMidCone = "UPDATE Teleop SET Mid_Cone = 0 WHERE Mid_Cone IS NULL;"
teleopLowCube = "UPDATE Teleop SET Low_Cube = 0 WHERE Low_Cube IS NULL;"
teleopLowCone = "UPDATE Teleop SET Low_Cone = 0 WHERE Low_Cone IS NULL;"

#endgame
endgameColor = "UPDATE Endgame SET Color = 'X' WHERE Color IS NULL;"
endgameClimb = "UPDATE Endgame SET Charge_Status = 'X' WHERE Charge_Status IS NULL;"
endgameWin = "UPDATE Endgame SET Win = 'X' WHERE Win IS NULL;"

#defense
defenseColor = "UPDATE Defense SET Color = 'X' WHERE Color IS NULL;"
defenseAttemptedBlock = "UPDATE Defense SET Blocked_Others = 'X' WHERE Blocked_Others IS NULL;"

#comments
commentsColor = "UPDATE Comments SET Color = 'X' WHERE Color IS NULL;"
commentsComments = "UPDATE Comments SET Insert_Comments = 'X' WHERE Insert_Comments IS NULL;"

cursor.execute(autonColor)
print("Finished High in Auton!")

cursor.execute(autonHighCube)
cursor.execute(autonHighCone)
print("Finished High in Auton!")

cursor.execute(autonMidCube)
cursor.execute(autonMidCone)
print("Finished Mid in Auton!")

cursor.execute(autonLowCube)
cursor.execute(autonLowCone)
print("Finished Low in Auton!")

cursor.execute(autonOffPlatform)
print("Finished Left_Platform in Auton!")

cursor.execute(autonOutOfCommunity)
print("Finished Out Of Community in Auton!")
                        
cursor.execute(teleopColor)
print("Finished Color in Teleop!")

cursor.execute(teleopMoved)
print("Finished Moved in Teleop!")

cursor.execute(teleopHighCone)
cursor.execute(teleopHighCube)
print("Finished Moved in Teleop!")

cursor.execute(teleopMidCube)
cursor.execute(teleopMidCone)
print("Finished Mid in Teleop!")

cursor.execute(teleopLowCube)
cursor.execute(teleopLowCone)
print("Finished Low in Teleop!")

#endgame
cursor.execute(endgameColor)
print("Finished Color in Endgame!")

cursor.execute(endgameClimb)
print("Finished Climb in Endgame!")

cursor.execute(endgameWin)
print("Finished Win in Endgame!")

#Defense
cursor.execute(defenseColor)
print("Finished Color in Defense!")

cursor.execute(defenseAttemptedBlock)
print("Finished Attempted Block in Defense!")

#comments
cursor.execute(commentsColor)
print("Finished Color in Comments!")

cursor.execute(commentsComments)
print("Finished Comments in Comments!")

print("DONE! :D")

cnx.commit()
cursor.close()
cnx.close()