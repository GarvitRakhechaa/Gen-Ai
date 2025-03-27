## **Python Scopes and Closures – Hinglish Notes** 🚀  

Python me variables alag-alag **scope** (range) me kaam karte hain, aur **closure** ek special concept hai jo nested functions ke sath kaam karta hai.  

---

## **1️⃣ Scope in Python**  
Scope ka matlab hai **variable ka area of accessibility** (kab aur kahan use ho sakta hai).  

### **Types of Scope:**  
1. **Local Scope** – Function ke andar define kiya gaya variable.  
2. **Enclosing Scope (Non-Local)** – Nested function ke andar ka variable.  
3. **Global Scope** – Pure program me accessible variable.  
4. **Built-in Scope** – Python ke predefined functions aur variables.  

---

## **2️⃣ Global Scope Example**  
```python
username = "chaiaurcode"  # Global Variable

def func():
    print(username)  # Global variable ko access kar sakte hain

print(username)  # Output: chaiaurcode
func()          # Output: chaiaurcode
```
📌 **Global variable function ke andar bhi accessible hota hai (agar overwrite na kiya ho).**  

---

## **3️⃣ Local Scope Example**  
```python
def func():
    username = "chai"  # Local Variable
    print(username)

func()  
# print(username)  # Error aayega kyunki local variable function ke bahar accessible nahi hai
```
📌 **Function ke andar define variable sirf usi function me kaam karega.**  

---

## **4️⃣ Enclosing Scope (Nonlocal Scope) – Nested Functions**  
```python
def f1():
    x = 88  # Enclosing Variable
    def f2():
        print(x)  # f2() function x ko access kar sakta hai
    return f2

myResult = f1()  
myResult()  # Output: 88
```
📌 **f2() function f1() ke `x` variable ko access kar sakta hai, kyunki wo enclosing scope me hai.**  

---

## **5️⃣ Global Keyword – Function me Global Variable Change Karna**  
```python
x = 99  # Global Variable

def func3():
    global x  # Global variable ko modify karne ke liye 'global' use karna padega
    x = 12

func3()
print(x)  # Output: 12
```
📌 **Agar `global` keyword use nahi karenge, toh function ek naya local variable banayega.**  

---

## **6️⃣ Closure in Python**  
Closure ek **function ke andar function** hota hai jo **outer function ke variables ko yaad rakhta hai** even after function execute ho chuka hota hai.  

```python
def chaicoder(num):
    def actual(x):
        return x ** num  # num ko yaad rakhta hai
    return actual  # Function return kar raha hai

f = chaicoder(2)  # num = 2
g = chaicoder(3)  # num = 3

print(f(3))  # 3^2 = 9
print(g(3))  # 3^3 = 27
```
📌 **Closure ke wajah se `num` ki value yaad rehti hai even after chaicoder function khatam ho jata hai.**  

---

## **📌 Summary**  
✅ **Local Scope** – Function ke andar ka variable sirf function me accessible hota hai.  
✅ **Global Scope** – Pure program me accessible hota hai, par function ke andar change karne ke liye `global` keyword chahiye.  
✅ **Enclosing Scope (Nonlocal)** – Nested function outer function ke variable ko access kar sakta hai.  
✅ **Closures** – Function ke andar function hota hai jo outer function ke variables ko yaad rakhta hai.  

