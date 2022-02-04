# How to properly set up and create the Database.

## Part 1: Check Versions

### **MySQL**

First, check the mySQL version. For Linux and possibly Windows 10 the command prompt can be used to check by typing the following:

```
$ mysql -V
```

If you have downloaded the correct version of mySQL it should show up as  *(mySQL Server version _8.0.27_)*. 

Note that this doesn't have to be exact, as long as the verion number is *_8.0.27_* or greater, you'll be fine.

### **Python**

To check the version of Python and its Connector, the first thing you'll need to do is to type the following into a command prompt:

```
$ python3 -V
```

The correct version of Python that you should have installed is Python *_3.9.7_* or later. Note that this doesn't have to be exact, as long as the verion number is *_8.0.27_* or greater, you'll be fine.

### **Python Connector**

To check the Python Connector, the first thing you do is to open a terminal and type the following to use Python's terminal:
```
$ python3

>>> from distutils.sysconfig import get_python_lib

>>> print(get_python_lib())
```
To exit the python3 terminal, simply hit CTRL + d
This should print out where it is located.
the correct python connector is *(connector version _8.0.28_)*

### Part 2: Starting Up the Database

First check if mySQL is already started, which is usually the case since mySQL likes to autostart. Through the Linux terminal, you can check the status of mySQL usinng the following command:
```
$ sudo systemctl status mysql
```
You can also do `mysql.service` in place of `mysql`.
Remember this command, as this will come up in Part 3.

### **Part 3: Creating a Database**

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