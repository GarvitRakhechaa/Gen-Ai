# Everything is Object in Python

Haan, bilkul! Yeh Python ka **fundamental concept** hai. Samajhne ke liye thoda detail me dekhte hain.  

---

## 📚 **Python me Har Cheez Object Hi Hai**  

Python ek **Object-Oriented Programming Language (OOP)** hai, jiska matlab hai ki **Python me har cheez ek object hota hai.**  

### 🔍 **Iska Matlab Kya Hai?**  
- **Python me sab kuch objects ke form me store hota hai.**  
- Har object ke paas **ek type (class)** hota hai, **ek identity (unique memory address)** hota hai, aur **ek value (actual data)** hota hai.  
- Har object ko **kuch attributes (properties)** aur **methods (functions)** milte hain, jo uske type par depend karte hain.  

---

## 📌 **Example: Number bhi ek Object Hai!**  
```python
num = 10  # Yeh actually ek 'int' class ka object hai
print(type(num))  # Output: <class 'int'>
```
Yeh proof kar raha hai ki `num` ek `int` class ka object hai.  

---

## 📌 **Example: String bhi ek Object Hai!**  
```python
name = "Aman"  # Yeh actually ek 'str' class ka object hai
print(type(name))  # Output: <class 'str'>

# String ke methods bhi hote hain jo uske sath aate hain
print(name.upper())  # Output: AMAN (Yeh 'upper()' method hai)
```

---

## 📌 **Example: List bhi ek Object Hai!**  
```python
my_list = [1, 2, 3]  # Yeh 'list' class ka object hai
print(type(my_list))  # Output: <class 'list'>

# List ke methods bhi hote hain
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

---

## 🔑 **Har Object ke 3 Important Parts:**  

1. **Type:**  
   - Har object ka ek type hota hai jo batata hai ki object kis class ka hai.  
   - Yeh `type()` function se pata chalta hai.  
   - Example:  
     ```python
     print(type(10))       # Output: <class 'int'>
     print(type("Hello"))   # Output: <class 'str'>
     print(type([1, 2, 3])) # Output: <class 'list'>
     ```

2. **Identity:**  
   - Yeh ek **unique memory address** hota hai jo Python me har object ke liye unique hota hai.  
   - Yeh `id()` function se pata chalta hai.  
   - Example:  
     ```python
     x = 10
     y = 10
     print(id(x))  # Same address for x and y because integers are immutable
     print(id(y))
     ```

3. **Value:**  
   - Object ke andar jo actual data hota hai, wo uski value hoti hai.  
   - Example:  
     ```python
     num = 42
     print(num)  # Output: 42 (Yeh value hai)
     ```

---

## 📌 **Custom Objects Example (Class Banakar)**  
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object banana (Instance of Class)
student1 = Student("Aman", 20)

print(type(student1))  # Output: <class '__main__.Student'>
print(student1.name)    # Output: Aman
print(student1.age)     # Output: 20
```

---

## 💡 **Python me Sab Kuch Object Hai Ka Matlab Kya Hai?**  
1. **Har Cheez ek Class se Bani Hai:**  
   - `int`, `str`, `list`, `dict`, `tuple`, sab apne-apne classes hai.  
   - Agar hum `type()` function use karte hain, toh hamesha output me `class` hi dikhega.  

2. **Memory Management:**  
   - Python har object ko **memory address (identity)** ke sath store karta hai.  
   - Immutable objects (`int`, `str`, `tuple`, etc.) ko agar modify karne ki koshish karte hain, toh naya object create hota hai.

3. **Everything is an Object:**  
   - Functions bhi objects hain!  
   - Modules bhi objects hain!  
   - Even, classes khud bhi objects hain! 😄  

---

### 🔍 **Proof: Function bhi Object hai!**  
```python
def greet():
    print("Hello!")

print(type(greet))  # Output: <class 'function'>
```

---

### 🔍 **Proof: Class bhi Object hai!**  
```python
class MyClass:
    pass

print(type(MyClass))  # Output: <class 'type'>
```

---

## 📖 **Summary:**  
- Python me sab kuch objects hai - numbers, strings, lists, dictionaries, functions, classes, etc.  
- Har object ka **type, identity, aur value hota hai.**  
- Python objects ko memory me manage karta hai, aur har object ko ek unique `id()` provide karta hai.  
- Immutable objects modify karne par naya object create karte hain.  

---
