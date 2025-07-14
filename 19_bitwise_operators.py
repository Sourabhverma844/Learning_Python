"""
Bitwise Operators in Python

Bitwise operators work at the bit level — they operate on binary representations of integers.

You can convert:
- Integer to Binary using: bin(value)
- Binary to Integer using: int("binary_str", 2)
"""

# Convert int to binary
print(bin(18))   # Output: '0b10010'
print(bin(12))   # Output: '0b1100'

# Convert binary string to int
print(int("0b10010", 2))   # Output: 18
print(int("0b1100", 2))    # Output: 12

"""
Bitwise AND (&) Operator

How it works:
- Converts both numbers to binary
- Compares each bit: returns 1 only if both bits are 1, else returns 0
- Final result is converted back to decimal
"""

x = 3      # Binary: 011
y = 6      # Binary: 110
print(x & y)   # Output: 2 (Binary: 010)

# Explanation:
#     011   (3)
#   & 110   (6)
#   ------
#     010   → 2

"""
Bitwise OR (|) Operator

If any input bit is 1, output bit is 1.
Only returns 0 when both bits are 0.
"""

print(x | y)   # Output: 7 (Binary: 111)

# Explanation:
#     011
#   | 110
#   ------
#     111 → 7

"""
Bitwise XOR (^) Operator

XOR returns:
- 0 if both bits are the same
- 1 if bits are different
"""

print(x ^ y)   # Output: 5 (Binary: 101)

# Explanation:
#     011
#   ^ 110
#   ------
#     101 → 5

"""
Summary:

Operator | Name        | Meaning (Bit-Level)
---------|-------------|----------------------
&        | AND         | 1 only if both bits are 1
|        | OR          | 1 if any one bit is 1
^        | XOR         | 1 if bits are different
"""
#---------------------------------------------------------

"""
Remaining Bitwise Operators in Python

In addition to &, |, ^ — Python also provides:

Bitwise NOT (~)
Left Shift (<<)
Right Shift (>>)

These also operate on binary (bit-level) representations of integers.
"""

# -----------------------------------------------------
# Bitwise NOT (~)
"""
~x: Inverts all the bits of x
- In binary: flips 1s to 0s and 0s to 1s
- In Python: uses 2's complement representation
  So, ~x = -(x + 1)
"""

x = 5
print(~x)  # Output: -6

# Explanation:
# x = 5 → 00000101
# ~x = 11111010 → which is -6 in 2's complement

# -----------------------------------------------------
# Left Shift (<<)
"""
x << n: Shifts the bits of x to the left by n positions
- Equivalent to: x * (2 ** n)
- Adds n zeros at the right
"""

x = 3
print(x << 2)  # Output: 12

# Explanation:
# x = 3 → 00000011
# x << 2 → 00001100 → 12 in decimal

# -----------------------------------------------------
# Right Shift (>>)
"""
x >> n: Shifts the bits of x to the right by n positions
- Equivalent to: x // (2 ** n)
- Removes n bits from the right
"""

x = 16
print(x >> 2)  # Output: 4

# Explanation:
# x = 16 → 00010000
# x >> 2 → 00000100 → 4 in decimal

# -----------------------------------------------------
"""
Summary Table:

Operator | Name         | Description
---------|--------------|-----------------------------------------------
~        | Bitwise NOT  | Inverts bits, result = -(x + 1)
<<       | Left Shift   | Shifts bits to left (x * 2^n)
>>       | Right Shift  | Shifts bits to right (x // 2^n)
"""


