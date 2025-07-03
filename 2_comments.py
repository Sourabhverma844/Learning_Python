# COMMENTS IN PYTHON

# Comments are used to describe the purpose and functionality of the program to others.
# They make the code easier to understand for yourself and others.
# Comments start with the '#' symbol and are completely ignored by the Python interpreter.

# Example of a comment:
# This is a single-line comment
#-------------------------------------------------------

# ✅ FUNCTION WITH COMMENTS

# Function to remove special characters, trailing spaces, and leading spaces from inputStr

def clean_text(inputStr):
    """
    ✅ This is a docstring.
    It describes what the function does.

    This function takes a string (inputStr), and:
    - Removes leading and trailing spaces
    - Removes all characters except alphabets, numbers, and spaces

    Note:
    - This docstring is NOT a comment.
    - It is processed by Python's interpreter and can be accessed via help() or __doc__
    """
    cleaned = inputStr.strip()  # Removes leading and trailing spaces
    cleaned = ''.join(char for char in cleaned if char.isalnum() or char.isspace())  # Removes special characters
    return cleaned
# -------------------------------------------------------

# ✅ DOCSTRING VS COMMENT

# Comments → start with #, used for inline explanations, ignored by Python
# Docstrings → written in triple quotes (''' or """), used to document functions, classes, or modules

# Example usage of the function:
text = "  Hello, @Python!!!  "
print(clean_text(text))  # Output: Hello Python
