#### python高级特性
#### 切片
		取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
			>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
		L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
		如果第一个索引是0，还可以省略： >>> L[:3]
		L[-1]取倒数第一个元素
		什么都不写，只写[:]就可以原样复制一个list：
		
		tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
		>>> (0, 1, 2, 3, 4, 5)[:3]
		(0, 1, 2)

		字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

		>>> 'ABCDEFG'[:3]
		'ABC'
		>>> 'ABCDEFG'[::2]
		'ACEG'

				
#### 迭代
		判断对象是否可以迭代
		form collections import Interable
		isinstance('abc', Interable)
		Ture
		isinstance([1,2,3],Interable)
		Ture
		isinstance(123, Interable)
		False
		
#### 列表生成式
		列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
		要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
		
		但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
			>>> L = []
			>>> for x in range(1, 11):
			...    L.append(x * x)
			...
			>>> L
		但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
			>>> [x * x for x in range(1, 11)]
			[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		