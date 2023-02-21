# Write a Python program to check if a given set is superset of itself and superset of another given set


def exercise_15(first_set, second_set):
    # Your code here
    return first_set.issuperset(second_set)


big_set = {"Pear", "Apple", "Peach"}
small_set = {"Peach"}

assert exercise_15(big_set, small_set) is True
assert exercise_15(small_set, big_set) is False
