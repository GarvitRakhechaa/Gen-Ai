# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

n = int(input("enter a number: "))
cube = lambda n: n **3
print(cube(n))