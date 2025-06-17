"""
Q13: What is the difference between 'is' and '==' for strings?

- '==' checks value equality
- 'is' checks object identity
"""

# Example
a = "hello"
b = "hello"
c = str("hello")

print("a == b:", a == b)
print("a is b:", a is b)
print("a is c:", a is c)
