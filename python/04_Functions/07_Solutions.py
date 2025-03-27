# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args): 
    sums = 0
    # args like an array
    # we can do this also 
    for i in args:
        sums = sums +i
    return sums

print(sum_all(1))
print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5))
