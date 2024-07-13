import mysql.connector

def get_data():
 mydb = mysql.connector.connect(host="localhost",user="root",password="Benita@3216",database="testdb1")
 mycursor = mydb.cursor()
 mycursor.execute( "SELECT * FROM todo")
 result = mycursor.fetchall()
 mydb.close()
 return result
