# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

postive_number_count = 0
for number in numbers:
    if number > 0:
        postive_number_count+= 1
print(f'Final count of positive numbers is: {postive_number_count}')