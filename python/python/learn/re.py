import re

match = re.search(r'[1-9]\d{5}','BIT 100181')
if match:
	print(match.group())
else:
	print('search')	

# search 在字符串中搜索
# match 在开始位置进行匹配

match = re.match(r'[1-9]\d{5}','100181 C 100888')
print(match.group())



# re.findall 搜索字符串，以列表类型返回全部能匹配的子串

ls = re.findall(r'[1-9]\d{4}','BIT10081 tts10098')
print(ls)

# re.split 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型

ls = re.split(r'[1-9]\d{4}','BIT10081 SST10011')
print(ls)
ls = re.split(r'[1-9]\d{4}','BIT10081 SST10011',maxsplit=1)
print(ls)


#re.finditer  搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素的match对象

for m in re.finditer(r'[1-9]\d{4}','BIT10081 SST10011'):
	if m:
		print(m.group(0))


## sub  在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
# re.sub(pattern,repl,string,count=0,flags=0)		
res = re.sub(r'[1-9]\d{4}','itsnum','BIT10081 SST10011')
print(res)


# regex = re.compile(pattern,flags=0)
# 将正则表达式的字符串形式编译成正则表达式对象
pat = re.compile(r'[1-9]\d{5}')
rst = pat.search('BIT10081')

##  match 对象的属性
#  .string 待匹配的文本   .re   匹配时使用的pattern对象   
# .pos  正则表达式搜索文本的开始位置   .endpos 正则表达式搜索文本的结束位置
#  方法
# .group(0)   获得匹配后的字符串  .start()   匹配字符串在原始字符串的开始位置
# .end()		匹配字符串在原始字符串的结束位置   .span 返回 .start(),.end()



#RE 库 默认贪婪匹配，会返回匹配字符串最长的子串
# 最小匹配：
# 	*?		前一个字符0次或无限次扩展，最小匹配
# 	+?		1次或无限次，最小
#	??		0或1  最小匹配
#	{m,n}?	扩展前一个字符m至n次，含n，最小匹配