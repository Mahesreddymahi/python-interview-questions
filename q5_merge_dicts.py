"""
Q5: How to merge two dictionaries in Python (3.9+)

- Use the | operator to merge dictionaries.
"""

# Example
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print("Merged Dictionary:", merged)
