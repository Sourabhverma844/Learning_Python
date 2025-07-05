"""
Program to take two numbers as input from user and perform addition.

Note:
- input() always returns string.
- So, directly adding input values without conversion will result in string concatenation.
"""

# Taking input from user
x = input("Enter First Number : ")
y = input("Enter Second Number : ")

# Example of wrong way (commented):
# result = x + y
# print("Sum is : " + result)
# If x = "10" and y = "4", result will be "104" (string concat, not sum)

# Correct way using explicit type conversion
result = int(x) + int(y)

# Printing result
print("Sum is : ", result)

# Also works with float:
# result = float(x) + float(y)