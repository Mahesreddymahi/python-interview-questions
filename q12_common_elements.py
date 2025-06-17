"""
Q12: Write a code to find common elements in two lists using set operations
"""

# Example
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print("Common Elements:", common)
