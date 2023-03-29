# make sure to move this to [where it goes]

# import the flask class
from flask import Flask, render_template, url_for, redirect, request, jsonify
from flaskext.mysql import MySQL

# create an instance of the flask class 
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

mysql = MySQL()
 
# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'dalek'    # user of MySQL
app.config['MYSQL_DATABASE_PASSWORD'] = '3637' # password 
app.config['MYSQL_DATABASE_DB'] = 'Scouting'  # Database name
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # database host of MySQL

#initialise mySQL
mysql.init_app(app)

#create connection to access data
conn = mysql.connect()

@app.route('/display', methods=["GET", "POST"])

# define a function that is triggered when this URL appears in the browser address bar
def display():
    result = False
    if request.method == 'POST':
        form = request.form
        result = getData(form)
    
    # literally just getting the team
    cursor = conn.cursor()
    cursor.execute('SELECT Team FROM Auton;')
    team_1 = cursor.fetchall()
    team_1 = tuple(set(team_1))
    return render_template('display.html', result=result, team_1=team_1)

def getData(form):

    # grab user input from form
    team = request.form['Search']

    # create a cursor
    cursor = conn.cursor()
    # execute select statement to fetch data to be displayed in combo/dropdown
    cursor.execute('SELECT * FROM Auton WHERE Team = %s', team)
    # fetch all rows and store it
    auton_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Teleop WHERE Team = %s', team)
    teleop_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Endgame WHERE Team = %s', team)
    endgame_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Defense WHERE Team = %s', team)
    defense_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Comments WHERE Team = %s', team)
    comments_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Pit WHERE Team = %s', team)
    pit_1 = cursor.fetchall()
    # storing queries as a set of tuples
    auton_1=auton_1
    comments_1=comments_1
    defense_1=defense_1
    endgame_1=endgame_1
    teleop_1=teleop_1
    pit_1 = pit_1
    return (auton_1, teleop_1, endgame_1, defense_1, comments_1, pit_1)

if __name__ == '__main__':
   app.run()