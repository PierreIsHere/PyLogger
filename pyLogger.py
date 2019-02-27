from pynput import keyboard

def on_release(key):
    letter = key
    if letter == keyboard.Key.tab:
    	# print(letter)
        return False				
letters = []
words = []
def log(key):
	letter = key
	if letter != keyboard.Key.space and letter != keyboard.Key.enter:	
		letters.append(letter)
	if letter == keyboard.Key.space or letter == keyboard.Key.enter:	
		print(letters)
		word = ''.join(map(str, letters))
		words.append(word.replace("'"," "))
		del letters[:] is this real life or is this just fantasey 
	print(letters)
	print(words)

with keyboard.Listener(
        on_press=log,
        on_release=on_release
        ) as listener:
    listener.join()
