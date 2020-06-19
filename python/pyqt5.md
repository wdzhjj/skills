####PyQT5库
		PyQt5是由一系列Python模块组成。
		PyQt5类分为很多模块，主要模块有：
			QtCore 包含了核心的非GUI的功能。
				主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用。
			QtGui 			包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类。	
			QtWidgets		类包含了一系列创建桌面应用的UI元素
			QtMultimedia	包含了处理多媒体的内容和调用摄像头API的类。
			QtBluetooth		模块包含了查找和连接蓝牙的类
			QtNetwork		包含了网络编程的类
			QtPositioning	定位的类，可以使用卫星、WiFi甚至文本
			Enginio			包含了通过客户端进入和管理Qt Cloud的类
			QtWebSockets	包含了WebSocket协议的类
			QtWebKit		包含了一个基WebKit2的web浏览器
			QtWebKitWidgets	包含了基于QtWidgets的WebKit1的类
			QtXml			包含了处理xml的类，提供了SAX和DOM API的工具。
			QtSvg			提供了显示SVG内容的类 
							是一种是一种基于可扩展标记语言（XML），用于描述二维矢量图形的图形格式
			QtSql			提供了处理数据库的工具
			QtTest			提供了测试PyQt5应用的工具
			
			
					
		import sys
		from PyQt5.QtWidgets import QApplication, QWidget
									这里引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件。			

		if __name__ == '__main__':

			app = QApplication(sys.argv)
				每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能。
			w = QWidget()
				QWidget控件是一个用户界面的基本控件，它提供了基本的应用构造器。
			w.resize(250, 150)
				resize()方法能改变控件的大小，这里的意思是窗口宽250px，高150px。
			w.move(300, 300)
				move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(300, 300)的位置
			w.setWindowTitle('Simple')
				我们给这个窗口添加了一个标题，标题在标题栏展示
			w.show()
				show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
				
			sys.exit(app.exec_())			
				当调用exit()方法或直接销毁主控件时，主循环就会结束。
				sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。
				exec_()之所以有个下划线，是因为exec是一个Python的关键字。
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			