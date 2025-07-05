# -------------------------------------------
# Python print() Function
# -------------------------------------------

"""
The print() function in Python

- A function is a set of instructions that takes some input, performs an operation, and gives an output.
- The print() function displays output on the screen.
"""

# Basic usage
print("Hello")
print("I am Sourabh Verma")

# Blank line
print()

print("I am gonna become super rich")

# -------------------------------------------
# Using 'end' and 'sep' parameters in print()
# -------------------------------------------

"""
end
- By default, print() adds a newline at the end.
- You can change that using end="".

sep
- By default, print() separates items with space.
- You can change the separator using sep="".
"""

# end="" joins this print with next one
print("Hello", end="")        # No newline here
print(" I am Sourabh")        # Continues on same line

# sep="-" adds separator between printed items
print("15", "16", "1928", sep="-")  # Output: 15-16-1928

# Combining sep and end
print(10, 20, 30, sep="+", end="")  # Output: 10+20+30
print(40, 50)                       # Continues immediately after previous line

# -------------------------------------------
# Summary
# -------------------------------------------

"""
✅ print("...")             → Print string or values
✅ print(a, b, c)           → Print multiple values with space by default
✅ print(..., sep="-")      → Separate values with custom separator
✅ print(..., end="---")    → Control how the line ends (e.g., no newline or custom string)

Common Use Cases:
- Print simple messages
- Format output with separators or continuation
- Debugging values and expressions
"""