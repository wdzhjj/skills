import sys 
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication,QToolTip)
import time,os,os.path,re

import requests
from bs4 import BeautifulSoup

class App(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.title = "PyQt5 button" 
        self.left = 450 
        self.top = 100 
        self.width = 1000 
        self.height = 800 
        self.initUI() 
    def initUI(self): 
        localtime = time.strftime('%Y%m%d',time.localtime(time.time()))  #本地时间
        rootdir = "D:/news/"
        path = rootdir+localtime+'.txt'
        if os.path.exists(path):
            f = open(path)
            txt = f.read()
        else:
            txt = ''    
        self.lbl = QLabel(txt, self)
        self.lbl.move(15, 10)

        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
      
        """在窗体内创建button对象""" 
        button = QPushButton("获取今日新闻", self) 
        """方法setToolTip在用户将鼠标停留在按钮上时显示的消息""" 
        button.setToolTip("This is an example button") 
        """按钮坐标x = 100, y = 70""" 
        button.move(850, 750) 
        """按钮与鼠标点击事件相关联"""
        button.clicked.connect(self.on_click) 
        self.show() 

    """ 获取html的标准方法 """
    def getHTMLText(self,url):
        try:
            kv={"user-agent":"Mizilla/5.0"}    #设置消息头 
            r = requests.get(url,timeout=30,headers=kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text 
        except: 
            print("产生异常，url为:" + url)

    """创建鼠标点击事件""" 
    @pyqtSlot() 
    def on_click(self): 
        localtime = time.strftime('%Y%m%d',time.localtime(time.time()))  #本地时间
        # 创建文件夹
        rootdir = "D:/news/"
        try:
            if os.path.exists(rootdir):
                print()
            else:
                os.makedirs(rootdir)
        except Exception as e:
            print("创建文件夹发生错误" + e)      

        filedir = rootdir+localtime+'.txt'

        f = open(rootdir+localtime+'.txt','w+')
        # end

        f.write(localtime[:4]+'年'+localtime[4:6]+'月'+localtime[6:]+'日')
        f.write('\n【中央新闻】\n')

        # # 新闻联播
        url = "http://tv.cctv.com/lm/xwlb/"     
        res = self.getHTMLText(url)
        soup = BeautifulSoup(res,"html.parser")     
        text = soup.select('.right_con01>ul>li>a')
        key = '[视频]'
        m = 1
        for txt in text:
            if key in txt.string[1:]:
                f.write(str(m)+'.'+txt.string.replace('\r','').replace('\n','').replace(' ','').replace('[视频]','')+'\n')
                m = m+1


        # 获取焦点访谈页面的信息
        url = 'http://tv.cctv.com/lm/jdft/'
        res = self.getHTMLText(url)
        soup = BeautifulSoup(res,"html.parser")     
        text = soup.select('.image_list_box>ul>li>div>a')
        key = '焦点访谈'
        for txt in text:
            if txt.string:
                if key in txt.string:
                    tmp = '20190504'
                    if re.findall("\d+",txt.string)[0] == tmp:
                        strstr = re.findall("\D+",txt.string.replace(' ','').replace('《','【').replace('》','】') ) 
                        f.write(str(m)+'.'+strstr[0]+strstr[1]+'\n')
                        m = m + 1

        
        f.write('\n【浙江新闻】\n')
        n = 1
        # 浙江新闻联播
        url = 'http://www.cztv.com/videos/zjxwlb'
        res = self.getHTMLText(url)
        soup = BeautifulSoup(res,'html.parser')
        text = soup.select('.info_box1>div.vod_list>ul>li>span.t1')
        for txt in text[2:]:
            f.write(str(n)+"."+txt.string+'\n')
            n = n+1


        # 浙江今日聚焦
        url = 'http://www.cztv.com/videos/jrjj/'
        res = self.getHTMLText(url)
        soup = BeautifulSoup(res,'html.parser')
        text = soup.select('.info_box>div#scroll_list>dl#scrollContent>dt>span>strong')
        for txt in text:
            tt = re.sub(r'\d','',txt.string.replace('《','【').replace('》','】'))
            f.write(str(n) + "." + tt + '\n')
        
        print("write ok")
        #关闭文件操作
        f.close()

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())
















