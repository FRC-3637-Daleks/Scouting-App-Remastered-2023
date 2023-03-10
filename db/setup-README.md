# How to properly set up and create the Database.

## Part 1: Check Versions

### **MySQL**

First, check the mySQL version. For Linux and possibly Windows 10 the command prompt can be used to check by typing the following:

```
$ mysql -V
```

If you have downloaded the correct version of mySQL it should show up as  *(mySQL Server version _8.0.27_)*. 

Note that this doesn't have to be exact, as long as the verion number is *_8.0.27_* or greater, you'll be fine.
The version number *_8.0.27_* is for the connector, since there is no easy way to check if you installed the right connector besides looking for that specific number before downloading, pray you installed the right one.

### **Python**

To check the version of Python and its Connector, the first thing you'll need to do is to type the following into a command prompt:

```
$ python3 -V
```

The correct version of Python3 that you should have installed is Python *_3.9.7_* or later. Note that this doesn't have to be exact, as long as the verion number is around *3.9.7_* or greater, you'll be fine.

### **Python Connector**

To download the python connector, simply [visit the same website](https://dev.mysql.com/downloads/connector/python/8.0.html). Make sure to check that you install the Ubuntu linux version as well as the correct python connector for the current Ubuntu version (21.10) or (20.04) depending on the version you choose.

Next, actually unpack the file by finding it within your downloads folder. Clicking it should bring up Eddy, then click install.

To check the Python Connector, the first thing you do is to open a terminal and type the following to use Python's terminal:
```
$ python3

>>> from distutils.sysconfig import get_python_lib

>>> print(get_python_lib())
```
This should print out where it is located.
the correct python connector is *connector version _8.0.28_* or greater
To exit the python3 terminal, simply hit `CTRL + d`

## Part 2: Starting Up the Database

First check if mySQL is already started, which is usually the case since mySQL likes to autostart. Through the Linux terminal, you can check the status of mySQL usinng the following command:
```
$ systemctl status mysql
```
You can also do `mysql.service` in place of `mysql`.
If the command returns something that shows that mysql is offline, then run
```
$ sudo systemctl start mysql
```
to get it back up and running.
If instead you get an error, you must completely, *and I cannot stress this enough* **COMPLETELY** remove every single file containing anything mysql related, then redownload mysql and the connector if you uninstalled it aswell.
## Part 3: Creating a Database

Since having the python script log in as root posed many unique challanges, you'll have to create a user with root privileges through the terminal instead.

to do this, open up a terminal and use the `sudo` command to get you into mysql as root.
```
$ sudo mysql
```
After imputting your sudo password, you should be within mysql in the terminal and where you type should look like this.
```
mysql>
```
Once in mysql, it's time to create a user.

## Part 3.1: Creating a User and Verifying the User Exists

Note that you must follow this **EXACTLY**, even giving the user a different name would force you to edit the python script to match it accordingly, so just take my advice and type carefully.

To create a user within mysql, type in the following below.
```
mysql> CREATE USER 'dalek'@'localhost' IDENTIFIED BY '3637';
```
Once you submit that command, you should get back from mysql a `Query OK, 0 rows affected`, indicating that your change did indeed go through.
If you want to double check, you can do so through the mysql terminal by typing 
```
mysql> use mysql;
```
To enter mysqls database. From there just type 
```
mysql> SELECT user FROM user;
```
This command should output a table displaying all the users currently made. Do not worry about the random ones like `mysql.infoschema`, just make sure that `dalek` is on there. If it isn't, check to make sure you are signed into mysql as root and that you input `use mysql;` to enter the mysql database.
In short, if it doesn't appear redo step 3.

## Part 3.2: Granting Privileges to the User

To ensure that the user can properly execute all the commands that are required you will have to give it root privileges in mysql.
To do this, first grant all of the privileges to that user through mysql
```
mysql> GRANT ALL PRIVILEGES ON *.* TO 'dalek'@'localhost';
```
Once this is entered you need to flush the privileges for teh changes to be in effect.
```
mysql> FLUSH PRIVILEGES;
```
to leave the mysql terminal, just type quit
```
mysql> quit
```
to relieve yourself of the mysql terminal.

That should be it! The user `dalek` now has all privileges and now you should be able to execute the python scripts with ease!

## Part 3.3: Actually Creating the Database

To create the database, first `cd` into the database directory, aptly named db.
Once there run this command to run the python scripts. Note that the first one that should be ran is `setup-database.py`.
```
$ python3 setup-database.py
```
This should spit out the current databases into the terminal. There should be one titled `Scouting`.

# Part 4: Creating Tables

To create a table, just run the `create-tables.py` script by typing into a terminal
```
$ python3 create-tables.py 
```
to run the script and create the tables. 
All of the output within the terminal should say OK or some derivitive of it.

# part 5: moving database.py
after moving `database.py` to `/usr/lib/cgi-bin` you must make it executable by running chmod as shown below
```
$ chmod 755 /usr/lib/cgi-bin/database.py
```

Yay you're done this section! Give yourself a pat on the back and return to the main [README.md](https://github.com/FRC-3637-Daleks/Scouting-App-Remastered-2023#readme) for further instructions.