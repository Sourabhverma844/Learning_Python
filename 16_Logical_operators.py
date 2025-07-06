"""
Logical Operators and Short-Circuiting in Python
"""

a = 10
b = 20
c = 30

# Logical AND (True if both conditions are True)
print(a < b and b < c)  # True and True → True

# Logical OR (True if at least one condition is True)
print(a < b or b > c)   # True or False → True

# Logical NOT (Inverts the boolean value)
print(not a > b)        # not False → True

"""
What is Short-Circuiting?

In logical operations, Python uses short-circuit evaluation:
   - For `and`: If the first operand is False, Python skips evaluating the second operand.
   - For `or`: If the first operand is True, Python skips evaluating the second operand.

This makes the program efficient and can prevent unnecessary computations or errors.
"""

# Example with strings
s1 = ""  # Empty string is treated as False
s2 = s1 or "DefaultStr"  # If s1 is False, it returns the second operand
print(s2)  # Output: DefaultStr

"""
Non-Boolean Values in Logical Operators (Unique to Python)

Unlike C or Java, Python's `and` and `or` operators do not always return True/False.
They return the last evaluated operand.
"""

# Using integers with `or`
x = 10  # Non-zero is treated as True
print(x or 20)  # Output: 10 → because x is True, second operand not evaluated

# Question: What is the last value evaluated here?
# Answer: x → 10 (due to short-circuiting)

y = 0  # Zero is treated as False
print(y or 30)  # Output: 30 → because y is False, so evaluates and returns second operand

# Using `and`
z = 40  # Non-zero is True
print(z and 50)  # Output: 50 → both True, returns second operand

"""
Summary:

- Short-circuiting skips unnecessary evaluations.
- Logical operators in Python return actual operand values (not just True/False).
- You can use these features for defaults, safe access, or concise logic expressions.
"""
