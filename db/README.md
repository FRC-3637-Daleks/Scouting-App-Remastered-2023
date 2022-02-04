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
$ 



### **Part 3: Creating a Database**

Since having the python script log in as root posed many unique challanges, you'll have to create a user with root privileges instead.

to do this,