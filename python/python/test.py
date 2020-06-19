import requests
import re
import random
import json
import time

appid = '333206289'
# url = 'https://www.chandashi.com/api/apps/keywordCover?appId=333206289&country=cn&date=20190813&prevDate=20190812&iosVersion=12&clientId=10005&timestamp=1565688251&sign=7E53E76522E2052EF8DD9F4AECCC10F7D59B1690'
# url = 'https://www.chandashi.com/api/apps/keywordCover'
# url = 'https://www.chandashi.com/api/apps/keywordCover?appId=333206289&country=cn&date=&prevDate=&iosVersion=12&clientId=10005&timestamp=1565698844&sign=A203DBD79747FE9228AE31ACB07926366B892238'
url = 'https://www.chandashi.com/api/apps/keywordCover?timestamp=1566974483&appId=333206289&country=cn&iosVersion=12&clientId=10005&sign=409A94FBE2CB060128549B01702AF593DF70D3FE'
keyword = '支付'

#登录
username = '412815436@qq.com'
pwd = '85322801'
login_url = 'https://www.chandashi.com/user/login.html'



SescretStr = 'shuinixiangshuishishabi'
clientId = '10005'
Salt = '&CDSweb.adb.20190101'

appid = '333206289'
country = 'cn'
iosVersion = '12'

def getSign(appid,country,iosVersion):
	timestamp = int(time.time())
	

# getSign(appid,country,iosVersion)	

def send_url(url):
	r = requests.get(url)
	return r

def login(username,pwd):
	rand = ""
	for i in range(6):
		num = random.randint(0, 9)
		rand = str(rand) + str(num)
	print(rand)	
	data = {
			'username':username,
			'pwd':pwd,
			'rand':'782309'          #一个六位数随机码
			}

	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
			}		

	# 保存session信息
	session = requests.session()
	r = session.post(login_url,data=data,headers=headers)
	print(r.cookies['cds_session_id'])
	url = 'https://www.chandashi.com/api/apps/keywordCover?appId=333206289&country=cn&date=&prevDate=&iosVersion=12&clientId=10005&timestamp=1565694701&sign='
	r = session.get(url,headers=headers)
	return r

# r = login(username,pwd)
r = send_url(url)
print(r.status_code)
print(r.text)




# 登录成功后 获取 keyword相关信息
'''
res = send_url(url)
if res.status_code == 200:
	jsondata = res.text
	dictdata = json.loads(jsondata)
	tag = False
	for i in range(len(dictdata['data'])):
		if keyword == dictdata['data'][i][0]:
			print(dictdata['data'][i])
			tag = True
	if tag == False:
		print('没有结果')

'''


