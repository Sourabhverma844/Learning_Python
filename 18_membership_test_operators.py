"""
Membership Test Operators in Python

Python provides two membership test operators:
    in      → Returns True if the item exists
    not in  → Returns True if the item does NOT exist

These operators are used to check for membership in:
    - Strings (substring search)
    - Lists, Tuples, Sets (element membership)
    - Dictionaries (key existence)

- In strings, the substring must be continuous
- In dictionaries, these operators check for keys, not values
"""

# Example: Using 'in' with a string
name = "sourabh"
print("s" in name)         # True — 's' is in the string
print("rab" in name)       # True — 'rab' is a continuous substring
print("za " in name)       # False — 'za ' is not in the string

# Example: Using 'in' with a dictionary (checks only keys)
empdata = {101: "Sourabh", 201: "Aniket"}
print(101 in empdata)      # True — key 101 exists
print(301 in empdata)      # False — key 301 does not exist

# Example: Using 'in' and 'not in' with a list
score = [10, 20, 30]
print(10 in score)         # True — 10 is in the list
print(100 in score)        # False — 100 is not in the list
print([20, 30] in score)   # False — [20, 30] is a sublist, not an individual element

# Important distinction:
# Even though [20, 30] appears together in `score`, Python checks elements, not patterns.

# Using 'not in' operator
print(30 not in score)     # False — 30 IS in the list
print(40 not in score)     # True — 40 is NOT in the list
print([20, 30] not in score)  # rue — sublist [20, 30] is NOT a member