## ✅ **Loops in Python**  
Python me **loops** ka use **repeated execution** ke liye hota hai.  
Agar ek kaam **multiple times execute** karna ho, to **loops** ka use karte hain.  

Python me **2 types ke loops** hote hain:  
1. **`for` loop** (Iterating over sequences like lists, tuples, strings, etc.)  
2. **`while` loop** (Condition-based looping)  

---

## 📌 **1. `for` Loop (Sequence Traversing)**
Jab kisi **sequence** (list, tuple, string, range, etc.) me iterate karna ho, tab `for` loop use hota hai.  

### 🔍 **Example:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
✅ Output:
```
apple
banana
cherry
```

---

## 📌 **2. `for` with `range()` (Looping N times)**
Agar **specific number of times** loop chalana ho to `range()` ka use hota hai.  

### 🔍 **Example:**
```python
for i in range(5):  
    print(i)  
```
✅ Output:
```
0
1
2
3
4
```
⚡ **`range(5)` → Default start `0`, end `4` (excludes 5).**  

---

## 📌 **3. `for` Loop with `range(start, end, step)`**
Agar custom **start, end, step-size** set karna ho to `range(start, end, step)` ka use hota hai.  

### 🔍 **Example:**
```python
for i in range(1, 10, 2):  
    print(i)
```
✅ Output:
```
1
3
5
7
9
```
⚡ **Yaha `1` se start hoke `9` tak gaya, step-size `2` hai.**  

---

## 📌 **4. `while` Loop (Condition-based Looping)**
Jab tak **condition `True`** hai, tab tak loop chalega.  

### 🔍 **Example:**
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
✅ Output:
```
1
2
3
4
5
```
⚡ **Jab `count` `6` hua, condition `False` ho gayi aur loop ruk gaya.**  

---

## 📌 **5. Infinite Loop (Avoid Carefully!)**
Agar **`while` condition kabhi `False` na ho**, to loop **infinite** chal sakta hai.  
❌ **Example (Beware! Will run forever):**
```python
while True:
    print("This is an infinite loop!")
```
👀 **Isko stop karne ke liye manually `Ctrl + C` daba ke break karna padega!**  

---

## 📌 **6. `break` Statement (Loop Ko Rokane Ke Liye)**
`break` ka use **loop ko forcefully stop** karne ke liye hota hai.  

### 🔍 **Example:**
```python
for num in range(1, 10):
    if num == 5:
        break  # Loop stops when num == 5
    print(num)
```
✅ Output:
```
1
2
3
4
```
⚡ **Jab `num == 5`, tab loop break ho gaya.**  

---

## 📌 **7. `continue` Statement (Skip Current Iteration)**
`continue` ka use **current iteration ko skip** karne ke liye hota hai.  

### 🔍 **Example:**
```python
for num in range(1, 6):
    if num == 3:
        continue  # Skip iteration when num == 3
    print(num)
```
✅ Output:
```
1
2
4
5
```
⚡ **Jab `num == 3`, to `continue` ne us iteration ko skip kar diya.**  

---

## 📌 **8. `else` with Loop (Loop Properly Finish Ho Gaya)**
Agar loop **normally execute hoke khatam ho jaye (without `break`)**, tab `else` block execute hota hai.  

### 🔍 **Example:**
```python
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")
```
✅ Output:
```
0
1
2
Loop finished successfully!
```

⚡ **Agar loop `break` se stop ho jaye, to `else` execute nahi hota.**  

### ❌ **Example with `break`:**
```python
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished successfully!")
```
✅ Output:
```
0
```
⚡ **Yaha loop `break` hone ki wajah se `else` execute nahi hua.**  

---

## 🔥 **Summary (Looping at a Glance)**
| **Loop Type**  | **Usage**  |
|---------------|------------|
| `for` loop  | **Iterate over a sequence** (list, tuple, string, range, etc.) |
| `while` loop  | **Run until a condition is False** |
| `break`  | **Loop ko forcefully stop karna** |
| `continue`  | **Current iteration ko skip karna** |
| `else` (with loops)  | **Loop agar normally finish ho jaye to execute hota hai** |

---

## ✅ **Best Practices**
✔ **Agar pata ho loop kitni baar chalega → `for` loop use karo.**  
✔ **Agar condition-based loop chahiye → `while` loop use karo.**  
✔ **Avoid infinite loops unless required (`while True`).**  
✔ **Use `break` and `continue` carefully.**  

---


Looping in Python works using iterators and the `__iter__` and `__next__` methods under the hood. Let’s break it down! 🚀  

---

## **1. How `for` Loop Works Internally**
A `for` loop in Python is just syntactic sugar for using an **iterator** explicitly.

Example:
```python
nums = [10, 20, 30]

for num in nums:
    print(num)
```
Behind the scenes, Python does this:

```python
nums = [10, 20, 30]

# Get an iterator
it = iter(nums)  # Equivalent to nums.__iter__()

while True:
    try:
        num = next(it)  # Equivalent to it.__next__()
        print(num)
    except StopIteration:
        break  # Stops when there are no more elements
```
✅ **Python converts a `for` loop into an iterator and uses `next()` to get each value until `StopIteration` is raised.**

---

## **2. How `while` Loop Works**
Unlike `for`, a `while` loop simply executes based on a condition:

```python
i = 0
while i < 3:
    print(i)
    i += 1
```
This keeps executing until `i < 3` is `False`.

---

## **3. Looping Over Custom Objects**
You can create your own iterable object by defining `__iter__` and `__next__`.

Example:
```python
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):  # Returns itself as an iterator
        return self

    def __next__(self):  # Defines how to get the next value
        if self.current >= self.end:
            raise StopIteration  # Ends the loop
        value = self.current
        self.current += 1
        return value

# Using the custom iterable
for num in Counter(1, 5):
    print(num)
```
**Output:**
```
1
2
3
4
```

---

## **4. Generator-Based Loops (Lazy Iteration)**
Generators allow creating iterators **without defining a class**.

Example:
```python
def counter(start, end):
    while start < end:
        yield start
        start += 1

for num in counter(1, 5):
    print(num)
```
🔹 **`yield` creates an iterator automatically** without `__iter__` and `__next__`.

---

## **Summary**
- `for` loops internally call `iter()` and `next()`.
- `while` loops just check conditions repeatedly.
- Custom iterators need `__iter__` and `__next__`.
- Generators (`yield`) simplify iterator creation.

Let me know if you want more details! 🚀