from functools import reduce
import re
import os

#clean : clean text by turkish words
def clean(text):
	d = { "Ş":"ş", "İ":"i", "Ü":"ü", "Ç":"ç", "Ö":"ö", "Ğ":"ğ",  "I":"ı", "Î":"ı", "Û":"u", "Â":"a" , "â":"a" , "î":"ı" , "û":"u" , "ä":"a", "à":"a", "å":"a", "é":"e", "ê":"e", "ë":"e", "è":"e", "ï":"ı", "ì":"ı", "ò":"o", "ù":"u", "ÿ":"y", "ó":"o", "ú":"u", "ñ":"n", "Ñ":"a", "À":"a", "Á":"a", "Ã":"a", "Ä":"a", "Å":"a", "È":"e", "É":"e", "Ê":"e", "Ë":"e", "Ì":"ı", "Í":"ı", "Î":"ı", "Ï":"ı", "Ò":"o", "Ó":"o", "Ô":"o", "Õ":"o", "Ö":"o" }
	text = reduce( lambda x, y: x.replace( y,d[y] ),d,text )
	text = text.lower()
	text = re.sub('[^a-z0-9\sçışöğü]+', '', text)
	text = text.strip()
	return text

#trinity: parse line into three characters 
def trinity(row):
	for i in range(len(row)-2):
		yield ''.join(row[i:i + 3])

#variables
totalch = 0
twchar = []

#char: columns name for matrix
char = '''abcçdefgğhıijklmnoöprsştuüvyzqwx'''

#twchar: rows name for matrix
for i in char:
	for j in char:
		twchar.append( i+j )

#print(len(char))#54
#print(len(twchar))#2916

#add number to name for create matrix
mrowname = dict( [ (k,v) for v,k in enumerate(char)] )
mcolname = dict( [ (k,v) for v,k in enumerate(twchar)] )
matris = [ [ 0 for mrow in range(len(char)) ] for mcol in range(len(twchar)) ]

#how long data size
print(os.stat("data.txt").st_size)
#sayac = 0

#calculate line in data
for exm in open('data.txt'):
	exm = clean(exm)
	#print(str(sayac)+'gonderiliyor')
	for a, b ,c in trinity(exm):
		matris[mcolname[a+b]][mrowname[c]] += 1
		totalch +=1
	#sayac +=1

#replace all indices into totalch in matris
for i in range(len(twchar)):
	for j in range(len(char)):
		matris[i][j] = matris[i][j] / totalch

#convert matris to txt file
with open("probobility_matrix.txt", "w") as file:
    file.write(str(matris))