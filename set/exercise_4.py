# Write a Python program to create a union of sets.


def exercise_4(first_set: set, second_set: set) -> set:
    # Your code here

    filtered_set = first_set.union(second_set)

    return filtered_set


cars_1 = {"Ferrari", "Mercedes"}
cars_2 = {"Ferrari", "Mclaren"}

assert exercise_4(cars_1, cars_2) == {"Mclaren", "Mercedes", "Ferrari"}
assert exercise_4(cars_1, cars_2) == {"Mercedes", "Ferrari", "Mclaren"}