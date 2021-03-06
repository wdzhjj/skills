# 简单选择排序

def select_sort(origin_items,comp=lambda x, y:x < y):
	items = origin_items[:]
	for i in range(len(items) -1):
		min_index = 1
		for j in range(i+1, len(items)):
			if comp(items[j], items[min_index]):
				min_index = j
		items[i],items[min_index] = items[min_index],items[i]
	return items		
