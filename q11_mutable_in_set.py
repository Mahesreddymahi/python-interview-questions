"""
Q11: What happens if you try to add a mutable object to a set?

- It raises a TypeError. Only immutable (hashable) types can be added.
"""

# Example
# my_set = {[1, 2]}  # ❌ TypeError
my_set = {(1, 2)}     # ✅
print(my_set)
