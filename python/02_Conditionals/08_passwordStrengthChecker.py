# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "Garvit@12312234"
if len(password)< 6:
    print("Password is Week")
elif len(password) <10 >=6:
    print("Password is Medium")
else:
    print("Password is Strong")