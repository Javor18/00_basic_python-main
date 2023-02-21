# Write a Python program to create an intersection of sets


def exercise_3(first_set: set, second_set: set) -> set:
    # Your code here

    # filtered_set = set_1.intersection(set_2)

    filtered_set = set_1 & set_2

    return filtered_set


set_1 = {"Ferrari", "Mercedes"}
set_2 = {"Ferrari", "Mclaren"}

assert exercise_3(set_1, set_2) == {"Ferrari"}