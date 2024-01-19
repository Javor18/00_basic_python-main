# Write a Python program to create an intersection of sets


def exercise_3(first_set: set, second_set: set) -> set:
    # Your code here

    filtered_set = first_set & second_set

    return filtered_set


set_1 = {"Ferrari", "Mercedes"}
set_2 = {"Ferrari", "Mclaren"}

assert exercise_3(set_1, set_2) == {"Ferrari"}