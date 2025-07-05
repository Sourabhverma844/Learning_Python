# Set Basics in Python
"""
Set{} is a collection of items. Like lists, sets can contain elements of the same or different types.

Points To Remember:
- Only distinct elements are allowed
- Sets are unordered
- No indexing support
- Set operations like union, intersection, and difference are fast because sets use **hashing internally**
"""

s1 = {10, 20, 30}
print(s1)

# Creating set using constructor
s2 = set([20, 30, 40])
print(s2)

# Creating an empty set like this will make a dictionary, not a set
s3 = {}
print(type(s3))  # <class 'dict'>

# Correct way to create an empty set
s4 = set()
print(type(s4))  # <class 'set'>
print(s4)

###############################################

scores = {10, 20}

# .add(value) adds a new element
scores.add(30)
print(scores)

# Adding duplicate element has no effect
scores.add(20)
print(scores)

# .update(iterable) adds multiple elements
scores.update([40, 50])
print(scores)

# Can pass multiple iterables to update
scores.update([60, 70], [80, 90])
print(scores)

###############################################

s = {10, 30, 20, 40}

# .discard(value) removes the element if present; does nothing if not
s.discard(30)
print(s)

# .remove(value) removes the element if present;  throws error if not found
s.remove(20)
print(s)

# .clear() removes all elements
s.clear()
print(s)

# You can still add after clear()
s.add(50)
print(s)

# del deletes the entire set object
del s
# print(s)  # This will raise an error (NameError)

###############################################

fruits = {"Mango", "Apple", "Banana"}

# len(set) returns the number of elements
print(len(fruits))

# Membership test
print("Mango" in fruits)   # True
print("Orange" in fruits)  # False

###############################################

set1 = {2, 4, 6, 8}
set2 = {3, 6, 9}

# Union
print(set1 | set2)
print(set1.union(set2))

# Intersection
print(set1 & set2)
print(set1.intersection(set2))

# Difference
print(set1 - set2)
print(set2 - set1)

# Symmetric Difference
print(set1 ^ set2)
print(set2.symmetric_difference(set1))

###############################################

seta = {2, 4, 6, 8}
setb = {4, 8}

# isdisjoint(): True if no common element
print(seta.isdisjoint(setb))  # False

# issubset() / <= : True if all elements of A are in B
print(seta <= setb)
print(seta.issubset(setb))

# < checks for proper subset
print(seta < setb)

# issuperset() / >=
print(seta.issuperset(setb))  # True
print(seta >= setb)

# > checks for proper superset
print(seta > setb)
