## 📌 **File System in Python (A to Z)**
Python me **File Handling** ka use **data read, write, update, aur delete** karne ke liye hota hai.  
Python ke `open()` function ka use karke **file handling operations** perform kar sakte hain.  

---

# 🔥 **1. File Handling Basics**
Python me **files** ko handle karne ke liye `open()` function use hota hai:  
```python
file = open("filename.txt", "mode")
```
📌 **Modes:**  
| Mode  | Description |
|--------|------------|
| `"r"`  | **Read Mode** (Default) |
| `"w"`  | **Write Mode** (Overwrite file) |
| `"a"`  | **Append Mode** (Add new content) |
| `"x"`  | **Create Mode** (Fails if file exists) |
| `"b"`  | **Binary Mode** (For binary files) |
| `"t"`  | **Text Mode** (Default mode) |

---

# 📌 **2. Opening & Closing a File**
### ✅ **File Open & Close Example**
```python
file = open("example.txt", "r")  # File open in read mode
print(file.read())  # Read content
file.close()  # Close the file
```
📌 **`close()` function compulsory hai, warna data loss ho sakta hai!**  
⚡ **Alternative (With `with` Statement - Auto Close)**  
```python
with open("example.txt", "r") as file:
    print(file.read())  # File will be auto-closed
```
✅ **No need to call `close()` manually.**

---

# 📌 **3. Reading Files (`r` mode)**
### ✅ **Complete File Read (`read()`)**
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### ✅ **Read First 10 Characters (`read(n)`)**
```python
with open("example.txt", "r") as file:
    print(file.read(10))  # Reads only first 10 characters
```

### ✅ **Read Line-by-Line (`readline()`)**
```python
with open("example.txt", "r") as file:
    print(file.readline())  # Reads first line only
```

### ✅ **Read All Lines as List (`readlines()`)**
```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Returns a list of lines
```

---

# 📌 **4. Writing to a File (`w` mode)**
Agar **file exist karti hai** to **purana data delete ho jayega** aur naya likha jayega.

### ✅ **Write to a File (`write()`)**
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")  # Overwrites the file
```

### ✅ **Write Multiple Lines (`writelines()`)**
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)
```

---

# 📌 **5. Appending to a File (`a` mode)**
Agar **file exist karti hai**, to naya content **add hoga (purana delete nahi hoga).**

### ✅ **Append New Content**
```python
with open("example.txt", "a") as file:
    file.write("New content added!\n")
```

---

# 📌 **6. Creating a File (`x` mode)**
Agar **file exist karti hai**, to **error milega**.

### ✅ **Create New File**
```python
with open("newfile.txt", "x") as file:
    file.write("This is a new file!")
```

---

# 📌 **7. Working with Binary Files (`b` mode)**
Binary mode **images, videos, PDFs, etc.** ke liye use hota hai.

### ✅ **Read Binary File (`rb` mode)**
```python
with open("image.jpg", "rb") as file:
    content = file.read()
```

### ✅ **Write Binary File (`wb` mode)**
```python
with open("copy.jpg", "wb") as file:
    file.write(content)
```

---

# 📌 **8. Checking if File Exists (`os` module)**
```python
import os
if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File not found!")
```

---

# 📌 **9. Renaming & Deleting Files**
### ✅ **Rename File**
```python
import os
os.rename("oldname.txt", "newname.txt")
```

### ✅ **Delete File**
```python
import os
os.remove("example.txt")
```

---

# 📌 **10. Working with Directories (`os` module)**
### ✅ **Check if Directory Exists**
```python
import os
if os.path.isdir("myfolder"):
    print("Directory exists!")
```

### ✅ **Create a New Directory**
```python
import os
os.mkdir("new_folder")
```

### ✅ **Remove a Directory**
```python
import os
os.rmdir("new_folder")
```

### ✅ **List All Files in a Directory**
```python
import os
files = os.listdir(".")  # List all files in current directory
print(files)
```

---

# 📌 **11. File Pointer Position (`tell()` & `seek()`)**
### ✅ **Get Current Position in File**
```python
with open("example.txt", "r") as file:
    print(file.tell())  # Shows current cursor position
```

### ✅ **Move to Specific Position (`seek()`)**
```python
with open("example.txt", "r") as file:
    file.seek(5)  # Move cursor to 5th character
    print(file.read())  # Read from new position
```

---

# 📌 **12. File Exception Handling (`try-except`)**
Agar **file exist nahi karti** ya koi **error hota hai**, to program crash na ho, iske liye `try-except` ka use karte hain.

### ✅ **Handle File Not Found Error**
```python
try:
    with open("missingfile.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

---

# 📌 **🔥 Summary (File Handling at a Glance)**
| **Operation**  | **Mode**  | **Description**  |
|--------------|--------|----------------|
| Read file  | `"r"` | File exist hona chahiye |
| Write file  | `"w"` | Purana data delete hoga |
| Append file  | `"a"` | Purana data safe rahega |
| Create new file  | `"x"` | Agar file exist ho to error |
| Read binary file  | `"rb"` | Binary mode |
| Write binary file  | `"wb"` | Binary mode |
| Check file exist  | `os.path.exists()` | Returns `True` / `False` |
| Delete file  | `os.remove()` | Delete the file |
| Rename file  | `os.rename()` | Rename the file |

---

## 📌 **Time Module in Python (A to Z)**  
Python ka `time` module **date & time manipulation** ke liye use hota hai.  
Isme **timestamps, delays, time calculations, etc.** karne ke liye functions hote hain.

---

# 🔥 **1. Importing Time Module**
```python
import time
```

---

# 📌 **2. Getting Current Time (`time.time()`)**
Ye function **current time (seconds since 1st Jan 1970, UTC)** return karta hai (Epoch Time).
```python
import time
print(time.time())  # Output: 1711343045.123 (Example)
```
✅ **Epoch Time:** 1 Jan 1970 ko **0 seconds** maana jata hai. 

---

# 📌 **3. Converting Seconds to Readable Format (`time.ctime()`)**
```python
import time
print(time.ctime())  # Current time in human-readable format
```
✅ **Output Example:**  
```
Mon Mar 25 12:34:56 2025
```
Agar kisi particular **timestamp** ka readable time chahiye:
```python
print(time.ctime(1711343045))  # Convert timestamp to human-readable format
```

---

# 📌 **4. Sleeping (Delaying Execution) - `time.sleep()`**
Agar **program execution delay** karni ho to `time.sleep(seconds)` ka use hota hai.
```python
import time
print("Start")
time.sleep(3)  # 3 seconds ke liye wait karega
print("End")
```
✅ **Use case:** API calls, animations, retry logic, etc.

---

# 📌 **5. Getting Current Local Time (`time.localtime()`)**
Ye function **current system time** ko **structured format** me return karta hai.

```python
import time
current_time = time.localtime()
print(current_time)  
```
✅ **Output Example:**  
```
time.struct_time(tm_year=2025, tm_mon=3, tm_mday=25, tm_hour=12, tm_min=45, tm_sec=30, ...)
```

### ✅ **Extracting Specific Time Components**
```python
print(current_time.tm_year)   # 2025
print(current_time.tm_mon)    # 3  (March)
print(current_time.tm_mday)   # 25 (Day)
print(current_time.tm_hour)   # 12 (Hours)
print(current_time.tm_min)    # 45 (Minutes)
print(current_time.tm_sec)    # 30 (Seconds)
```

---

# 📌 **6. Converting Time to String (`time.strftime()`)**
Agar **date & time** ko **custom format** me convert karna ho, to `strftime()` use hota hai.

```python
import time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(formatted_time)  # Output: "2025-03-25 12:45:30"
```

### ✅ **Common Format Codes**
| **Code** | **Description** | **Example** |
|----------|---------------|-------------|
| `%Y`     | Year (4-digit) | `2025` |
| `%m`     | Month (2-digit) | `03` (March) |
| `%d`     | Day of Month | `25` |
| `%H`     | Hours (24-hour format) | `12` |
| `%I`     | Hours (12-hour format) | `12` |
| `%p`     | AM/PM | `PM` |
| `%M`     | Minutes | `45` |
| `%S`     | Seconds | `30` |
| `%A`     | Weekday Name | `Monday` |
| `%B`     | Month Name | `March` |

---

# 📌 **7. Converting String to Time (`time.strptime()`)**
Agar **string formatted time ko structured time me convert** karna ho to `strptime()` use hota hai.

```python
import time
time_string = "2025-03-25 12:45:30"
time_struct = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(time_struct)  # Output: struct_time object
```

---

# 📌 **8. Converting Struct Time to Timestamp (`time.mktime()`)**
Agar **structured time ko timestamp (seconds) me convert** karna ho, to `mktime()` use hota hai.

```python
import time
time_struct = time.localtime()
timestamp = time.mktime(time_struct)
print(timestamp)  # Output: 1711343045.0 (Seconds since 1970)
```

---

# 📌 **9. Measuring Execution Time (`time.perf_counter()`)**
Agar kisi **code block ka execution time** calculate karna ho, to `perf_counter()` use hota hai.

```python
import time
start = time.perf_counter()

# Code block whose time we want to measure
for i in range(1000000):
    pass  

end = time.perf_counter()
print(f"Execution Time: {end - start} seconds")
```

---

# 📌 **🔥 Summary (Time Module at a Glance)**
| **Function** | **Purpose** |
|-------------|------------|
| `time.time()` | Current timestamp (seconds since 1970) |
| `time.ctime(timestamp)` | Convert timestamp to human-readable format |
| `time.sleep(seconds)` | Pause execution for given seconds |
| `time.localtime()` | Get current local time in structured format |
| `time.strftime(format, struct_time)` | Convert struct_time to string format |
| `time.strptime(string, format)` | Convert string format time to struct_time |
| `time.mktime(struct_time)` | Convert struct_time to timestamp |
| `time.perf_counter()` | Get high-precision performance counter |

---

## 🤔 **Koi Doubt Hai?**
Agar `datetime` module ya `time zone handling` ke concepts chahiye to batao! 😊