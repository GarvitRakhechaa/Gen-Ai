# 📚 **Python Data Types (With Examples)**  

---



## 📌 **1. Numeric Data Types (Numbers)**  
Python me **Numeric Data Types** wo data types hain jo numbers ko represent karte hain. Yeh data types generally **mathematical operations** me use hote hain.  

### 🔑 **Types of Numeric Data Types:**  
1. **`int` (Integer)**  
2. **`float` (Floating Point)**  
3. **`complex` (Complex Numbers)**  
4. **`Decimal` (Exact Decimal Numbers)** - [Non-Standard]  
5. **`Fraction` (Rational Numbers)** - [Non-Standard]  
6. **Number Systems (`int` ke andar alag formats)** - Binary, Octal, Hexadecimal  

---

### 📖 **(a) `int` (Integer)**  
**Description:**  
- Integer wo numbers hain jo **poore numbers hote hain, bina kisi decimal ke**.  
- Yeh positive, negative, ya zero ho sakte hain.  
- Python me integers ki size limit nahi hoti.  

**Examples:**  
```python
# Integer Numbers
x = 10
y = -20
z = 0

print(x)        # Output: 10
print(y)        # Output: -20
print(z)        # Output: 0

# Checking Type
print(type(x))  # Output: <class 'int'>
```

---

### 📖 **(b) `float` (Floating Point)**  
**Description:**  
- Float numbers wo hote hain jo **decimal numbers ko represent karte hain.**  
- Example: 3.14, -0.5, 100.0.  
- Python me float numbers **double-precision (64-bit)** format me store hote hain.  

**Examples:**  
```python
# Floating Point Numbers
a = 10.5
b = -20.75
c = 0.0

print(a)        # Output: 10.5
print(b)        # Output: -20.75
print(c)        # Output: 0.0

# Checking Type
print(type(a))  # Output: <class 'float'>
```

---

### 📖 **(c) `complex` (Complex Numbers)**  
**Description:**  
- Complex numbers wo hote hain jo **real part aur imaginary part ko combine karte hain.**  
- Format: `a + bj` (Yahaan `a` real part hai aur `b` imaginary part hai).  
- `j` imaginary unit ko represent karta hai (Mathematics me `i` hota hai, par Python me `j` use hota hai).  

**Examples:**  
```python
# Complex Numbers
z = 2 + 3j

print(z)         # Output: (2+3j)
print(z.real)    # Output: 2.0 (Real part)
print(z.imag)    # Output: 3.0 (Imaginary part)

# Checking Type
print(type(z))   # Output: <class 'complex'>
```

---

### 📖 **(d) `Decimal` (Exact Decimal Numbers)** - [Non-Standard]  
**Description:**  
- Yeh `decimal.Decimal` class se milta hai (`decimal` module me available hai).  
- Accurate decimal arithmetic karne ke liye use hota hai.  
- Jab floating-point numbers ke accuracy issue se bachna ho, tab use karte hain.  

**Examples:**  
```python
from decimal import Decimal

x = Decimal('0.1')
y = Decimal('0.2')
result = x + y

print(result)           # Output: 0.3 (Accurate calculation)
print(type(result))      # Output: <class 'decimal.Decimal'>
```

---

### 📖 **(e) `Fraction` (Rational Numbers)** - [Non-Standard]  
**Description:**  
- Yeh `fractions.Fraction` class se milta hai (`fractions` module me available hai).  
- Rational numbers ko `numerator/denominator` ke form me store karte hain.  

**Examples:**  
```python
from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(2, 3)
result = x + y

print(result)        # Output: 1 (1/3 + 2/3 = 1)
print(type(result))   # Output: <class 'fractions.Fraction'>
```

---

### 📖 **(f) Number Systems (`int` ke andar alag formats)**  
Python me integers **different number systems** me bhi represent ho sakte hain.  

| Number System | Prefix | Example    | Decimal Value |
|---------------|--------|------------|---------------|
| Decimal       | None    | `10`       | 10            |
| Binary        | `0b`    | `0b1010`   | 10            |
| Octal         | `0o`    | `0o12`     | 10            |
| Hexadecimal   | `0x`    | `0xA`      | 10            |

---

### 🔍 **Examples of Number Systems:**  
```python
# Binary
bin_num = 0b1010
print(bin_num)    # Output: 10

# Octal
oct_num = 0o12
print(oct_num)    # Output: 10

# Hexadecimal
hex_num = 0xA
print(hex_num)    # Output: 10
```

---

### ✅ **Conversion Functions:**  
Python me conversion functions hote hain jo number systems me convert karne me madad karte hain.  

```python
num = 10

print(bin(num))  # Output: '0b1010' (Decimal to Binary)
print(oct(num))  # Output: '0o12' (Decimal to Octal)
print(hex(num))  # Output: '0xa' (Decimal to Hexadecimal)
```

---

### 💡 **Important Points:**  
1. **`int`, `float`, `complex` are built-in data types and are immutable.**  
2. `Decimal` & `Fraction` are also **immutable**, but they come from Python's standard library.  
3. **Number Systems (Binary, Octal, Hexadecimal)** are special forms of the `int` type.  
4. Arithmetic operations work on all numeric data types.  

---

Yeh tha **`Numeric Data Types (Numbers)` ka detailed explanation with examples.**  



---



## 📌 **2. Text Data Type (Strings)**  
Python me **String (`str`)** ek data type hai jo **textual data ko represent karne ke liye use hota hai**. String basically characters ka ek sequence hota hai, jisme **alphabets, numbers, symbols, spaces, etc. sabhi ho sakte hain**.  

---

### 🔑 **Creating a String:**  
Python me **String ko create karne ke liye single, double, ya triple quotes use karte hain.**  

```python
# Single Quotes
str1 = 'Hello, Python!'

# Double Quotes
str2 = "Hello, Python!"

# Triple Quotes (Multiline String)
str3 = '''Hello,
Python!
How are you?'''

print(str1)  # Output: Hello, Python!
print(str2)  # Output: Hello, Python!
print(str3)  # Output: Hello, \nPython!\nHow are you?
```

---

### 🔑 **String Characteristics:**  
1. **Immutable:** Python me strings **immutable hote hain**, yani once create hone ke baad unko modify nahi kar sakte.  
2. **Indexed:** String me **indexing hoti hai**, yani har character ka ek position number hota hai.  
3. **Slicing Supported:** String me se ek portion ko **slice karne ke liye** indexing ka use karte hain.  

---

### 📖 **Accessing Characters in a String (Indexing):**  
Python me string me har character ka **index hota hai:**  
- **Positive Indexing:** Left to Right (0 se start hota hai)  
- **Negative Indexing:** Right to Left (-1 se start hota hai)  

```python
text = "Python"

# Positive Indexing
print(text[0])  # Output: P
print(text[1])  # Output: y

# Negative Indexing
print(text[-1]) # Output: n
print(text[-2]) # Output: o
```

---

### 📖 **Slicing Strings:**  
String me **slice karne ke liye format hota hai: `string[start:end:step]`**  
- `start`: Kis index se shuru karna hai (inclusive).  
- `end`: Kis index par rukna hai (exclusive).  
- `step`: Kitne steps ka gap rakhna hai.  

```python
text = "Python Programming"

# Basic Slicing
print(text[0:6])       # Output: Python
print(text[7:18])      # Output: Programming

# Using Step
print(text[0:18:2])    # Output: Pto rgamn

# Negative Indexing
print(text[-11:])      # Output: Programming
```

---

### 📖 **String Concatenation and Repetition:**  
Python me strings ko **concatenate (`+`) aur repeat (`*`) kar sakte hain.**  

```python
str1 = "Hello"
str2 = "World"

# Concatenation
result = str1 + " " + str2
print(result)  # Output: Hello World

# Repetition
repeat = str1 * 3
print(repeat)  # Output: HelloHelloHello
```

---

### 📖 **String Functions & Methods:**  
Python me strings par kai **built-in functions aur methods** hote hain:  

| Method         | Description                                | Example                              |
|----------------|--------------------------------------------|-------------------------------------|
| `len()`        | String ki length return karta hai.         | `len("Python") -> 6`                |
| `upper()`      | Saare characters ko uppercase me badalna.  | `"python".upper() -> "PYTHON"`      |
| `lower()`      | Saare characters ko lowercase me badalna.  | `"PYTHON".lower() -> "python"`      |
| `strip()`      | Extra spaces ko remove karna.              | `"  hello  ".strip() -> "hello"`    |
| `replace()`    | Substring ko replace karna.                | `"hello".replace('h', 'H') -> "Hello"` |
| `split()`      | String ko parts me todna.                  | `"a,b,c".split(",") -> ['a', 'b', 'c']` |
| `join()`       | List ke elements ko string me join karna.  | `",".join(['a', 'b', 'c']) -> "a,b,c"` |
| `find()`       | Substring ki position find karna.          | `"Python".find("th") -> 2`          |
| `count()`      | Substring kitni baar aayi, ye batata hai.  | `"banana".count('a') -> 3`          |

---

### 📖 **String Formatting:**  
Python me strings ko format karne ke kai tareeke hain:  

#### ✅ **1. `f-strings` (Recommended)**  
```python
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: My name is John and I am 25 years old.
```

#### ✅ **2. `.format()` Method**  
```python
print("My name is {} and I am {} years old.".format(name, age))
```

#### ✅ **3. `%` Formatting (Old Method)**  
```python
print("My name is %s and I am %d years old." % (name, age))
```

---

### 📖 **String Immutability (Important):**  
Strings are **Immutable**, iska matlab aap existing string ko modify nahi kar sakte.  
Agar aap koi operation karte hain, to **naya string create hota hai, original string same rehti hai**.  

```python
text = "Python"
new_text = text.replace("P", "J")

print(text)       # Output: Python (Original remains unchanged)
print(new_text)   # Output: Jython (New string created)
```

---

### 💡 **Important Points:**  
1. Strings ko create karne ke liye `''`, `""`, `''' '''` use karte hain.  
2. String **Immutable hote hain.**  
3. String me **Indexing aur Slicing** supported hai.  
4. String methods me se kuchh strings ko modify karte hain par naya string return karte hain.  
5. `f-strings` sabse powerful aur modern way hai strings ko format karne ka.  

---

Yeh tha **`Text Data Type (Strings)` ka detailed explanation with examples.**  
Agar aap chaho toh me ise properly **notes ke format me likh kar de deta hoon**. 😊  
Kya ab me agle point par badhu? 😊

---


## 📌 **3. Sequence Data Types (List, Tuple, Range)**  
Python me **Sequence Data Types** wo data types hain jo **ordered collection of items ko represent karte hain.** Yeh collections **indexing, slicing, aur iteration** ko support karte hain.  

### 🔑 **Types of Sequence Data Types:**  
1. **List (`list`)** - Mutable  
2. **Tuple (`tuple`)** - Immutable  
3. **Range (`range`)** - Immutable (Specially for generating sequences of numbers)  

---

## 📖 **(a) List (`list`)**  
### 📋 **Description:**  
- Python me **List ek ordered collection hota hai** jo **different data types ko store kar sakta hai**.  
- Lists **mutable hoti hain**, yani unka content change ho sakta hai (add, remove, modify).  
- Lists ko **`[]` square brackets** me define karte hain.  

---

### 🔍 **Creating a List:**  
```python
# Different types of lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14, True]
nested = [[1, 2], [3, 4]]

print(numbers)  # Output: [1, 2, 3, 4, 5]
print(mixed)    # Output: [1, 'Hello', 3.14, True]
print(nested)   # Output: [[1, 2], [3, 4]]
```

---

### 🔍 **Accessing Elements (Indexing & Slicing):**  
```python
fruits = ["Apple", "Banana", "Cherry", "Mango"]

# Indexing
print(fruits[0])     # Output: Apple
print(fruits[-1])    # Output: Mango (Negative Indexing)

# Slicing
print(fruits[1:3])   # Output: ['Banana', 'Cherry']
print(fruits[:2])    # Output: ['Apple', 'Banana']
```

---

### 🔍 **Modifying a List (Mutable):**  
```python
fruits = ["Apple", "Banana", "Cherry"]

# Modifying an element
fruits[1] = "Orange"
print(fruits)  # Output: ['Apple', 'Orange', 'Cherry']

# Adding elements
fruits.append("Mango")
print(fruits)  # Output: ['Apple', 'Orange', 'Cherry', 'Mango']

# Removing elements
fruits.remove("Apple")
print(fruits)  # Output: ['Orange', 'Cherry', 'Mango']
```

---

### 🔍 **List Functions & Methods:**  
| Function/Method | Description                                   | Example                                           |
|-----------------|----------------------------------------------|---------------------------------------------------|
| `len()`         | List ki length return karta hai.             | `len(fruits)` -> 3                                 |
| `append()`      | List ke end me element add karta hai.        | `fruits.append("Grapes")` -> `['Orange', 'Cherry', 'Mango', 'Grapes']` |
| `remove()`      | Specified element ko delete kar deta hai.    | `fruits.remove("Mango")` -> `['Orange', 'Cherry']` |
| `pop()`         | Element ko index se delete kar deta hai.     | `fruits.pop(1)` -> `'Cherry'` (remove by index)    |
| `sort()`        | List ko ascending order me sort kar deta hai. | `numbers.sort()` -> `[1, 2, 3, 4, 5]`             |
| `reverse()`     | List ko reverse kar deta hai.                | `numbers.reverse()` -> `[5, 4, 3, 2, 1]`         |

---

## 📖 **(b) Tuple (`tuple`)**  
### 📋 **Description:**  
- Python me **Tuple bhi ek ordered collection hota hai**, lekin yeh **immutable hota hai**.  
- Tuples ko **`()` parenthesis** me define karte hain.  
- Read-only data ko store karne ke liye use hota hai.  

---

### 🔍 **Creating a Tuple:**  
```python
# Different types of tuples
numbers = (1, 2, 3)
mixed = (1, "Hello", 3.14)
single_element = (5,)  # Important! Single element tuple ke liye comma zaruri hai.

print(numbers)          # Output: (1, 2, 3)
print(mixed)            # Output: (1, 'Hello', 3.14)
print(single_element)    # Output: (5,)
```

---

### 🔍 **Accessing Elements (Indexing & Slicing):**  
```python
colors = ("Red", "Green", "Blue")

# Indexing
print(colors[0])   # Output: Red
print(colors[-1])  # Output: Blue

# Slicing
print(colors[0:2])  # Output: ('Red', 'Green')
```

---

### 🔍 **Tuple Methods:**  
| Method      | Description                                  |
|-------------|---------------------------------------------|
| `count()`   | Tuple me kitni baar specified value hai.    |
| `index()`   | Specified value ka index return karta hai.  |

---

## 📖 **(c) Range (`range`)**  
### 📋 **Description:**  
- Python me **Range ek immutable sequence hai** jo **sequence of numbers generate karne ke liye use hota hai.**  
- Commonly **loops me use hota hai**.  
- Format: `range(start, stop, step)`  

---

### 🔍 **Creating & Using a Range:**  
```python
# Basic range
numbers = range(5)
print(list(numbers))  # Output: [0, 1, 2, 3, 4]

# Range with start & stop
numbers = range(1, 6)
print(list(numbers))  # Output: [1, 2, 3, 4, 5]

# Range with step
numbers = range(0, 10, 2)
print(list(numbers))  # Output: [0, 2, 4, 6, 8]
```

---

### 💡 **Important Points:**  
1. **List (`list`)**: Mutable, Ordered, Indexed, Slicing allowed.  
2. **Tuple (`tuple`)**: Immutable, Ordered, Indexed, Slicing allowed.  
3. **Range (`range`)**: Immutable, Ordered, Generated lazily.  
4. Tuples ko **protect karne ke liye use karte hain, jab data ko change karna allowed na ho.**  
5. Lists me **elements add, remove, aur modify kiye ja sakte hain.**  

---

## 📌 **4. Mapping Data Type (Dictionary)**
Python me **Dictionary (`dict`)** ek aisa data type hai jo **key-value pairs me data store karne ke liye use hota hai.**  
Yeh **unordered collection** hota hai jismein **keys unique hoti hain** aur har key ka ek **associated value** hota hai.  

---

### 🔑 **Creating a Dictionary:**  
Dictionaries ko **curly braces `{}`** ke saath define karte hain ya phir **`dict()` function ka use karte hain.  

```python
# Method 1: Using curly braces
student = {
    "name": "Aman",
    "age": 20,
    "subjects": ["Math", "Physics", "Chemistry"]
}

# Method 2: Using dict() function
employee = dict(name="Rahul", age=30, job="Engineer")

print(student)
print(employee)
```
---

### 🔍 **Accessing Values (Indexing)**  
Values ko access karne ke liye **square brackets `[]` me key ka naam dete hain.**  
Agar key exist nahi karti, to **`KeyError`** aata hai.  

```python
print(student["name"])        # Output: Aman
print(student["subjects"])     # Output: ['Math', 'Physics', 'Chemistry']
```

---

### 🔍 **Accessing Values Safely (Using `get()`)**  
Agar key exist nahi karti, to `get()` function `None` return kar deta hai instead of error.  

```python
print(student.get("age"))       # Output: 20
print(student.get("address"))    # Output: None
```

---

### 🔍 **Adding & Modifying Items (Mutable)**  
Dictionary mutable hoti hai, to hum **values ko change ya update kar sakte hain.**  

```python
# Adding a new key-value pair
student["address"] = "Delhi"

# Modifying an existing key's value
student["age"] = 21

print(student)
```

---

### 🔍 **Removing Items**  
Python me dictionaries se items ko delete karne ke kai tarike hain:  

```python
# 1. Using del keyword
del student["address"]

# 2. Using pop() method (Returns the value of the removed key)
age = student.pop("age")
print(age)         # Output: 21

# 3. Using popitem() method (Removes the last inserted item)
last_item = student.popitem()
print(last_item)    # Output: ('subjects', ['Math', 'Physics', 'Chemistry'])
```

---

### 🔍 **Dictionary Methods**  
| Method        | Description                                              | Example                                    |
|---------------|----------------------------------------------------------|------------------------------------------|
| `get()`       | Key exist karne par uski value return karta hai, otherwise `None`. | `student.get("name")` -> `Aman` |
| `keys()`      | Saari keys ko `dict_keys` object me return karta hai.    | `student.keys()` -> `dict_keys(['name'])` |
| `values()`    | Saari values ko `dict_values` object me return karta hai. | `student.values()` -> `dict_values(['Aman'])` |
| `items()`     | Key-value pairs ko `dict_items` object me return karta hai. | `student.items()` -> `dict_items([('name', 'Aman')])` |
| `update()`    | Ek dictionary ko dusre dictionary se update karne ke liye. | `student.update({"age": 22})` |
| `clear()`     | Saari items ko delete kar deta hai.                       | `student.clear()` -> `{}` |
| `copy()`      | Dictionary ka shallow copy banata hai.                   | `new_dict = student.copy()` |

---

### 💡 **Dictionary Comprehension (Shorter way to create dictionaries)**  
```python
# Example: Creating a dictionary of squares of numbers from 1 to 5
squares = {x: x * x for x in range(1, 6)}
print(squares)    # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### 📖 **Important Points:**  
1. **Dictionaries are mutable:** Keys add, update, ya delete ho sakte hain.  
2. **Keys are unique:** Agar same key do baar add karenge, to pehle wali value overwrite ho jayegi.  
3. **Keys must be immutable:** Lists, sets, ya koi bhi mutable object ko key ke roop me use nahi kar sakte.  
4. **Values can be of any data type:** Including lists, dictionaries, tuples, etc.  

---


## 📌 **5. Set Data Types (Set and FrozenSet)**
Python me **Set** ek aisa data type hai jo **unordered, mutable, aur unique elements ko store karne ke liye use hota hai.**  
Sets ka main purpose **duplicate elements ko avoid karna** hai.  

---

### 🔑 **Creating a Set:**  
Sets ko **curly braces `{}`** ya phir **`set()` function se create karte hain.**  

```python
# Method 1: Using curly braces
my_set = {1, 2, 3, 4, 5}

# Method 2: Using set() function
another_set = set([3, 4, 5, 6, 7])

# Empty set (Only using set() function)
empty_set = set()

print(my_set)        # Output: {1, 2, 3, 4, 5}
print(another_set)    # Output: {3, 4, 5, 6, 7}
print(empty_set)      # Output: set()
```

---

### 🔍 **Characteristics of Sets:**  
1. **Unordered:** Elements ka order fix nahi hota, yani indexing ya slicing nahi ho sakti.  
2. **Unique Elements:** Sets me duplicate elements automatically remove ho jate hain.  
3. **Mutable:** Hum sets me naya element add ya remove kar sakte hain.  

---

### 🔍 **Accessing Set Elements (No Indexing)**  
Sets me **indexing support nahi hota**. Agar elements ko access karna ho, to hume **loop ya specific methods** ka use karna padta hai.  

```python
for item in my_set:
    print(item)
```

---

### 🔍 **Adding & Removing Elements (Mutable)**  
```python
# Adding single element
my_set.add(6)
print(my_set)    # Output: {1, 2, 3, 4, 5, 6}

# Adding multiple elements
my_set.update([7, 8, 9])
print(my_set)    # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing an element (Raises error if not found)
my_set.remove(9)   # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Removing an element safely (Does not raise error)
my_set.discard(10)  # No error even if 10 is not in the set

# Removing a random element
removed_item = my_set.pop()
print(removed_item)    # Randomly removed element
```

---

### 🔍 **Set Operations (Union, Intersection, Difference, Symmetric Difference)**  
Sets me **mathematical operations** ko perform karne ke liye methods ya operators use karte hain.  

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (All unique elements from both sets)
print(set_a | set_b)               # Output: {1, 2, 3, 4, 5, 6}
print(set_a.union(set_b))          

# Intersection (Common elements from both sets)
print(set_a & set_b)               # Output: {3, 4}
print(set_a.intersection(set_b))    

# Difference (Elements in set_a but not in set_b)
print(set_a - set_b)               # Output: {1, 2}
print(set_a.difference(set_b))      

# Symmetric Difference (Elements not common in both sets)
print(set_a ^ set_b)               # Output: {1, 2, 5, 6}
print(set_a.symmetric_difference(set_b))
```

---

### 🔍 **Set Methods:**  
| Method               | Description                                 |
|----------------------|---------------------------------------------|
| `add()`              | Adds a single element to the set.           |
| `update()`           | Adds multiple elements to the set.          |
| `remove()`           | Removes an element, raises error if not found. |
| `discard()`          | Removes an element safely without error.    |
| `pop()`              | Removes and returns a random element.       |
| `clear()`            | Removes all elements from the set.          |
| `copy()`             | Returns a shallow copy of the set.          |

---

## 📌 **FrozenSet (Immutable Set)**
Agar hume **immutable set chahiye jo modify na ho sake**, to hum **`frozenset()` function** use karte hain.  
Ye **read-only set** hota hai.  

```python
# Creating a frozenset
immutable_set = frozenset([1, 2, 3, 4])

# Trying to modify (Will raise an error)
immutable_set.add(5)    # AttributeError: 'frozenset' object has no attribute 'add'
```

---

### 📖 **Important Points:**  
1. **Sets are mutable:** `add()`, `remove()`, `update()`, etc. use ho sakte hain.  
2. **FrozenSets are immutable:** Once created, modify nahi ho sakte.  
3. **Use Cases:**  
   - Sets ko mostly **duplicate removal** ya **mathematical operations (union, intersection, etc.)** me use karte hain.  
   - FrozenSets ko mostly **hashable objects** ki tarah use karte hain, jaise ke dictionary keys me.  

---



## 📌 **6. Boolean Data Type (bool)**
Python me **Boolean Data Type (`bool`)** sirf **do values store kar sakta hai:**  
- `True`  (Sach / Yes)  
- `False` (Jhoot / No)  

Yeh mainly **conditions ko check karne aur logical operations me use hota hai.**  

---

### 🔑 **Creating Boolean Values:**  
Boolean values ko **directly likh sakte hain (`True` ya `False`)** ya phir **comparison operators** ke result se milte hain.  

```python
# Direct boolean values
is_raining = True
is_sunny = False

print(is_raining)   # Output: True
print(is_sunny)     # Output: False
```

---

### 🔍 **Comparison Operators (Result: Boolean Value)**  
Comparison karne par `True` ya `False` return hota hai.  

| Operator | Description           | Example        | Result  |
|----------|-----------------------|----------------|---------|
| `==`     | Equal to               | `5 == 5`       | `True`  |
| `!=`     | Not equal to           | `5 != 3`       | `True`  |
| `>`      | Greater than           | `7 > 2`        | `True`  |
| `<`      | Less than              | `2 < 1`        | `False` |
| `>=`     | Greater than or equal  | `4 >= 4`       | `True`  |
| `<=`     | Less than or equal     | `3 <= 2`       | `False` |

---

### 🔍 **Logical Operators (AND, OR, NOT)**  
Ye operators **multiple conditions ko combine karne ke liye use hote hain.**  

| Operator  | Description                | Example               | Result  |
|-----------|---------------------------|-----------------------|---------|
| `and`     | True agar dono conditions true hain. | `True and False`   | `False` |
| `or`      | True agar koi ek condition true ho.   | `True or False`    | `True`  |
| `not`     | True ko False me aur False ko True me convert kar deta hai. | `not True` | `False` |

---

### 🔍 **Examples (Logical Operations):**  
```python
a = 10
b = 20

# AND operation (Both conditions must be True)
result = (a > 5) and (b > 15)
print(result)  # Output: True

# OR operation (At least one condition must be True)
result = (a > 15) or (b > 15)
print(result)  # Output: True

# NOT operation (Inverts the condition)
result = not (a > 5)
print(result)  # Output: False
```

---

### 🔍 **Boolean Conversion (Typecasting):**  
Koi bhi data type ko **`bool()` function se boolean me convert kar sakte hain.**  

```python
# Non-zero numbers, non-empty strings/lists/dicts are True
print(bool(1))            # Output: True
print(bool("Hello"))       # Output: True
print(bool([1, 2, 3]))     # Output: True

# Zero, empty strings/lists/dicts are False
print(bool(0))             # Output: False
print(bool(""))            # Output: False
print(bool([]))            # Output: False
```

---

### 🔍 **Boolean as Numbers (0 and 1)**  
Python me `True` ka value **`1`** aur `False` ka value **`0`** ke barabar hota hai.  

```python
# Performing arithmetic operations
result = True + True
print(result)     # Output: 2 (1 + 1)

result = True * False
print(result)     # Output: 0 (1 * 0)
```

---

### 📖 **Important Points:**  
1. **Booleans are Subclass of Integers:** `True` = `1` and `False` = `0`.  
2. **Used in Conditions:** If statements, loops, logical operations, etc.  
3. **Type Conversion:** Kisi bhi data type ko `bool()` function se boolean me convert kar sakte hain.  

---


## 📌 **7. None Data Type (`NoneType`)**
Python me **`None`** ek special data type hai jo **"kuch bhi nahi" ya "null value"** ko represent karne ke liye use hota hai.  
Ye **JavaScript me `null` ya Java me `null` ke barabar hai.**  
Iska data type hota hai: **`NoneType`**.  

---

### 🔍 **Creating a None Value:**  
`None` ko **directly likha jata hai (`None`)**.  

```python
# Assigning None to a variable
x = None
print(x)           # Output: None
print(type(x))      # Output: <class 'NoneType'>
```

---

### 🔍 **Use Cases of `None`:**  
1. **Default Value:**  
   - Jab kisi function me value return nahi karni ho.  
   - Example: Agar function sirf print kar raha hai to return value `None` hoti hai.  

```python
def greet():
    print("Hello, World!")

result = greet()      # Function call
print(result)         # Output: None
```

---

2. **Placeholder Value:**  
   - Jab hum variable ko declare karna chahte hain lekin usme abhi koi value nahi dena chahte.  

```python
# Declaring a variable without assigning any value
user_data = None

if user_data is None:
    print("User data is not yet available.")   # Output: User data is not yet available.
```

---

3. **Indicating Absence of Value (Database, API, etc.):**  
   - Jab kisi operation ka result exist nahi karta ya **missing data ko represent karna ho.**  

---

### 🔍 **Checking for `None`: (`is` keyword)**  
Comparison karte waqt **`==` use karne ke bajaye `is` keyword use karna chahiye.**  

```python
x = None

if x is None:
    print("Yes, x is None.")   # Output: Yes, x is None.
```

> 💡 **Why `is` instead of `==`?**  
> - `is` check karta hai **identity (same object in memory)** ko.  
> - `==` check karta hai **value equality** ko.  

---

### 🔍 **Functions Returning `None`:**  
Kuch functions jo kuch return nahi karte, wo actually **`None` return karte hain.**  

```python
def say_hello():
    print("Hello!")

result = say_hello()   # Output: Hello!
print(result)          # Output: None
```

---

### 🔍 **Using `None` with Conditional Statements:**  
`None` ko conditional statements me bhi use kar sakte hain.  

```python
x = None

if x:
    print("x has a value.")
else:
    print("x is None or False.")   # Output: x is None or False.
```

---

### 📖 **Important Points:**  
1. **`None` ek singleton object hai:** Matlab Python me sirf ek hi `None` object hota hai.  
2. **`None` ka type hota hai:** `NoneType`.  
3. **Use `is` for Comparison:** `None` ko check karne ke liye `is` keyword use karna chahiye.  
4. **Mostly used for:** Default values, missing data, uninitialized variables, etc.  

---
Ohh, samajh gaya! Ab me aapko properly explain karunga **Binary Data Types (Bytes)** ko with examples. 😊  

---

## 📌 **8. Binary Data Types (Bytes)**  
Python me **Binary Data Types** use hote hain **Binary data (0s and 1s)** ko handle karne ke liye. Ye mainly **files ko read/write karne, network communication ya low-level operations** me use hote hain.  
Binary Data Types:  
1. **`bytes` (Immutable)**  
2. **`bytearray` (Mutable)**  
3. **`memoryview` (Read-write buffer for binary data)**  

---

### 🔑 **1. `bytes` (Immutable)**  
- Ye **immutable sequence of bytes (0 to 255)** ko store karte hain.  
- Jab create kar liya to modify nahi kar sakte (Jaise strings).  

---

#### ✅ **Creating a `bytes` Object:**  
```python
# Creating bytes from a string (Encoding required)
text = "Hello"
byte_data = bytes(text, 'utf-8')
print(byte_data)           # Output: b'Hello'

# Creating bytes from a list of integers (0-255)
byte_data2 = bytes([72, 101, 108, 108, 111])
print(byte_data2)           # Output: b'Hello'
```

---

#### 🔍 **Accessing `bytes`:**  
```python
# Accessing individual bytes
print(byte_data[0])         # Output: 72 (ASCII value of 'H')

# Iterating over bytes
for b in byte_data:
    print(b, end=" ")        # Output: 72 101 108 108 111
```

---

#### ❌ **Modification Error (Immutable):**  
```python
# Trying to modify a bytes object (Error)
byte_data[0] = 77            # Output: TypeError: 'bytes' object does not support item assignment
```

---

### 🔑 **2. `bytearray` (Mutable)**  
- Ye bhi **sequence of bytes (0 to 255)** hai, lekin **mutable hai (Modify kar sakte hain)**.  
- Useful jab aapko binary data ko modify karna ho.  

---

#### ✅ **Creating a `bytearray` Object:**  
```python
# Creating a bytearray from a string
text = "Hello"
byte_array = bytearray(text, 'utf-8')
print(byte_array)            # Output: bytearray(b'Hello')

# Creating a bytearray from a list of integers
byte_array2 = bytearray([72, 101, 108, 108, 111])
print(byte_array2)           # Output: bytearray(b'Hello')
```

---

#### 🔍 **Modifying `bytearray`:**  
```python
# Changing the first byte to ASCII value of 'M'
byte_array[0] = 77
print(byte_array)            # Output: bytearray(b'Mello')
```

---

#### 🔍 **Adding Data (`append()`):**  
```python
# Adding an exclamation mark (ASCII value 33)
byte_array.append(33)
print(byte_array)            # Output: bytearray(b'Mello!')
```

---

### 🔑 **3. `memoryview` (Read-write Buffer for Binary Data)**  
- Ye **existing binary data ko bina copy kare uske upar read/write operations karne deta hai**.  
- Efficient memory management ke liye useful hota hai.  

---

#### ✅ **Creating a `memoryview` Object:**  
```python
# Creating a bytearray
byte_array = bytearray("Hello", 'utf-8')

# Creating memoryview from bytearray
mv = memoryview(byte_array)

# Accessing the first byte
print(mv[0])                  # Output: 72 (ASCII value of 'H')
```

---

#### 🔍 **Modifying Data via `memoryview`:**  
```python
# Modifying data
mv[0] = 77
print(byte_array)             # Output: bytearray(b'Mello')
```

---

### 📖 **Important Points:**  
1. **`bytes` (Immutable):** Cannot be modified once created.  
2. **`bytearray` (Mutable):** Can be modified, useful for editing binary data.  
3. **`memoryview`:** Provides a read-write view of binary data without copying.  
4. **Binary Data Representation:** Useful for file handling, networking, images, etc.  
5. **ASCII Values:** `A` = 65, `B` = 66, `a` = 97, `b` = 98, etc. (0 - 255 range).  

---
