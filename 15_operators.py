"""
Arithmetic Operators in Python
"""

x = 9
y = 4

# Addition
print(x + y)     # 13

# Subtraction
print(x - y)     # 5

# Division (always returns float)
print(x / y)     # 2.25

# Multiplication
print(x * y)     # 36

# // Floor Division: Discards the decimal part
print(x // y)    # 2

# % Modulus: Gives remainder
print(x % y)     # 1

# ** Exponentiation (Power)
print(x ** y)    # 6561

# Floor Division with negative numbers
x = -5
y = 2
print(x // y)    # -3 → because -5 // 2 gives the floor value, which is -3 (not -2)

# Floor Division with float
x = 5.0
y = 2
print(x // y)    # 2.0 → Result type is float if any operand is float

# ** Negative Exponentiation
x = 2
y = -2
print(x ** y)    # 0.25 → Equivalent to 1 / (2 ** 2)

"""
Operator Precedence
----------------------
Highest precedence operators are evaluated first:

1. **       → Highest
2. * / // % → Higher
3. + -      → Lower

"""
print(5 + 2 * 3)       # 5 + (2*3) = 11
print(5 + 3 * 4 ** 2)  # 5 + 3 * (4**2) = 5 + 3 * 16 = 53

"""
Associativity of Operators
----------------------------
When operators have the same precedence, associativity decides the order of evaluation:

Left to Right:
+ - * / // %

Right to Left:
** (Exponentiation)

Examples:
"""
print(5 + 4 - 2)       # (5 + 4) - 2 = 7
print(2 ** 2 ** -1)    # 2 ** (2 ** -1) = 2 ** 0.5 = √2 ≈ 1.414
print((2 ** 2) ** -1)  # (4) ** -1 = 1/4 = 0.25
