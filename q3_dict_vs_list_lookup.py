"""
Q3: Why are dictionaries faster than lists for lookups?

- Dictionary uses hashing (hash table) which provides O(1) time complexity.
- List lookup requires iteration (O(n)).
"""

# Example
students_dict = {'101': 'Alice', '102': 'Bob'}
print("Using dict:", students_dict['101'])  # Fast

students_list = [('101', 'Alice'), ('102', 'Bob')]
for id, name in students_list:
    if id == '101':
        print("Using list:", name)
