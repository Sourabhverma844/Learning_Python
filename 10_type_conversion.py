# -------------------------------------------
# Type Conversion
# -------------------------------------------

"""
Type Conversion in Python

Implicit Type Conversion:
   - Python automatically converts one data type to another without any manual effort.

Explicit Type Conversion:
   - We manually convert one data type to another using functions like int(), float(), str(), etc.
"""

# -------------------------------------------
# Implicit Type Conversion
# -------------------------------------------

a = 10
b = 1.5
c = a + b  # int + float → float
print(c)           # Output: 11.5
print(type(c))     # Output: <class 'float'>

d = True  # True is treated as 1 in arithmetic
e = a + d
print(e)           # Output: 11

# -------------------------------------------
# Explicit Type Conversion
# -------------------------------------------

f = "135"
g = 10 + int(f)     # string to int
h = float(g)        # int to float
print(g)            # Output: 145
print(h)            # Output: 145.0

# String to list, tuple, set
i = "Sourabh"
print(list(i))      # ['S', 'o', 'u', 'r', 'a', 'b', 'h']
print(tuple(i))     # ('S', 'o', 'u', 'r', 'a', 'b', 'h')
print(set(i))       # Unordered unique characters

# Containers to string
j = [1, 2, 3]
k = ("monday", "tuesday")
l = {'a', 'b', 'c'}

print(j)            # [1, 2, 3]
print(k)            # ('monday', 'tuesday')
print(l)            # {'a', 'b', 'c'}
print(type(j), type(k), type(l))

m = str(j)
n = str(k)
o = str(l)
print(type(m), type(n), type(o))
print(m)
print(n)
print(o)

# Number to string (for concatenation)
p = 10
q = 11
print(str(p) + str(q))  # Output: "1011"

r = 12.5
print(str(r))           # Output: "12.5"

# Tuple / Set to List
s = (10, 20, 30)
print(list(s))

t = {10, 20, 40}
print(list(t))

# -------------------------------------------
# Base Conversions
# -------------------------------------------

numb = 20

# Decimal to Binary, Hexadecimal, Octal
print(bin(numb))  # Output: '0b10100'
print(hex(numb))  # Output: '0x14'
print(oct(numb))  # Output: '0o24'

# Binary (string) to Decimal
binary_numb = "1001"
print(int(binary_numb, 2))  # Output: 9

# Octal (string) to Decimal
octal_numb = "12"
print(int(octal_numb, 8))   # Output: 10

# Hexadecimal (string) to Decimal
hexadecimal_numb = "A1"
print(int(hexadecimal_numb, 16))  # Output: 161

# -------------------------------------------
# Common Conversion Functions
# -------------------------------------------

"""
Common Conversion Functions:

int(x)       → Converts to integer
float(x)     → Converts to float
str(x)       → Converts to string
list(x)      → Converts to list
tuple(x)     → Converts to tuple
set(x)       → Converts to set
bin(x)       → Converts to binary string (prefixed with '0b')
oct(x)       → Converts to octal string (prefixed with '0o')
hex(x)       → Converts to hexadecimal string (prefixed with '0x')
int(x, base) → Converts string from given base (2, 8, 16) to decimal
"""