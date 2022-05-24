# pcost.py
#
# Exercise 1.27

import os
#debugtest
print(os.getcwd())


# def sumcount(n):
#     total = 0
#     for num in range(n + 1):
#         total += num
#     return total


# print(sumcount(100))


# def greeting(name):
#     ' Ssues a greeting with thew name provided.'
#     print(f'HELLO {name} !!!')


# greeting('Baby')


def portfolio_cost(fname):
    with open(fname) as data:
        headers = next(data).split('.')
        total_cost = 0.0
        cost = 0.0
        #  -- headers
        #print(headers)
        for line in data:
            # print(line.split(','))
            stock = line.split(',')
            # tryna catch error(s) for missing data fields
            try:
                cost = int(stock[1]) * float(stock[2])
                total_cost += cost
            except ValueError:
                print(f'ERROR:  ... missing value in the data for  stock: {stock[0]}')
            # print(cost)n

            # debugtest : stockname - number - price - totalcost
            #print( f' stock-{stock[0]} num-{stock[1]} price/per-{stock[2]}  cost-{cost}')
    return total_cost
   # print(f"The total cost to buy all stocks is: {total_cost}")
    # print(line.split(','), end="")

# filename = 'Work/Data/portfolio.csv'
filename = 'Work/Data/missing.csv'
cost = portfolio_cost(filename)
print ('TOTOL COST::: ', cost)