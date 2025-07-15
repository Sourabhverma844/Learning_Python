# The abs() function in Python returns the absolute (non-negative) value of a number.
# When working with negative integers, using abs() ensures mathematical operations
# like modulo (%) behave as expected — particularly when extracting digits.

# Example Use Case:
# Extracting the last digit of an integer, whether it is positive or negative.

x = int(input("Enter x : "))
last_digit = abs(x) % 10
print("Last Digit is", last_digit)

# Why abs() is important here:
# If we do not use abs() and input a negative number like -121,
# the result can be misleading due to how Python handles modulo with negative values.

"""
Examples (Without abs):
-121 % 10 = 9
  (Because -121 = -13*10 + 9 → Remainder = 9)

49 % -10 = -1
  (Because 49 = -5*(-10) - 1 → Remainder = -1)

So to avoid negative or incorrect remainders when extracting digits,
we use abs() to make the number positive first.
"""
