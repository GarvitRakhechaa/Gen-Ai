# mutable and immutalble in python 

Theek hai! Pura jo ab tak padha hai, usko ek saath notes ke form me dekh le:  

---

## 📚 **Mutable and Immutable Objects in Python**  

### 🔍 **Mutable vs Immutable (Basic Definition)**  
- **Mutable Objects:** Jinka content change ho sakta hai bina naye object banaye.  
- **Immutable Objects:** Jinka content change nahi ho sakta, agar change karna hai toh naya object create hota hai.  

---

### ✅ **Mutable Objects (Jo Change Ho Sakte Hain)**  
1. **List (Sabse Common Example)**  
```python
my_list = [1, 2, 3]
my_list.append(4)  # Naya element add ho gaya
print(my_list)  # Output: [1, 2, 3, 4]
```

2. **Dictionary (Key-Value Pairs wala Object)**  
```python
my_dict = {"name": "Aman", "age": 20}
my_dict["age"] = 21  # Age update ho gayi
print(my_dict)  # Output: {'name': 'Aman', 'age': 21}
```

3. **Set (Unique Values ka Collection)**  
```python
my_set = {1, 2, 3}
my_set.add(4)  # Set me naya element add ho gaya
print(my_set)  # Output: {1, 2, 3, 4}
```

---

### ❌ **Immutable Objects (Jo Change Nahi Ho Sakte)**  
1. **String (Hamesha New String Banata Hai Modify Karne par)**  
```python
name = "Aman"
new_name = name.upper()  # Naya string banayega
print(name)      # Output: Aman
print(new_name)  # Output: AMAN
```

2. **Tuple (Immutable List Jaisa)**  
```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Ye error dega kyunki tuple ko modify nahi kar sakte
```

3. **frozenset (Immutable Set)**  
```python
my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # Ye error dega kyunki frozenset me add nahi kar sakte
```

---

### 📌 **Kaise Check Karein Ki Object Mutable Hai Ya Immutable?**  
**Example 1: Mutable Object (`list`)**  
```python
my_list = [1, 2, 3]
print(id(my_list))  # id() function se memory address check karte hain

my_list.append(4)
print(id(my_list))  # Same address hoga - MATLAB mutable hai
```

**Example 2: Immutable Object (`str`)**  
```python
my_str = "Aman"
print(id(my_str))

my_str = my_str + " Singh"
print(id(my_str))  # Address alag hoga - MATLAB immutable hai
```

---

### 🔑 **Why Does It Matter? (Yeh Kyon Important Hai?)**  
1. **Performance:** Immutable objects fast hote hain access karne me, aur memory efficient bhi.  
2. **Hashability:** Immutable objects ko `dict` ke keys ya `set` ke elements ke roop me use kar sakte hain (kyunki unka value kabhi change nahi hota).  
3. **Safety:** Immutable objects ko alag alag parts me safely share kar sakte hain bina kisi dikkat ke.  

---

### 💡 **Summary Table:**  

| Mutable (Change Ho Sakta Hai) | Immutable (Change Nahi Ho Sakta) |
|-----------------------------|----------------------------------|
| `list`                      | `tuple`                         |
| `dict`                      | `str`                           |
| `set`                       | `frozenset`                     |
| `bytearray`                 | `int`, `float`, `bool`          |

---

