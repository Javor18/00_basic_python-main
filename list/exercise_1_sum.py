numbers = [1, 2, 3, 4]

# Write a Python program to multiply all the items in a list.


def exercise_2(numbers: list) -> int:
    # Your code here

    total = 0

    for x in numbers:

        total += x

    return total

total = exercise_2(numbers)
assert total == 10