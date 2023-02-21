# Write a Python program to add member(s) in a set.


def exercise_1_first_solution(fruits_set: set) -> set:
    # Your code here

    fruits_set.update({"🥝", "🍐", "🍓", "Orange", "🥭", "Peach"})

    return fruits_set


fruits_set = {"🍐"}

assert exercise_1_first_solution(fruits_set) == {"🥝", "🍐", "🍓", "Orange", "🥭", "Peach"}