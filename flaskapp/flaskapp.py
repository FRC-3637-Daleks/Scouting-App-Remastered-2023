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


    

# define the route() decorator to link with a valid URL in the application
#keep it as /, since its alias is changed in the 000-default.conf in sites-enabled.
@app.route('/display') 

# # define a function that is triggered when this URL appears in the browser address bar
def dropdown(): 

    #create a cursor
    cursor = conn.cursor() 
    
    #execute select statement to fetch data to be displayed in combo/dropdown
    cursor.execute('SELECT * FROM Auton ORDER BY CAST(Team AS unsigned);') 
    #fetch all rows and store as a set of tuples 
    auton_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Comments ORDER BY CAST(Team AS unsigned);') 
    comments_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Defense ORDER BY CAST(Team AS unsigned);')
    defense_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Endgame ORDER BY CAST(Team AS unsigned);')
    endgame_1 = cursor.fetchall()
    cursor.execute('SELECT * FROM Teleop ORDER BY CAST(Team AS unsigned);')
    teleop_1 = cursor.fetchall()
    
     #render template and send the set of tuples to the HTML file for displaying
    return render_template("display.html",auton_1=auton_1, comments_1=comments_1, defense_1=defense_1, endgame_1=endgame_1, teleop_1=teleop_1)

if __name__ == '__main__':
   app.run()