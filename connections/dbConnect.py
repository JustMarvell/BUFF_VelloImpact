import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pythondb_test"
)

async def Connect():
    mycursor = mydb.cursor()
    return mycursor

async def Close():
    mydb.close()
    