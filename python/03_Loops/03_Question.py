# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("enter number which you  want to print a table:"))
multi = 1
for i in range(1,11):
    if i == 5:
        continue
    multi = number * i
    print(multi)


