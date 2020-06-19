from myUtil import myUtil
import time
import logging
import json

logging.basicConfig(level=logging.INFO)    #logging的配置
#记录级别  有  debug  info warning error  
#指定INFO  debug就不起作用了   指定 warning后   debug和info就不起作用


m = myUtil()
p = print
#列表
list = ['sdfsdf','sfe','12dsf'];


list.pop(0)        
m.p(list)

#元祖
tuple = ('123','q123','qq1234')
tuple2 = ('123',)     #  逗号 表示一个元素  
m.p(tuple)

#字典
d = {'wdz':29,'wxx':28,'hjj':89}
m.p(d['wdz'])

#集合
s = set([1,2,3])
m.p(set)

m.p(max(1,854,15,-484,118,1234))

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)	

# fact = fact(50)
# m.p(fact)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
p(L[0:3])

# isinstance('adffdsf',Iterable)  是否可以迭代

# g = (x * x for x in range(1,11))
# for n in g:
# 	print(n)

p(sorted([36,5,0,-9,81,-15]))

f = lambda x : x*(x+x)
p(f(5))




def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

def test(func):
	def wrapper(*args, **kw):
		print(time.time())
		return func(*args, **kw)
	return wrapper

@test
def now():
    print('123')

now()




# __slots__  限制实例的属性
class Student(object):
	__slots__ = ('name','sex')

# s = Student()
# s.name='wdz'
# print(s.name)
# s.tt = 'wwe'	  # not ok

logging.info('its ok from now')


list = ['12321','sdfdsf','223','wdz']

print(json.dumps(list))
