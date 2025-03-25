# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["banana","apple", "banana", "orange", "apple", "mango"]

g = iter(items)

for item in items:
    # print(g.__next__())
    if items.count(item) > 1:
        print(item)
        break

