stock_price = 8.35
stock_num = 15400
debt = 3000 + 15000 + 20000 + 43000
month = 2
rent = 1650 * month
working_day = 12
salary = 5850 + int(working_day/23*6000)

my_stock = int(stock_price * stock_num)
my_property = my_stock + salary
my_debt = my_property - debt - month * rent
print('股票价值',my_stock)
print('工资',salary)
print('负债',debt)
print(my_debt)

if my_debt > 50000:
    print('资产')
else:
    print('负债')
print(my_debt-50000)

