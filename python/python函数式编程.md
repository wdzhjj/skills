#### 高阶函数
		abs				<built-in function abs>
		abs(-10)	是函数调用
		abs 		是函数本身
		函数本身也可以赋值给变量		f = abs
		f(-10)		可以调用函数 说明变量f指向了abs函数本身
		
		函数名也是变量
		当把函数名指向其他对象，无法继续调用函数
		
		传入函数
			变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接受另一个函数作为参数
		=》 高阶函数
		f = abs
		def add(x,y,f):
			return f(x)+f(y)
			
		=> f(x) + f(y) = abs(x) + abs(y) 	
		
		
#### map/reduce
		map()函数接受两个参数，一个是函数，一个是Iterable，map将传入的函数一次作用到序列的每个元素，并把结果作为新的Iterator返回
		
		def f(x):
			return x*x
		r = map(f,[1,2,3,4,5,6,7,8,9])	
		>>> list(r)
		[1,4,9,16,25,36,49,64,81]
		
		把list所有数字转为字符串
		>>> list(map(str,[1,2,3,4,5,6,7,8,9]))
		['1','2','3','4','5','6','7','8','9']
		
		
		reduce 把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接受两个参数，reduce把结果
		和序列的下一个元素做累积计算
			redece(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
			
		def add(x,y):
			return x + y
		>>>reduce(add,[1,3,5,7,9])                  # 1+3+5+7+9
		>>>25
		
		
#### filter
		filter 用于过滤序列
		filter()接收一个函数和一个序列，把 传入的函数一次作用于每个元素，然后根据返回值是
		True还是False决定保留还是丢弃该元素
			def is_odd(n):
				return n % 2 == 1
			
			list(filter(is_odd,[1,2,4,5,6,9,10,15]))		#单数返回值为1 
		=>	[1,5,9,15]		
		
		
#### 匿名函数
		在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数
			lambda x: x*x
			相当于
			def f(x):
				return x*x
		
		关键字lambda表示匿名函数，冒号前面的x表示函数参数
		只能有一个表达式，不用写return，返回值就是该表达式的结果
		因为函数没有名字，不必担心函数名冲突
		匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
			f = lambda x: x*x
			f(5)  => 25
		
#### 装饰器
		比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，成为 装饰器 （Decorator）
		本质上，decorator就是一个返回函数的高阶函数
		定义打印日志函数
			def log(func):
				def wrapper(*args,**kw):
					print(func.__name__)
					return func(*arg,**kw)
				return wrapper	
			
			@log
			def now():
				print("2019")
		
		调用now函数，不仅会运行now本身，还会运行
			now = log(now)
			
		
#### 偏函数 Partial function
		import functools
		int2 = functools.partial(int,base=2)
		相当于
			def int2(x,base=2):
				return int(x,base)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		