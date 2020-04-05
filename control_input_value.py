from functools import reduce
import numpy as np

#clean : clean text by turkish words
def clean(text):
	d = { "Ş":"ş", "İ":"i", "Ü":"ü", "Ç":"ç", "Ö":"ö", "Ğ":"ğ",  "I":"ı", "Î":"ı", "Û":"u", "Â":"a" , "â":"a" , "î":"ı" , "û":"u" }
	text = reduce( lambda x, y: x.replace( y,d[y] ),d,text )
	text = text.lower()
	text = text.strip()
	return text

#trinity: parse line into three characters 
def trinity(row):
	for i in range(len(row)-2):
		yield ''.join(row[i:i + 3])

#variable
totalch = 0
twchar = []

#char: columns name for matrix
char = "abcçdefgğhıijklmnoöprsştuüvyzqwx "

#twchar: rows name for matrix
for i in char:
	for j in char:
		twchar.append( i+j )

#print(len(char))#53
#print(len(twchar))#2809

#add number to name for create matrix
mrowname = dict( [ (k,v) for v,k in enumerate(char)] )
mcolname = dict( [ (k,v) for v,k in enumerate(twchar)] )
#print( mrowname )
#print( mcolname )

#read matrix in file
with open("probobility_matrix.txt", "r") as file:
    matris = eval(file.readline())

#trial steps
while True:
	text = input("Denenecek kelimeyi giriniz : ")
	text = clean( text )
	text = text.split()
	totalch = 0
	pay = 0
	minum = 0
	ort = 0
	q75 = 0
	liste = []
	for word in text:
		for a, b ,c in trinity(word):
			pay += matris[mcolname[a+b]][mrowname[c]]
			liste.append(matris[mcolname[a+b]][mrowname[c]])
			totalch +=1
			if minum == 0:
				minum = pay
			elif minum > pay:
				minum = pay
	ort = pay / totalch
	if ort >=0.00003:
		print(str(ort) + 'Anlamlı')
	else:
		print(str(ort) + 'Anlamsız')