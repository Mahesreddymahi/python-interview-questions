"""
Q7: What are nested dictionaries and how do you access inner values?

- A dictionary inside another dictionary.
"""

# Example
student = {
    "info": {"name": "Alice", "age": 22},
    "grades": {"math": 90, "science": 88}
}

print("Name:", student["info"]["name"])
print("Math grade:", student["grades"]["math"])
