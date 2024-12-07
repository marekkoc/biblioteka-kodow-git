# Strings can be surrounded by either single or double quotation marks
single_quoted_string = "Hello, World!"
double_quoted_string = "Hello, World!"

# Strings using single or double quotes interchangeably
print(single_quoted_string)
print(double_quoted_string)

# Multi-line strings using triple quotes
multi_line_string = """This is a multi-line string.
It spans multiple lines.
This is often used for documentation."""
print(multi_line_string)

# Strings behave like lists: slicing, concatenation, and searching
# Slicing
substring = single_quoted_string[0:5]
print("Sliced string:", substring)

# Concatenation
concatenated_string = single_quoted_string + " How are you?"
print("Concatenated string:", concatenated_string)

# Searching
search_result = "World" in single_quoted_string
print("Searching for 'World':", search_result)

# Reassigning string
single_quoted_string = "Goodbye, World!"
print("Reassigned string:", single_quoted_string)

# Python treats single characters and strings of characters as the same type
single_character = "A"
print("Type of single_character:", type(single_character))
print("Type of single_quoted_string:", type(single_quoted_string))
