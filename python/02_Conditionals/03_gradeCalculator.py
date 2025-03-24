# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

marks = int(input("enter your score"))

if marks>= 90 <= 100:
    print("A")
elif marks >= 80 < 90:
    print("B")
elif marks >= 70 < 80:
    print("C")
elif marks >= 60 < 70:
    print("D")
else:
    print("F")
