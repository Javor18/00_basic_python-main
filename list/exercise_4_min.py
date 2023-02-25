numbers = [1, 2, 3, 4]

# Write a Python program to get the largest number from a list.

def exercise_4(numbers: list) -> int:
    # Your code here
    # TODO: Can you do another version without using min?
    return min(numbers)

largest_number = exercise_4(numbers)
assert largest_number == 1
