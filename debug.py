
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



# Fix 1 (modify original list):
# Loop backwards with range(len(list)-1, -1, -1). Removing items
# from the end avoids skipping because earlier elements aren’t affected.
def clean_database(record_ids):
    # Fix 1: Loop backwards to safely remove odd numbers
    for i in range(len(record_ids) - 1, -1, -1):
        if record_ids[i] % 2 != 0:
            record_ids.pop(i)
    return record_ids

# Alternative Fix 2 (immutable approach):
# def clean_database(record_ids):
#     return [record_id for record_id in record_ids if record_id % 2 == 0]

# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]


# -------------------------------
# Task 2: Explanation
#
# Observation:
# The bug first appeared at index 1. After removing 1 at index 0,
# the list shifted left, so 3 moved into index 0. But the loop
# advanced to index 1 (now holding 4), skipping 3.
#
# Why:
# When you remove an item while looping forward, all later elements
# shift left. The loop’s pointer still moves forward, so the element
# that just shifted into the current index is never checked.
# This makes the loop "blind" to the next element.


