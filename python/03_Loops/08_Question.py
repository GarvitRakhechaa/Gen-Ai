# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = int(input("enter a number: "))
is_prime = 0

for i in range(2, number):
    if number%i == 0:
        is_prime = 1

if is_prime == 0:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
    