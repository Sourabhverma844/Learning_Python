"""
Identity Operators in Python: `is` and `is not`

The `is` operator checks whether two variables point to the same memory location (object identity).
- Returns `True` if both variables reference the same object (i.e., same `id()`).
- The `is not` operator is simply the negation of `is`.

Think of `is` as checking: "Are these exactly the same object, not just equal?"
"""

# Integer Literals (Immutable)
x1 = 10
x2 = 10

# Float Literals (Immutable)
y1 = 10.5
y2 = 10.5

# String Literals (Immutable)
z1 = "sourabhvermaworksinripple"
z2 = "sourabhvermaworksinripple"

# Identity checks
print(x1 is x2)  # True (same memory for small integers)
print(y1 is y2)  # True (Python may optimize float reuse)
print(z1 is z2)  # True (string interning for identical literals)

"""
Note: When assigning literals (like int, float, str) to variables, 
Python may reuse the same object in memory for optimization.
That's why identical literals can share the same `id()`.
"""

# None type (singleton object)
x1 = None
x2 = None
print(x1 is x2)  # True → there's only one `None` object in Python

# View their IDs
print(id(x1))
print(id(x2))

"""
WARNING: This identity behavior does not apply to containers like `list`, `tuple`, `dict`, etc.
Each time you create a container, Python creates a new object.
"""

# List (mutable container)
l1 = [10, 20, 30]
l2 = [10, 20, 30]

print(l1 is l2)       # False → different list objects even if content is same
print(id(l1))         # ID of l1
print(id(l2))         # ID of l2

"""
Use `is` when you care about object identity (e.g., `None` checks).
Use `==` when you care about value equality.
"""
