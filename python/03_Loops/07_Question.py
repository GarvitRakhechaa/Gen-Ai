# 7 . Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

number = int(input("enter a valid number"))

while True:
    if number< 11 >0:
        print("you enterd valid number")
        break
    else:
        number = int(input("enter a number again"))

