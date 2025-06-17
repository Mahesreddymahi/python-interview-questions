"""
Q10: Can we use a list as a key in a dictionary?

- No. Lists are mutable and unhashable.
- Tuples (immutable) can be used.
"""

# Example
# d = {[1, 2]: "value"}  # ❌ TypeError
d = {(1, 2): "value"}     # ✅
print(d)
