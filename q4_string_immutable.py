"""
Q4: How are Python strings immutable if they allow operations like replace()?

- Strings are immutable; methods like replace() return a new string.
"""

# Example
text = "hello"
new_text = text.replace("h", "y")
print("Original:", text)
print("Modified:", new_text)
