import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "2018622",
	database = "blog"
)

mycursor = mydb.cursor()
mycursor.execute("select title from blog")

for x in mycursor:
	print(x)