# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter age: "))
if age<13:
    print("you are child")
elif age >= 13 and age <20:
    print("you are teenager")
elif age >= 20 and age <60:
    print("you are adult")
else:
    print("you are Senior")
    