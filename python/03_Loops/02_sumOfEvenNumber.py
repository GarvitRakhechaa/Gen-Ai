# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

number = int(input("enter number till you want to summ of even number:"))
sum = 0
for i in range(1, number+1):
    if i%2 == 0:
        sum = sum+i
print(f"sum of even number till {sum}")

