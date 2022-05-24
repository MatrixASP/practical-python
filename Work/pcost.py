# pcost.py
#
# Exercise 1.27

import os
print (os.getcwd())
'''
with open('Work/Data/missing.csv') as data:
    headers = next(data).split('.')
    total_cost = 0.0
    cost = 0.0
    #debugPrn - peek a boo at the header
    #print (headers)
    for line in data:       
        # print(line.split(','))
        stock = line.split(',')
        try:
            cost = int(stock[1]) * float(stock[2])
            total_cost += cost
        except : 
            print(f'ERROR ... missing value in the data for  stock: {stock[0]}')
        #print(cost)
        # foramt print Stock - numBought - pricePer - totalCost
        #print(f'stock-{stock[0]} num-{stock[1]} price/per-{stock[2]}  cost-{cost}')

    print (f"The total cost to buy all stocks is: {total_cost}")
        # print(line.split(','), end="")

'''

## VERSION 2 using CSV modulo

import csv
#print(os.getcwd())

with open('Work/Data/missing.csv') as f:
    
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0.0
    cost = 0.0
    #debugPrn - peek a boo at the header
    print ('Using CSV module \n : headers --->', headers)
    for row in rows:
        try:
            #cost = int(row[1]) * float(row[2])
            t = (row[0], int(row[1]), float(row[2]))
            cost = t[1] * t[2]
            total_cost += cost
        except BaseException:
            print(
                f'ERROR ... missing value in the data for  stock: {t[0]}')
        
    print(f"The total cost to buy all stocks is: {total_cost}")
    # print(line.split(','), end="")
