import sys

def bubble_sort(list,n):
	for j in range(0,n-1):
		for i in range(0,n-1-j):
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp

	print(list)		


def select_sort(list,n):
	for i in range(0,n-1):
		max = 0	
		for j in range(0,n-1-i):
			if(list[j]>max):
				max = list[j]
				pos = j		
		list[pos] = list[n-1-i]
		list[n-1-i] = max
	print(list)

def insert_sort(list,n):	
	for i in range(n,0,-1):		  # 长度12  只需要运行11 次 从大到小排列 每次运行次数加一
		for j in range(0,n-i):	  # 从 1 开始 第二个数
			if list[j]>list[n-i]:	# 后一位小于前一位时交换位置
				temp = list[j]
				list[j] = list[n-i]
				list[n-i] = temp
				break	
	print(list)


if __name__ == '__main__':
	list = [6,5,17,1,22,3,2,9,8,4,7,15]
	# bubble_sort(list,len(list))
	# select_sort(list,len(list))
	insert_sort(list,len(list))