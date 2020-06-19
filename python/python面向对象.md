#### 类和实例	Class Instance
		定义类
			class Student(object):
				pass
		(object) 表示继承哪个类，如果没有合适的继承类，就是object类。3新特性，拥有更多的属性		
		
		创建实例：	
		bart = Student()
		变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。
		特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
		def __init__(self,name,score):
			self.name = name
			self.score = score
		__init__ 的第一个参数永远是self 表示创建的实例本身	
		
		Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
		

#### 继承和多态
		在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
		class Animal(object):
			def run(self):
				print('Animal is running...')
		class Dog(Animal):
			pass

		class Cat(Animal):
			pass
			
		子类获得了父类的全部功能
			dog = Dog()
			dog.run()
		
		子类重写run方法 ，运行最近的方法 =》多态
		判断一个变量是否是某个类型可以用isinstance()判断	
			dog 是 Dog 也是 Animal
			
			
#### 获取对象信息
		type() 			判断对象类型
		isinstance()	一个对象是否是某种类型	
			换句话说，isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
		dir()				
			如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
		dir('ABC')
		['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

			
#### @property
		Python内置的@property装饰器就是负责把一个方法变成属性调用的：
		@property
		def score(self):
			return self._score

		@score.setter
		def score(self, value):
			if not isinstance(value, int):
				raise ValueError('score must be an integer!')
			if value < 0 or value > 100:
				raise ValueError('score must between 0 ~ 100!')
			self._score = value			
		@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作		
			

			
			
			
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		