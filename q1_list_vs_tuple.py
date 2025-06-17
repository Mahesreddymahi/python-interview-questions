"""
Q1: Difference Between List and Tuple in Python

- List:
    - Mutable (can be changed)
    - Defined using square brackets []
    - Slower than tuple
- Tuple:
    - Immutable (cannot be changed)
    - Defined using parentheses ()
    - Faster and hashable (can be used as dictionary keys)
"""

# Example
my_list = [1, 2, 3]
my_list.append(4)
print("List:", my_list)

my_tuple = (1, 2, 3)
# my_tuple.append(4) # This will raise an error
print("Tuple:", my_tuple)
