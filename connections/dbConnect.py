import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pythondb_test"
)

mycursor = mydb.cursor()