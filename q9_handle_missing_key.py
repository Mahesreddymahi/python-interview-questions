"""
Q9: How would you handle missing key in a dictionary?

- Use get() or defaultdict to avoid KeyError.
"""

# Example using get()
my_dict = {'a': 1}
print(my_dict.get('b', 'Not Found'))
