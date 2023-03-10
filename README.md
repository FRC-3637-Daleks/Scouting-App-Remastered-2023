# Scouting-App-2023
The scouting app utilises HTML, CSS, Apache, and MySQL. It is very important that all of these are installed, where applicable. It is very IMPORTANT to note that these instructions are intended for Linux. 

### **Section 1 - Installing Necessary software** 
- You must install the appropriate version of Apache, this can be done in 2 ways
    PLEASE note that downloading things may NOT work on school wifi because of Smoothwall, you may have to use either a VPN or a phone hotspot.

    1.1 - Install Apache using `sudo apt install apache2`

    1.1.2 - Download Apache directly from [here](https://httpd.apache.org/download.cgi), note that the original version used is 2.4.52, newer versions may not be supported.

    1.2 - Use `sudo apt install mysql-server` to install the MySQL server.

    1.3 - Check and confirm that MySQL is running by entering `sudo systemctl status mysql`. It should say that it is running.

- Finally please go to test if these are installed correctly and to install further applications (like the connector python) visit the [setup-README.md](https://github.com/FRC-3637-Daleks/Scouting-App-Remastered-2023/blob/main/db/setup-README.md) located in the `db/` folder.

### **Section 2 - Understanding and Setting Up CGI**
- 
    4.1 - CGI, also known as the Common Gateway Interface, gives a server the ability to execute external programs, in our case these are `.py` files. 
    This allows Apache2 to pull information from a submitted form using python. This is espcially helpful when pulling information from multiple forms, which need to be submitted into a database.
    
    4.2 - Setting Up CGI. To set up CGI, multiple changes must be made to Apache2, as Apache2 already includes compatibility for CGI that isn't turned on by default. 
    The command below activates the `cgi.load` with a symbolic link that enables Apache2 to use CGI.
    ```
    sudo ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/
    ```
    Next, update the contents of `serve-cgi-bin.conf` located in `/etc/apache2/conf-enabled` to match what's below.
    The main change is adding "" to the ScriptAlias as well as the `Options` and `AddHandler' section under the `<Directory`.
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
    Finally, restart Apache2.
    ```
    sudo systemctl restart apache2
    ```

### **Section 3- Flask**
-
    6.1  - Flask is a micro web framework written in Python. To install Flask you first need to install pip, a package manager for Python. To acquire pip, type
    ```
    sudo apt install python3-pip
    ```
    into the terminal.
    Once the download completes, install Flask through pip by typing
    ```
    sudo pip install Flask
    ```
    You must also install WSGI, the Web Server Gateway Interface, which does exactly what you expect it to do, [interface with the web server gateway](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface). To install it, type the following into the terminal
    ```
    sudo apt-get install libapache2-mod-wsgi-py3
    ```
    Usually it will automatically be invoked, saying so within the Terminal.
    For good measure attempt to enable it again with `sudo a2enmod wsgi`

    6.2 - Moving files to the right place. To get everything to work, some files need to move to certain locations. The first thing you want to do is to go to a browser on the same machine running the webserver and type `127.0.0.1` and see if the generic ubuntu thing comes up, as it should. Then, remove the `index.html` file within the `/var/www/html` file by typing.
    
    ```
    sudo rm /var/www/html/index.html
    ```

    Next you want to copy over the flaskapp folder in the Scouting App Remastered folder to the root directory. If you aren't there already, you can get to the root directory by typing `cd ~` in the terminal, then copy the flaskapp folder by typing
    ```
    sudo cp -r Scouting-App-Remastered-2023/flaskapp ./
    ```
 
    after that, copy the other two critical files located in the scouting app folder called `web/pages/static` and `web/pages/templates` into the flaskapp foder in the root directory by typing
    ```
    sudo cp -r Scouting-App-Remastered-2023/web/pages/static flaskapp/
    sudo cp -r Scouting-App-Remastered-2023/web/pages/templates flaskapp/
    ```

    6.3 - config files. The first config file you will want to change would be `/etc/apache2/sites-enabled/000-default.conf` by copying the CONTENTS INSIDE the `000-default.conf` in the `copies` folder into the `000-default.conf` in `sites-enabled`, NOT the folder itself.

    6.4 - moving the folder. After creating the full folder, move it all to its proper place
    ```
    sudo mv flaskapp/ /var/www/html/
    ```

    6.4 - Permissions. Make sure that the others group have read and execute permissions and are given to the flaskapp folder and everything in it with this command
    ```
    sudo chmod o+rx -R /var/www/html/flaskapp/
    ```
    make sure that the `/var/www/html/flaskapp/` are ALL given their respective permissions with the following commands
    ```
    sudo chmod o+rx -R /var/www/html/
    ```

    6.5 - flask-mysql. Lastly, install flask-mysql by typing this within the console:
    ```
    sudo pip install flask-mysql
    ```
    for good measure, restart Apache as well with a good ol' `sudo systemctl restart apache2` and see if it runs by typing `127.0.0.1` into your internet browser of choice!

### **Miscellaneous - Understanding Scouting App With Examples** 
- General information to know.

    - Databases use tables and other items to well, store data. Here is how we [set up the data to be stored](https://docs.google.com/spreadsheets/d/1lCQqQTsaWcqok09gHu-j7aPdQEGYPZY-G7KIvSE3v24/edit?usp=sharing).
    
    - If you are unfamiliar with MySQL, there are some [sources](https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html) to get your started, mainly the structure and how to edit an already existing file. There are also [some information](https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html) on how the connector-python works in case you're a lil' bookworm.

    - Finally, and arguably the most important information you need to know, a basic knowledge of Python and HTML. The offial MySQL with Python documentation can be found [here](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html). Additionally a "crash course" concerning html and css can be found [here](https://youtube.com/playlist?list=PLblA84xge2_y8F1K0wzPia9V_ULVcfg4k) if you are unfamiliar with these instruments.
