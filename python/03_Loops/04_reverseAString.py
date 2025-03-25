# 4. Reverse a String
# Problem: Reverse a string using a loop.

string = input("enter")
reverseString = ""

for char in string:
    reverseString = char + reverseString

print(reverseString)
