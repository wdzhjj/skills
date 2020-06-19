## Django 

### Django 基本命令
		1.新建一个工程 django project
			django-admin(.py) startproject project_name
			project_name 必须是合法的 python包名 不能为 1a 或a-b
		2.新建 app
			进入项目目录下 cd project_name 
			python manage.py startapp app_name
			或  django-admin.py startapp app_name
		
		3.创建数据库表  或 更改数据库表或字段
			创建更改的文件  python manage.py makemigrations
			生成的py 应用到数据库
				python manage.py migrate
			旧版本的Django 1.6及以下用
				python manage.py syncdb
		4.使用开发服务器
			方便调试和开发，但是由于性能问题，建议只用来测试，不要用在生产环境。
				python manage.py runserver
			端口被占 可以使用其他端口
				python manage.py runserver 9999
			监听机器所有可用 ip （电脑可能有多个内网ip或多个外网ip）
				python manage.py runserver 0.0.0.0:8000
		
		5.清空数据库
			python manage.py flush
		6.创建超级管理员
			python manage.py createsuperuser
			修改用户密码
				python manage.py changepassword username
		7.导入导出数据
			python manage.py loaddata appname.json
			python manage.py dumpdata appname > appname.json
		
		8.Django 项目环境终端
			python manage.py shell
			你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据，还有一些小测试非常方便。
		9.数据库命令行
			python manage.py dbshell
			Django 会自动进入在settings.py中设置的数据库
			在这个终端可以执行数据库的SQL语句。
		
		
### django 视图与网址
		1、新建一个项目 
			django-admin startproject mysite
			settings.py 文件，总的urls配置文件 urls.py 以及部署服务器时用到的 wsgi.py 文件， __init__.py 是python包的目录结构必须的，与调用有关。
		
		2、新建一个应用app
			python manage.py startapp learn
			
		3、将新定义的learn 加到 settings.py 的 INSTALL_APPS 中
			
		4、定义视图函数（访问页面时的内容）
			learn目录中的 views.py
			
			# coding:utf-8
			from django.http import HttpResponse
			def index(request):
				return HttpResponse("hello learn")
				
			引入HttpResponse，它是用来向网页返回内容的，就像Python中的 print 一样，只不过 HttpResponse 是把内容显示到网页上。	
			定义了一个index()函数，第一个参数必须是 request，与网页发来的请求有关
			
			
		5、定义视图函数相关的URl(网址)
			urls.py
				from learn import views as learn_views
					 新建立的项目 视图		别名
					 
				url(r'^$', learn_views.index)
			
		6、终端上运行
			python manage.py runserver
		
		7、打开浏览器访问
			python manage.py runserver 0.0.0.0:8000
				监听机器上所有ip 8000端口，访问时用电脑的ip代替 127.0.0.1
			
			
### 接收参数
		1、采用 /add/?a=4&b=5 GET接收
			from calc import views as calc_views
			views.py
				a = request.GET['a']
				b = request.GET['b']
			urls.py	
				path('add/', calc_views.add, name='add')
		
		2、采用 /add/3/4
				path('add/<int:a>/<int:b>', cal_views.add2, name='add2')
				name 可以用于在 templates, models, views ……中得到对应的网址，相当于“给网址取了个名字”，只要这个名字不变，网址变了也能通过名字获取到
				
			
### Django 模板
		views.py 写一个视图
			from django.shortcuts import render
			def home(request):
				return render(request, 'home.html')
		
		在 learn目录下新建一个 templates 文件夹，里面新建一个 home.html
			{% block title %} 默认标题 {% endblock %}
			{% include 'nav.html' %}
			{% block content %}
			<div>默认内容，继承这个模板的，不覆盖就显示</div>
			{% endblock %}
			
			block 继承模板可以重写的部分
			include 包含其他文件的内容 把一些网页共用的部分拿出来
			
			模板一般放在 app下的templates中，Django会自动去这个文件夹中找
			
### 模板内容展示
		1、显示一个基本的字符串
			views.py 中
			return render(request,'home.html',{'string':string})
			html中
				{{ string }}
			
		2、for循环list内容的展示
			list = ['html','css','js']
			return render(request,'home.html',{'list':list})
			
			{% for i in list %}
			{{ i }}
			{% endfor %}
			
			一般的变量之类的用 {{ }}（变量），功能类的，比如循环，条件判断是用 {%  %}（标签）
			
		3、显示字典
			{% for key ,value in info.items %}
				{{ key }}: {{ value }}
			{% endfor %}
			
		4、	模板中逻辑操作
			== , != , >= , <=, >, <
				{% if var >= 99 %}
				{% elif num<99 and num>60 %}
				{% else %}
				{% endif %}
			
			and, or, not, not in 
			
			
		5、获取	信息
			{{ request.user }}
			{{ request.path }}
			{{ request.GET.urlencode }}
			
			
### Django模型（数据库）
		修改 models.py	
			from django.db import models	
			
			class Person(models.model):
				name = models.CharField(max_length=30)
				age = models.IntegerField()
			
		创建数据库
			python manage.py makemigrations
			python manage.py migrate
			
		获取对象
			Person.objects.all()
			Person.objects.all()[:10] 切片 获取10个人，不支持负索引
			Person.objects.get(name=name)
			get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
			Person.objects.filter(name="abc") 
				等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
			Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人
			Person.objects.filter(name__icontains="abc")  #名称中包含 "abc"，且abc不区分大小写
			Person.objects.filter(name__regex="^abc")  # 正则表达式查询
			Person.objects.filter(name__iregex="^abc")  # 正则表达式不区分大小写
			filter是找出满足条件的，当然也有排除符合某条件的
			Person.objects.exclude(name__contains="WZ")  # 排除包含 WZ 的Person对象
			
			
### Django 数据库接口 QuerySet API
		1. QuerySet 创建对象的方法
			# 方法 1
			Author.objects.create(name="WeizhongTu", email="tuweizhong@163.com")
			 
			# 方法 2
			twz = Author(name="WeizhongTu", email="tuweizhong@163.com")
			twz.save()
			 
			# 方法 3
			twz = Author()
			twz.name="WeizhongTu"
			twz.email="tuweizhong@163.com"
			twz.save()
			 
			# 方法 4，首先尝试获取，不存在就创建，可以防止重复
			Author.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")
			# 返回值(object, True/False)

		2.删除符合条件的结果	
			Person.objects.filter(name__contains="abc").delete() # 删除 名称中包含 "abc"的人
			
			people = Person.objects.filter(name__contains="abc")
			people.delete()
			
		3. 更新某个内容
			*** 批量更新
				Person.objects.filter(name__contains="abc").update(name='xxx')
				 # 名称中包含 "abc"的人 都改成 xxx
				Person.objects.all().delete() # 删除所有 Person 记录
			
			*** 单个 object 更新，适合于 .get(), get_or_create(), update_or_create() 等得到的 obj，和新建很类似。
				twz = Author.objects.get(name="WeizhongTu")
				twz.name="WeizhongTu"
				twz.email="tuweizhong@163.com"
				twz.save()  # 最后不要忘了保存！！！
		
		4.QuerySet 是可迭代的
			es = Entry.objects.all()
			for e in es:
				print(e.headline)
			Entry.objects.all() 或者 es 就是 QuerySet 是查询所有的 Entry 条目。
			
		5. QuerySet 查询结果排序	
			Author.objects.all().order_by('name')
			Author.objects.all().order_by('-name') # 在 column name 前加一个负号，可以实现倒序
			
		6.QuerySet 支持链式查询
			Author.objects.filter(name__contains="WeizhongTu").filter(email="tuweizhong@163.com")
			Author.objects.filter(name__contains="Wei").exclude(email="tuweizhong@163.com")
			 
			# 找出名称含有abc, 但是排除年龄是23岁的
			Person.objects.filter(name__contains="abc").exclude(age=23)
		
		7.QuerySet 重复的问题，使用 .distinct() 去重
			qs = qs.distinct()
		
		
#### django querySet 进阶
		1、查看Django queryset 执行的SQL
			print str(Author.objects.all().query)
			print str(Author.objects.filter(name="WeizhongTu").query)
		2. values_list 获取元组形式结果
			authors = Author.objects.values_list('name', 'qq')
		
		
		
		
		
####  过滤器
		{{ value|filter }}
		如： {{ list_nums|length }}
		可叠加 {{ value|filter1|filter2 }}
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		