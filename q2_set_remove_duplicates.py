"""
Q2: How do sets help in removing duplicates from a list?

- Sets do not allow duplicate values.
- Converting a list to a set removes duplicates.
"""

# Example
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Original list:", numbers)
print("Unique list:", unique_numbers)
