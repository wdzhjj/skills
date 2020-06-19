#jieba.py 通过三方库 记录分词出现次数
import jieba

def getContent():
	txt = open("hamlet.txt", "r").read()
	txt = txt.lower()
	for ch in '|"$%^#())*,-./:;<>=@!@|[]·~':
		txt = txt.replace(ch, " ");
	return txt	

def getChina():
	txt = open("bawangbieji.txt","r", encoding="utf-8").read()
	words = jieba.lcut(txt)
	return words


#kindomTxt = getContent()	
#words = kindomTxt.split()
words = getChina()
counts = {}
for word in words:
	if len(word) == 1:
		continue
	else:	
		counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(15):
	word,count = items[i]
	print("{0:<100}{1:<5}".format(word,count))		