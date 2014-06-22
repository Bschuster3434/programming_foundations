import urllib

words = "C:\Users\Schuster\Documents\GitHub\programming_foundations\hurry back.txt"

def read_text(words):
	with open(words, 'r') as fil:
		contents = fil.read()
		check_profanity(contents)
		
def check_profanity(text):
	conn = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
	output = conn.read()
	print output
	conn.close()
	
read_text(words)