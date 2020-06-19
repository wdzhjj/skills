import requests
import time

def getHTMLText(url):
	try:
		kv = {'user-agent':'Mozilla/5.0'} 	#模拟浏览器发送请求
		r = requests.get(url, timeout=30, headers = kv)
		r.raise_for_status()				#如果不是200 则产生异常
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常",r.status_code	

def getText():
	url = "http://www.baidu.com"
	start = time.perf_counter()
	for i in range(100):
		start1 = time.perf_counter()
		getHTMLText(url)
		end1 = time.perf_counter()
		print("第{0}次用时{1}".format(i,end1 - start1))
	end = time.perf_counter()
	print("爬取用时{0}".format(end-start))	

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
print(getHTMLText(url))