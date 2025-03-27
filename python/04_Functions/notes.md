# **Python Functions – Complete Notes** 🚀  

## **1️⃣ Basic Function Syntax**  
🔹 Function ek **reusable block of code** hota hai jo koi specific kaam karta hai.  

### **Syntax:**  
```python
def function_name(parameters):
    return value
```

### **Example:**  
```python
def square(num):
    return num * num
```
🟢 **`square(4)` → Output: 16**  

---

## **2️⃣ Function with Multiple Parameters**  
🔹 Function **multiple inputs le sakta hai** aur result return kar sakta hai.  

### **Example:**  
```python
def add(a, b):
    return a + b
```
🟢 **`add(5, 3)` → Output: 8**  

---

## **3️⃣ Polymorphism in Functions**  
🔹 **Ek hi function alag-alag data types pe kaam kar sakta hai.**  

### **Example:**  
```python
def multiply(x, y):
    return x * y

print(multiply(3, 4))      # Output: 12
print(multiply("Hello", 3)) # Output: HelloHelloHello
```
📌 **Agar number diye toh multiply, string diye toh repeat karega!**  

---

## **4️⃣ Function Returning Multiple Values**  
🔹 **Function ek se zyada values return kar sakta hai (tuple form me).**  

### **Example:**  
```python
import math

def circle_properties(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

print(circle_properties(5))
```
🟢 **Output:** `(78.54, 31.42)` (Area, Circumference)  

---

## **5️⃣ Default Parameter Value**  
🔹 **Agar argument na diya jaye, toh ek default value use hogi.**  

### **Example:**  
```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())       # Output: Hello, Guest!
print(greet("John")) # Output: Hello, John!
```

📌 **Agar koi naam nahi diya, toh "Guest" ko use karega.**  

---

## **6️⃣ Lambda Function (One-line Function)**  
🔹 **Chhoti functions likhne ke liye ek single-line anonymous function.**  

### **Example:**  
```python
cube = lambda x: x ** 3
print(cube(3))  # Output: 27
```
📌 **Normal function ke bina hi ek line me kaam ho gaya!**  

---

## **7️⃣ Function with `*args` (Variable Arguments)**  
🔹 **Jitne chahe utne arguments pass kar sakte hain (tuple me store hote hain).**  

### **Example:**  
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4)) # Output: 10
```
📌 **Aap jitne chahe numbers pass kar sakte ho!**  

---

## **8️⃣ Function with `**kwargs` (Keyword Arguments)**  
🔹 **Named arguments ka use karke flexible function likh sakte hain.**  

### **Example:**  
```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25, city="New York")
```
🟢 **Output:**  
```
name: Alice
age: 25
city: New York
```
📌 **Jitne bhi keyword arguments pass karoge, function accept karega!**  

---

## **9️⃣ Generator Function with `yield`**  
🔹 **`yield` se function ek ek value return karta hai bina memory zyada use kiye.**  

### **Example:**  
```python
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)
```
🟢 **Output:** `2 4 6 8 10`  
📌 **Ek saath sab return karne ki jagah ek ek karke deta hai.**  

---

## **🔟 Recursive Function**  
🔹 **Function jo khud ko call kare jab tak base condition na mile.**  

### **Example:**  
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # Output: 120
```
📌 **Factorial ka formula: `n! = n * (n-1)!`**  

---

### **📌 Summary:**  
✅ Functions reuse karne ke liye useful hote hain.  
✅ `*args` multiple values leta hai (tuple me).  
✅ `**kwargs` named values leta hai (dictionary me).  
✅ `lambda` ek line me function likhne deta hai.  
✅ `yield` se ek ek value return hoti hai (memory efficient).  
✅ Recursion tab tak chalega jab tak base case nahi milta.  

---
