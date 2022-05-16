# bounce.py
#
# Exercise 1.5

drop = 100
for i in range(1, 11):
    drop = drop * 0.6
    print(i , round(drop, 4))
