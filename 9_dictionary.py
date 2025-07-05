
"""
Dictionary in Python
- Collection of key-value pairs
- Unordered (insertion order preserved from Python 3.7+)
- All keys must be unique
- Values may be repeated
- Uses hashing internally
"""

# Creating a dictionary
emp_data = {
    "name": "Sourabh",
    "companey": "ripple",
    "Salary": 120000,
    "commission": 120000
}
print(emp_data)

# Creating an empty dictionary
mobile_data = {}
print(mobile_data)

# Adding key-value pairs
mobile_data["mobile"] = "Motorola G84"
mobile_data["price"] = 15800
mobile_data["RAM"] = "128GB"
print(mobile_data)

# Accessing values using key
print(mobile_data["mobile"])  # Output: Motorola G84

# Safe access using get()
print(emp_data.get("Salary"))    # Output: 120000
print(emp_data.get("Height"))    # Output: None

# get() with default value
print(emp_data.get("Height", "NA"))   # Output: NA
print(mobile_data.get("RAM", "NA"))   # Output: 128GB

# Checking if key exists
if "price" in mobile_data:
    print(mobile_data["price"])
else:
    print("NA")

###########################################################################

# Modifying a Dictionary

d = {
    110: "abc",
    101: "xyz",
    105: "pqr",
    106: "bcd"
}
print(d)

# Updating value of a key
d[110] = "Hello"
print(d)

# Getting length of dictionary
print(len(d))  # Output: 4

# Removing an item using pop()
print(d.pop(110))  # Removes key 110
print(d)

# Removing using del
del d[106]
print(d)

# Adding new item
d[108] = "cde"
print(d)

#  Removing last inserted item using popitem()
print(d.popitem())  # Returns (key, value) tuple

###################################################### 
"""
dict[key]                → Access value by key (KeyError if not found)
dict.get(key, default)   → Access safely (returns default if key not found)
dict[key] = value        → Add or update key
dict.pop(key)            → Remove by key (returns value)
dict.popitem()           → Remove last inserted item (returns tuple)
del dict[key]            → Delete item by key
"key" in dict            → Check if key exists (returns True/False)
len(dict)                → Total number of key-value pairs
"""

# Use Cases
# Dictionaries are ideal for storing:
# Employee data
# Product info
# Config settings
# API JSON responses
