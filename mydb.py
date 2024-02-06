import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd = 'ecu3ador4'
)


# cursor object

cursorObject = dataBase.cursor()

#create a db

cursorObject.execute("CREATE DATABASE mycrmdb")

print("ALL DONE")