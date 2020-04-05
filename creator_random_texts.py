import random

def randomChar() -> str:
	return random.choice( list("abcdefghijklmnoprstuvyzxqwşıüğçö") )

def randomWord() -> str:
	word = ""
	for _ in range(random.randrange(4, 16)): word = word + randomChar()
	return word

def randomText() -> str:
	text = ""
	for _ in range(random.randrange(1, 6)): text = text + randomWord() + " "
	return text.strip()

with open("randomtexts.txt","w",encoding="utf-8") as file:
	for i in range(500):
		file.write(randomText()+"\n")
	file.close()