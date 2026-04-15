
def clean_database(record_ids):
    # Requirement: Remove all odd numbers from the list
    cleaned = [record_id for record_id in record_ids if record_id % 2 == 0]
    return cleaned

# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]

# Task 2: Explanation
# Observation: The bug first appeared at index 1, where the loop skipped the odd number 3.
# While debugging in VS Code, I set a breakpoint inside the loop.

# Why: Removing items while looping forward shifts elements left, 
# causing the next element to be skipped. For example, 
# when 1 is removed, 3 moves to index 0, but the loop moves to index 1, skipping 3.
# This makes the loop "blind" to the next element.


# Fix 2: Build a new list with only even numbers (immutable approach).
#By using a list comprehension to create a new list of even numbers,
# This way, we avoid modifying the list while iterating,
# and we get a clean result without skipping any elements.
