#### requests库
		pip install requests
		
		******7个主要方法
		
		requests.request() 构造一个请求，支撑一下各方法的基础方法
				.get() 	   获取html网页的主要方法，对应于http的get
				.head()		获取html网页头信息的方法，对应http的head
				.post() 	向HTML网页提交POST请求方法，对应于HTTP的POST
				.put()		向HTML提交PUT请求
				.patch()	向HTML提交局部修改请求
				.delete()	向HTML提交删除请求
				
				
		request.get(url,params=None,**kwargs)
		
		url:拟获取页面的url链接
		params: url中的额外参数，字典或字节流格式
		**kwargs:12个控制访问的参数
		
		
		*******Response 对象的属性
			r.status_code	HTTP请求的返回状态，200表示成功，404表示失败
			r.text			HTTP响应的内容的字符串形式
			r.encoding		http header中猜测的响应内容的编码方式
			r.apparent_encoding 从内容中分析出的响应内容的编码方式
			r.content 		HTTP响应内容的二进制形式
		
		
		
		*********Requests库的异常
			requests.ConnectionEroor  	网络连接错误异常，如DNS查询失败、拒绝连接
			requests.HTTPError			HTTP错误异常
			requests.URLRequired		URL缺失异常
			requests.TooManyRedirects	超过最大重定向次数，产生重定向异常
			requests.ConnectTimeout		远程连接服务器超时异常
			requests.Timeout			请求URL超时，产生超时异常
		
		
		**** requests.request(method,url,**kwargs)
			**kwargs : 访问控制的参数，均为可选项
			params： 字典或字节序列，作为参数增加到url中
			kv = {'k1':'v1','k2':'v2'}
			requests.request('GET','http://..',params=kv)
			=>相当于
				http://...?k1=v1&k2=v2
			
			data: 字典、字节序列或文件对象，作为 Request的内容
			
			json：json格式数据，作为内容提交
			
			headers: http头字段  模拟浏览器
		
			cookies : 字典或cookieJar Request中
			auth: 元祖，支持HTTP认证功能
		
			files : 字典类型，传输文件		files = fs
			timeout : 设定超时时间，秒为单位
			
			proxies : 字典类型，设定访问代理服务器，可以增加登录认证
					有效隐藏ip信息  防止爬虫逆向追踪
			allow_redirects: True|False 默认为T，是否允许重定向
			stream: T|F  默认T  是否对获取内容立即进行下载
			verify: T|F  是否认证SSL证书
			cert： 本地SSL证书路径
		
		
#### becautiful soup库
		pip install becautifulsoup4
		
		bs库也叫 beautifulsoup4 或 bs4
			from bs4 import BecautifulSoup
			import bs
			
		bs 库 解析器
			解析器					使用方法						 条件
		bs4的HTML解析器        BecautifulSoup(mk,'html.parser')		安装bs4库
		lxml的html解析器	   BecautifulSoup(mk,'lxml')			pip install lxml
		lxml的XML解析器	       BecautifulSoup(mk,'xml')				pip install lxml
		html5lib的解析器		BecautifulSoup(mk,'html5lib')		pip install html5lib
		
		
		***** 基本元素
			Tag			标签，最基本的组织单元，分别用<></>标明开头和结尾
			Name 		标签的名字，<p></p> 名字是 p 
			Attributes	标签的 属性，字典形式组织，格式 <tag>.attrs
			NavigableString		标签内非属性字符串  <>...</>中字符串 <tag>.string
			Comment		标签内字符串的舒适部分，一个特殊的Comment类型
		
		
		** 标签树的下行遍历
			.contents   子节点的列表，将<tag>所有儿子节点存入列表
			.children	子节点的迭代类型,与.contents类似，用于循环遍历儿子节点
			.descendantrs	子孙节点的迭代类型，包含所有子孙节点，用云循环遍历
		
		** 上行遍历
			.parent 	节点的父亲标签
			.parents	节点的先辈标签的迭代类型，用于循环遍历先辈节点
		
		** 平行遍历
			.next_sibling		返回按照HTML文本顺序的下一个平行节点标签
			.previous_sibling	返回按照HTML文本顺序的上一个平行节点标签
			.next_siblings		迭代类型，返回按照HTML文本是顺序的后续平行节点标签
			.previous_siblings	迭代类型，返回按照HTML文本是顺序的前续平行节点标签
		
		
		<>.find_all(name, attrs, recursive, string, **kwargs)
			返回一个列表类型，存储查找的结果
			name: 对标签名称的检索字符串
			attrs：对标签属性值的检索字符串，可标注属性检索
			recursive:是否对子孙全部检索，默认为True
			string:<>...</>中字符串区域的检索字符串
		
		
#### RE库
		正则表达式库
		regular expression   regex   RE
			用来简洁表达一组字符串的表达式
		编译：
			将符合正则表达式语法的字符串转换成正则表达式特征
		
		.   	表示任何单个字符
		[]		字符集，对单个字符给出取值范围
		[^]		非字符集，对单个字符给出排除范围
		*		前一个字符0次或无限次扩展
		+				  1
		？				  0次或1次
		|		左右表达式任意一个
		{m}		扩展前一个字符m次
		{m,n}	扩展前一个字符m到n次
		
		^		匹配字符串开头
		$		匹配字符串结尾
		()		分组标记，内部职能使用|操作符
		\d 		数字，等价于[0-9]
		\w		单词字符，等价于[A-Za-z0-9+_]
		
		RE库是python标准库，不需安装，主要用于字符串匹配
		调用：
			import re
		主要函数：
			re.search()		在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
			re.match()		从一个字符串的开始位置起匹配正则表达式，返回match对象
			re.findall()	搜索字符串，以列表类型返回廍能匹配的子串
			re.split()		将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
			re.finditer()	搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
			re.sub()		在一个字符串中替换所有匹配正则表达式的子串返回替换后的字符串
			
			
		re.search(pattern,string,flags=0)
			pattern: 正则表达式的字符串或原生字符串表示
			string： 待匹配的字符串
			flags：正则表达式使用时的控制标记
			
				re.I		忽略正则表达式的大小写 [A-Z]可以匹配小写字符
				re.M		^操作符能够将给定字符串的每行当做匹配开始=
				re.S		正则表达式中的 . 操作符能够匹配所有字符，默认匹配除换行外的所有字符
		
			前三个函数 参数相同
			re.split()	 第三个参数为 maxsplit 最大分割数，剩余部分作为最后一个元素输出，默认为0
		
			re.sub(pattern,repl,string,count=0,flags=0)
				repl: 	匹配到修改的字符串
				count:	匹配的最大替换次数
		
			re.compile(pattern,flags=0)
			将正则表达式的字符串形式编译成正则表达式形式
				regex = re.compile(r'[1-9]\d{5}')
		
			Match 对象的属性
				.string 		待匹配的文本
				.re				匹配时使用的pattern对象（正则）
				.pos			正则表达式搜索文本的开始位置
				.endpos			正则表达式搜索文本的结束位置
			Match 对象的方法
				.group(0)		获得匹配后的字符串
				.start()		匹配字符串在原始字符串的开始位置
				.end()			匹配字符串在原始字符串的结束位置
				.span()			返回（.start(), .end(()）
		
		
			贪婪匹配和最小匹配
				默认贪婪匹配：匹配范围内最大的字符串
				最小匹配操作符
					*？		前一个字符 0次或无限次扩展，最小匹配
					+？				   1
					??				   0次或1次
					{m,n}	扩展前一个字符m至n次,含n   最小匹配
					
					
#### Scrapy 爬虫框架
		安装 pip install scrapy
		爬虫框架是实现爬虫功能的一个软件结构和功能组件集合
					
		常用命令
			提供操作 Scrapy 命令行
				scrapy -h		开启命令行
			命令行格式
				scrapy <command> [options] [args]
				
				commands:
					startproject  创建一个新工程
					genspider	  创建一个爬虫
					settings 	  获取爬虫配置信息
					crawl		  运行一个爬虫
					list		  列出工程中所有爬虫
					shell		  启动URL调试命令行
					
		**** 流程
			1、scrapy startproject demo
			2、工程目录
				scrapy.cfg		部署Scrapy爬虫的配置文件
				demo			Scrapy框架的用户自定义Python代码
					__init__.py			初始化脚本
					intems.py 			Items代码模板（继承类）
					middlewares.py		Middlewares代码模板 继承类
					pipelines.py		Pipelines 代码模板  继承类
					settings.py         Scrapy 爬虫的配置文件
					spiders/			Spiders代码模板目录
					
			3、scrapy genspider		
				生成demo.py
			
			4、配置产生的 spider
					
			** yield关键字
				生成器、是一个不断产生值的函数
				包含yield语句的函数是一个生成器
				生成器每次产生一个值，函数被冻结，被唤醒后再产生一个值
					for i in range(n):
						yield i**2			产生的值会被返回，再遍历循环
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
		
		
		
		
		
		
		