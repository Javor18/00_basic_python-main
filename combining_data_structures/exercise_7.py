# Write a program to return the only combination of numbers unique in the list
from typing import List, Tuple

big_list = [
    (1, 4, 5, 7, 4),
    (4, 5, 7, 1, 4),
    (2, 3, 6, 9, 5),
    (1, 2, 3, 4, 5),
    (2, 3, 5, 6, 9)
]


def exercise_7(big_list: List[Tuple[int]]) -> Tuple:
    # Your code here. Try to find at least two ways to do it.

    unique_combinations = []

    # --------First way--------
    unique_combinations = []
    for combination in big_list:

        for x in combination:
            unique_combinations.append(x)

    unique_combinations = set(unique_combinations)
    print(unique_combinations)

    return tuple(unique_combinations)


assert exercise_7(big_list) == (1, 2, 3, 4, 5, 6, 7, 9)
