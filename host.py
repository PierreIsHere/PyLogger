import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sameed123",
  database="pylogger"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM words")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)