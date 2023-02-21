# Write a Python program to create set difference.


def exercise_5(first_set: set, second_set: set) -> set:
    # Your code here

    filtered_set = first_set.difference(second_set)

    return filtered_set


cars_1 = {"Ferrari", "Mercedes"}
cars_2 = {"Ferrari", "Mclaren"}

assert exercise_5(cars_1, cars_2) == {"Mercedes"}