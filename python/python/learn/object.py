class wdz(object):
	# __init__ 是一个特殊方法用于在创建对象时进行初始化操作
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def like(self,likes):
		print(self.name + ' at ' + str(self.age) +' like '+likes)

	#访问可见性
	def __foo(self):
		print('it,s foo')

	#property 装饰器	
	#使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
	@property
	def foo(self):
		return self._foo

	@foo.setter
	def foo(self):
		self.foo = 'foo'	
	
	# __slots__ 魔法
	# 限定Person对象只能绑定 _name,_age和_gender属性
	__slots__ = ('_name','_age','_gender')


def main():
	me = wdz('wdz',28)
	me.like('swimming')

if __name__ == '__main__':
	main()			