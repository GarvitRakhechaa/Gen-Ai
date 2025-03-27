# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.


def fact(n):
    if n>1:
        return n * fact(n-1)
    elif n == 0 or 1:
        return 1
    
print(fact(5))

    


