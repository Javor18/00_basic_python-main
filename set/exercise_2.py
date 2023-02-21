# Write a Python program to remove item(s) from a given set.


def exercise_2(set_2: set) -> set:
    # Your code here

    items_to_remove = {"Fox", "Cat"}

    set_2.difference_update(items_to_remove)

    return set_2


# animals_set = set("Fox", "Eagle", "Dog", "Cat")

animals_set = {"Fox", "Eagle", "Dog", "Cat"}

assert exercise_2(animals_set) == {"Eagle", "Dog"}