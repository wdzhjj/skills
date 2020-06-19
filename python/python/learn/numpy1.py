#encoding = utf-8
import numpy as np

def main():
	lst = [ [1,3,5,7],[2,6,12,24] ]
	print(type(lst))
	arr = np.array(lst)
	# arr = np.array(lst,dtype=np.float)

	# # bool,int,int8,int16,int32,int64,int128,uint8~uint128,float..
	# print(arr.shape)			#几行几列
	# print(arr.ndim)				#维度
	# print(arr.dtype)
	# print(arr.itemsize)
	# print(arr.size)	
	# print(np.zeros([2,4]))			## 2行4列的0值数组
	# print(np.ones([6,3]))
	# print(np.random.rand(2,4))		## 随机数 float 0~1
	# random.randint(1,10,3)   ##随机整数 范围+间隔
	

if __name__ == '__main__':
	main()	