# Write a Python program to create a shallow copy of sets


def exercise_8(animals: set) -> set:
    # Your code here

    copied_list = animals.copy()

    return copied_list


animals = {"Fox", "Cat", "Dog"}

assert id(exercise_8(animals)) != id(animals)