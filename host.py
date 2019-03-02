import mysql.connector
from time import sleep
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sameed123",
  database="pylogger"
)
mycursor = mydb.cursor()

count = 1
typed = 0
true = 1
while true == 1:
	if typed == 0:
		mycursor.execute("SELECT * FROM words WHERE id = '"+str(count)+"'")
		myresult = mycursor.fetchall()
		for x in myresult:
  			print(x)
		typed = 1
		count = count + 1
	if typed == 1:
		sleep(0.2)
		mycursor.execute("SELECT * FROM words WHERE id = '"+str(count)+"'")
		myresult = mycursor.fetchall()
		# print(len(myresult))
		if len(myresult) == 1:
			typed = 0