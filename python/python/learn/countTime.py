'''
income = 0
incre = 1.2
come_incre = 5000 
sum = 30000
for x in range(1,10):
	sum = sum * incre + income
	income = 20000 + 5000*x
	print(sum)	
'''
import time
start = time.perf_counter()
for i in range(1,pow(2,20)):
	i = i+1
end = time.perf_counter()
print(end-start)	