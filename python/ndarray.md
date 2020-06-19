#### ndarray
	引用：
		import numpy as np
	数组创建方法
	1、从Python中的列表、元祖等类型创建ndarray数组
		x = np.array(list/tuple)
		x = np.array(list/tuple,dtype=np.float32)
		
	2、使用NumPy函数创建ndarray 数组
		np.arange(n) 		类似range()函数，返回ndarray类型元素从0到n-1
		np.ones(shape)		根据shape生成一个全1数组，shape是元祖类型
		np.zeros(shape)		根据shape生成一个全0数组，shape是元祖类型
		np.full(shape,val)	根据shape生成一个数组，每个元素值都是val
		np.eye(n)			创建一个正方的n*n单位矩阵，对角线为1，其余为0
		
		np.ones_like(a)		根据数组a的形状生成一个全1数组
		np.zeros_like(a)	根据数组a的形状生成一个全0数组
		np.full_like(a,val)	根据数组a的形状生成一个数组，每个元素值都是val
		
		np.linspace()		就跟起止数据等间距地填充数据，形成数组
		np.concatenate()	将两个或多个数组合并成一个新的数组
		
	3、数组变换维度
		.reshape(shape)		不改变数组元素，返回一个shape形状的数组
		.resize(shape)		与.reshape()功能一致，但修改原数组
		.swapaxes(ax1,ax2)	将数组n个维度中两个维度进行调换
		.flatten()			对数组进行降维，返回折叠后的以为数组。原数组不变
		
		
	4、NumPy一元函数
		np.abs(x)np.fabs(x)		计算数组各元素的绝对值
		np.sqrt(x)				计算数组各元素的平方根
		np.square(x)			计算数组各元素的平方
		np.log(x)|np.log10(x)	计算数组各元素的自然对数，10底对数
		np.ceil(x) np.floor(x)	计算数组各元素的ceiling或floor值
		np.rint(x)								四舍五入值
		np.modf(x)								的小数和整数部分以两个独立数组形式返回
		np.cos(x)	np.cosh(x)	
		np.sin(x)				计算各元祖的普通型和双曲型三角函数
		np.tan(x)
		
		np.exp(x)								指数值
		np.sign(x)								符号值 1(+) 0 -1(-)
	
	5、np.random的随机数函数
		rand(d0,d1,...dn) 		根据d0-dn创建的随机数数组，浮点数，【0,1） 均匀分布
		randn(d0,d1,...dn)		标准正态分布
		randint（low[,high,shape]）	根据shape创建随机整数或整数数组，范围是[low,high)
		seeds(s)				随机数种子，s是给定的种子值
		
		
#### CSV文件
		np.savetxt(frame,array,fmt='%.18e',delimiter=None,uppack=False)
		frame:	文件、字符串或产生器，可以是.gz或.bz的压缩文件
		array:	存入文件的数组
		fmt：	写入文件的格式，如：%d %.2f %.18e
		unpack:	如果True 读入属性将分别写入不同变量
		
		np.fromfile(frame,dtype=float,count=-1,sep="")
		frame:	文件、字符串
		dtype： 读取的数据类型
		count:	读取元素个数，-1表示读入整个文件
		sep：	数据分割字符串，如果是空串，写入文件为二进制
		
		NumPy 便捷文件存取
			np.save(fname,array)    np.savez(fname,array)
			np.load(frame)				
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		