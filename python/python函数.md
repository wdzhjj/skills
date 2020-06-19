#### python 函数
		abs(x) 返回绝对值
		通过help(abs)查看abs函数的帮助信息
		而max函数max()可以接收任意多个参数，并返回最大的那个
		
		数据类型转换
		Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
		函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
		>>> a = abs # 变量a指向abs函数
		>>> a(-1) # 所以也可以通过a调用abs函数
		
		*****定义函数
		定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
		def my_abs(x):
		if x >= 0:
			return x
		else:
			return -x
		
		把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）
		
		
		*****空函数
			如果想定义一个什么事也不做的空函数，可以用pass语句：
			def nop():
				pass
			实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
		
		*****参数检查
		调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
		但是如果参数类型不对，Python解释器就无法帮我们检查。
		当传入了不恰当的参数时，会导致if语句出错，出错信息和abs不一样，对参数类型做检查，只允许整数和浮点数类型的参数
		数据类型检查可以用内置函数isinstance()实现
		
		*****返回多个值
		import math
		def move(x, y, step, angle=0):
			nx = x + step * math.cos(angle)
			ny = y - step * math.sin(angle)
			return nx, ny
			
		import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
		Python的函数返回多值其实就是返回一个tuple
		
		小结

		定义函数时，需要确定函数名和参数个数；

		如果有必要，可以先对参数的数据类型做检查；

		函数体内部可以用return随时返回函数结果；

		函数执行完毕也没有return语句时，自动return None。

		函数可以同时返回多个值，但其实就是一个tuple。
		


#### 函数的参数
		多个参数
			power(x, n)
		***默认参数
			power(x, n=2)
		一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
		二是如何设置默认参数。	
		当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
		定义默认参数要牢记一点：默认参数必须指向不变对象！ 
		
		***可变参数
		def calc(*numbers)
			sum = 0
			for n in numbers
				sum = sum + n * n
			return sum
		*nums表示把nums这个list的所有元素作为可变参数传进去。
		
		***关键字参数
		可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
		def person(name, age, **kw):
			print('name:', name, 'age:', age, 'other:', kw)
		
		***命名关键字参数
		对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数
		def person(name, age, **kw):
			if 'city' in kw:
				# 有city参数
				pass
			if 'job' in kw:
				# 有job参数
				pass
			print('name:', name, 'age:', age, 'other:', kw)
		
		*****参数组合
		在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
		
		
		小结

		Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

		默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

		要注意定义可变参数和关键字参数的语法：

		*args是可变参数，args接收的是一个tuple；

		**kw是关键字参数，kw接收的是一个dict。

		以及调用函数时如何传入可变参数和关键字参数的语法：

		可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

		关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

		使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

		命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

		定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
		
		
		
#### 高阶函数
		map/reduce
		Python内建了map()和reduce()函数。
		map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
		>>> def f(x):
		...     return x * x
		...
		>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
		>>> list(r)
		[1, 4, 9, 16, 25, 36, 49, 64, 81]
				
		reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
		>>> from functools import reduce
		>>> def add(x, y):
		...     return x + y
		...
		>>> reduce(add, [1, 3, 5, 7, 9])
		25

		**filter
		Python内建的filter()函数用于过滤序列。
		filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
		def is_odd(n):
			return n % 2 == 1
		list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
		
		**sorted
		排序算法
		Python内置的sorted()函数就可以对list进行排序：
		>>> sorted([36, 5, -12, 9, -21])
		[-21, -12, 5, 9, 36]
		
		sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
		>>> sorted([36, 5, -12, 9, -21], key=abs)
		[5, 9, -12, -21, 36]
		计算绝对值后排序返回list
		
		我们给sorted传入key函数，即可实现忽略大小写的排序
		>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
		['about', 'bob', 'Credit', 'Zoo']
		要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
		>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
		['Zoo', 'Credit', 'bob', 'about']
		
		
		
		
		
		
		
###  Python 内置函数
		abs()			abs() 函数返回数字的绝对值。
		all()			用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
						元素除了是 0、空、FALSE 外都算 TRUE。
		any() 			用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
		ascii()			类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 	函数使用 \x, \u 或 \U 编码的字符。
		bin()			返回一个整数 int 或者长整数 long int 的二进制表示。
		bool()			函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
		bytearray()		方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
		bytes()			函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。
		callable()		函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。 
		chr()			用一个整数作参数，返回一个对应的字符。
		classmethod()	修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
		compile() 		函数将一个字符串编译为字节代码。
		delattr() 		函数用于删除属性。delattr(x, 'foobar') 相等于 del x.foobar。
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		