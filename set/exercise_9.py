# Write a Python program to remove all elements from a given set


def exercise_9(initial_set: set):
    # Your code here

    initial_set.clear()

    return dict(initial_set)


animals = {"Fox", "Cat", "Dog"}

assert exercise_9(animals) == {}
