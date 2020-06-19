sum = 242+600
p1 = 89
p2 = 129
p3 = 169

for i in range(0,10):
	for j in range(0,10):
		for k in range(0,10):
			if (p1*i + p2*j + p3*k < sum):
				rest = sum-p1*i-p2*j-p3*k
				if(rest<p1):
					print(i,j,k)
					print("rest of sum is:",rest)
					print('\n')

