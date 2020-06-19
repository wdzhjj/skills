import requests
from bs4 import BeautifulSoup
import time
import re,os,os.path,sys

def getHTMLText(url):
	try:
		kv={"user-agent":"Mizilla/5.0"}    #设置消息头 
		r = requests.get(url,timeout=30,headers=kv)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text 
	except:	
		print("产生异常，url为:" + url)

def illegal_char(s):
    s = re \
        .compile( \
        u"[^"
        u"\u4e00-\u9fa5"
        u"\u0041-\u005A"
        u"\u0061-\u007A"
        u"\u0030-\u0039"
        u"\u3002\uFF1F\uFF01\uFF0C\u3001\uFF1B\uFF1A\u300C\u300D\u300E\u300F\u2018\u2019\u201C\u201D\uFF08\uFF09\u3014\u3015\u3010\u3011\u2014\u2026\u2013\uFF0E\u300A\u300B\u3008\u3009"
        u"\!\@\#\$\%\^\&\*\(\)\-\=\[\]\{\}\\\|\;\'\:\"\,\.\/\<\>\?\/\*\+"
        u"]+") \
        .sub('', s)
    return s        


if __name__ == '__main__':
    localtime = time.strftime('%Y%m%d',time.localtime(time.time()))  #本地时间
    # 创建文件夹
    # rootdir = sys.path[0]+"/news/"+localtime
    rootdir = "C:/Etaray"+"/news/"+localtime
    print(rootdir)
    try:
        if os.path.exists(rootdir):
            pass
        else:
            os.makedirs(rootdir)    
    except Exception as e:
        print("创建文件夹发生错误" + e)      

    filename = str(int(round(time.time()*1000)))
    f = open(rootdir+'/'+filename+'.txt','w+')
    # end
    f.write(localtime[:4]+'年'+localtime[4:6]+'月'+localtime[6:]+'日')

    url = "http://tv.cctv.com/lm/xwlb/"     
    res = getHTMLText(url)
    soup = BeautifulSoup(res,"html.parser")     
    text = soup.select('.right_con01>ul>li>a')
    key = '[视频]'
    lbkey = '联播快讯'
    m = 1
    xwlb_time = soup.select('.mh_title')
    list_time = re.findall('\d',xwlb_time[0].get_text())
    str_time = "".join(list_time)

    if str_time == localtime:
        for txt in text:
            if lbkey in txt.string:
                sonUrl = txt.get('href')
                sonRes = getHTMLText(sonUrl)
                sonSoup = BeautifulSoup(sonRes,'html.parser')
                sonText = sonSoup.select('.cnt_bd>p>strong')
                x = 1
                for tt in sonText[1:]:
                    print(tt.string)
                    f.write('(' + str(x) + ')' + tt.string+';/n')
                    x = x + 1
    else:
        f.write('未更新 \n')                
  
    # # 六安人论坛
    # for n in range(1,1001):
    #     url = "http://bbs.luanren.com/forum-49-"+str(n)+".html"
    #     res = getHTMLText(url)
    #     soup = BeautifulSoup(res,'html.parser')
    #     text = soup.select('.new>a')
    #     for txt in text:
    #         if txt.string:
    #             print(txt.)
    #             sys.exit()
    #             # f.write(illegal_char(txt.string)+'\n')
    # f.close()    