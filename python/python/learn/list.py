# list 操作

def main():
	list1 = [1,3,5,7,100]
	print(list1)
	list2 = ['hello'] * 5 			# 复制5次 每次一个元素
	print(list2)

	#计算列表长度
	len(list1)
	# 下标(索引)运算
	print(list1[0])
	print(list1[-1])
	# list1[2] = 300		修改元素
	print(list1)

	# 添加元素
	list1.append(200)
	list1.insert(0,400)
	print(list1)

	#删除元素
	list1.remove(3) 		# 非下标
	print(list1)

	del list1[0]
	del list1[-1]
	print(list1)

	# 清空list
	list1.clear()
	print(list1)


	# 排序
	new = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
	news = sorted(new)
	# print(news)
	# sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
	# news = sorted(new,reverse=True)
	# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    # news = sorted(new,key=len)



if __name__ == '__main__':
		main()	