# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def circle(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area, circumference

ar , cr = circle(1)
print(f'{ar:.2f}')
print(f'{cr:.2f}')


