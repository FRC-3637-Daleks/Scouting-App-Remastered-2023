# Scouting-App-Remastered-2022
The new and improved scouting app with complete documentation and instructions (hopefully)
The scouting app utilises HTML, CSS, Apache, and MySql. It is very important that all of these are installed, where applicable. It is very IMPORTANT to note that these instructions are intended for Linux. 

### **Section 1 - Installing Necessary software** 
- You must install the aproprate version fo Apache, this can be done in 2 ways

    1.1 - Using ```sudo apt install apache2``` 

    1.1.2 - Download Apache directly from [here](https://httpd.apache.org/download.cgi), note that the original version used is 2.4.52, newer versions may not be supported.

- You must install MySql, this can be done in 2 ways
    1.2 - Using ```sudo apt install MySql```, this may install the most recent version, which may deprecate the code

    1.2.1 - Download MySql from the [here](https://dev.mysql.com/downloads/mysql/), note that the original version used is 8.0.28, newer versions may not be supported

- Finally please note that to test if these are installed correctly please go [here](https://github.com/FRC-3637-Daleks/Scouting-App-Remastered-2022/blob/14f0c79bc9d863b82ffda5790914cf5350550fc0/db/setup-README.md), it is important to note further instructions on items usch as connector pything are listed here. These should be installed. 

### **Section 2 - Double Check That All Dependencies Are Installed**
-  
    2.1  - Go to [here](https://github.com/FRC-3637-Daleks/Scouting-App-Remastered-2022/blob/14f0c79bc9d863b82ffda5790914cf5350550fc0/db/setup-README.md)

    2.2 - Triple check all databases are present 

### **Section 3 - Understanding Databeses With Examples**
- 
    3.1 - Databases use tables and other items to well, store data. In the original version of the scouting app we used a 2d table, to store information utilising rows and colums. The colums would contain the data types and the rows would contain said data. Essentially a whole row would be allocated to a team, making it much simpler than a 3d table. For more infomration please click [here](https://docs.google.com/spreadsheets/d/1lCQqQTsaWcqok09gHu-j7aPdQEGYPZY-G7KIvSE3v24/edit?usp=sharing). For more information go to [here](https://github.com/FRC-3637-Daleks/Scouting-App-Remastered-2022/blob/14f0c79bc9d863b82ffda5790914cf5350550fc0/db/setup-README.md) and [here](https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html)
    
    3.2 - Understanding connector pythong is very important, please visit [here](https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html), and [here](https://github.com/FRC-3637-Daleks/Scouting-App-Remastered-2022/blob/14f0c79bc9d863b82ffda5790914cf5350550fc0/db/setup-README.md)

    3.3 - Finally, and arguably the most important informaiton you need to know is a basic knowledge of Python and HTML. Using the Python documentation with MySql will be sufficent. The offial MySql with Python documentation can be found [here](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html). Additionally a "crash course" concerning html and css can be found [here](https://youtube.com/playlist?list=PLblA84xge2_y8F1K0wzPia9V_ULVcfg4k)

### **Section 4 - Understanding and Setting Up CGI**
- 
    4.1 - Common Gateway Interface Port, this alllows a server to execute external programs. This allows apache2 to pull infomraiton from a submitted form. This is espcially hepful when pulling information from multiple forms, which need to be submitted into a databse. To install CGI read further. NOTE* before installing CGI check to make sure you dont have ```httpd.conf present```, as further depedenices and issues may arise. 
    
    4.2 - Setting Up CGI. To set up CGI multiple changes must be made to apache2, as apache2 already includes CGI. 
    This activates the cgi.load which will enable apache2 to start looking for the the submitted form. 
    ```
    sudo ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/
    ```
    Add your databse.py into this directory using the mv command 
    ```
    mv databse.py /usr/lib/cgi-bin
    ```
    This gives apache the permissions to execute cgi commands. 
    ```
    sudo chmod 755 /usr/lib/cgi-bin/databse.py
    ````
    Next move over the ```serv-cgi-bin.conf``` located in ```/etc/apache2/conf-enabled```. Next change the files to match what's below.
    ```
    <IfModule mod_alias.c>
        <IfModule mod_cgi.c>
                Define ENABLE_USR_LIB_CGI_BIN
        </IfModule>

        <IfModule mod_cgid.c>
                Define ENABLE_USR_LIB_CGI_BIN
        </IfModule>

        <IfDefine ENABLE_USR_LIB_CGI_BIN>
                ScriptAlias "/cgi-bin/" "/usr/lib/cgi-bin/"
                <Directory "/usr/lib/cgi-bin">
                        AllowOverride None
                        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                        AddHandler cgi-script .cgi .py
                        Require all granted
                </Directory>
        </IfDefine>
    </IfModule>
    ```
    Finally restart apache 2
    ```
    sudo systemctl restart apache2
    ```
### **Section 5 - Setting Up Forms**
- 
    5.1 Information taken in from itmes such as radio buttons are usally added as inputs which then python handles, and sequentially sends to your ```datbase.py```. For some additonal help and information vist here[https://www.tutorialspoint.com/passing-radio-button-data-to-cgi-program-in-python].




    
