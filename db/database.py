import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode
import requests
from bs4 import BeautifulSoup

cnx = mysql.connector.connect(user="dalek", password="3637",
                        host="127.0.0.1",
                        database='Scouting')

cursor = cnx.cursor()

#request url
response = requests.get("http://127.0.0.1")
soup = BeautifulSoup(response.text, "html.parser")


#find value of html slider
slider = soup.find("span", {"id": "autonHighShotsMadeOutput"})
print (slider)

# print (slider['autonHighShotsOutput'])

slider = soup.find("span", {"id": "autonLowShotsMadeOutput"})
print (slider)

#slider = soup.find("div", {"class": "slider"})
#print(slider.get("value"))

# print (soup.find('value',attrs={'name':'autonHighShots'}).has_attr('checked'))
# print (soup.find('input',attrs={'name':'autonHighShots'}).has_attr('checked'))
# print (soup.find('input',attrs={'name':'autonHighShots'}).has_attr('checked'))
# print (soup.find('input',attrs={'name':'autonHighShots'}).has_attr('checked'))

cursor.close()
cnx.close()
# https://beautiful-soup-4.readthedocs.io/en/latest/