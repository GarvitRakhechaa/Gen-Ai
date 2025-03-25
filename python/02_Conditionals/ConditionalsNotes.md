## ✅ **Conditionals in Python (if-elif-else)**
Python me **Conditionals** ka use **decision-making** ke liye hota hai.  
Agar kisi **particular condition** ko check karke **different actions** execute karne ho, tab hum `if`, `elif`, aur `else` ka use karte hain.  

---

## 📌 **1. `if` Statement (Simple Condition)**
Agar condition `True` hai to **if-block** execute hoga.  

### 🔍 **Example:**
```python
age = 18

if age >= 18:
    print("You are eligible to vote!")
```
✅ Output: `You are eligible to vote!`

---

## 📌 **2. `if-else` Statement (Two Conditions)**
Agar `if` condition **False** ho, tab `else` block execute hoga.  

### 🔍 **Example:**
```python
num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
✅ Output: `Even number`

---

## 📌 **3. `if-elif-else` (Multiple Conditions)**
Agar ek se zyada conditions ho, to **`elif` (else if)** ka use karte hain.  
Agar koi bhi `if` ya `elif` `True` nahi hota, to `else` block execute hota hai.  

### 🔍 **Example:**
```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```
✅ Output: `Grade: B`

---

## 📌 **4. Nested `if` (if ke andar if)**
Agar ek condition ke andar bhi condition check karni ho to **nested `if`** use karte hain.  

### 🔍 **Example:**
```python
num = 15

if num > 0:
    print("Positive number")
    if num % 5 == 0:
        print("Divisible by 5")
```
✅ Output:
```
Positive number
Divisible by 5
```

---

## 📌 **5. Short-Hand `if` (One-Liner If Statement)**
Agar ek hi statement execute karna ho to **short-hand `if`** likh sakte hain.  

### 🔍 **Example:**
```python
x = 10
if x > 5: print("x is greater than 5")
```
✅ Output: `x is greater than 5`

---

## 📌 **6. Short-Hand `if-else` (Ternary Operator)**
Python me ternary operator `if-else` ko ek hi line me likhne ke liye use hota hai.  

### 🔍 **Example:**
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```
✅ Output: `Adult`

---

## 📌 **7. `pass` Statement (Empty `if` Block)**
Agar aap `if` ke andar koi action nahi likhna chahte ho, to `pass` keyword use hota hai.  

### 🔍 **Example:**
```python
x = 10
if x > 5:
    pass  # Placeholder (No action performed)
print("This will still execute!")
```
✅ Output: `This will still execute!`

---

## 🔥 **Important Points:**
1. **Python me indentation (`Tab` ya `Space`) compulsory hota hai.**  
2. **`if` condition me `:` (colon) lagana zaroori hai.**  
3. **Ternary operator ek line me if-else likhne ke liye hota hai.**  
4. **`pass` ka use empty blocks ke liye hota hai.**  

---

