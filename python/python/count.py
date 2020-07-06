rate = 0.15
amount = 12000
year = 11
sum = 0
for i in range(1,year):
    sum += amount+sum*rate
    print(sum)
