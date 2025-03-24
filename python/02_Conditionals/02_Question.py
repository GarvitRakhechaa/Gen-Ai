# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter age: "))
day = input("Enter day: ")

if age<18:
    if day == 'Wednesday':
        print("price is 6$ for you child")
    else:
        print("price is 8$ for you child")
else:
    if day == 'Wednesday':
        print("price is 10$ for you Sir/Mam")
    else:
        print("price is 12$ for you Sir/Mam")
