# Write a Python program to remove spaces from dictionary keys.

dict1 = {
    " a": 1,
    "b b b": 2,
    "e  ": 3
}


def exercise_5(dict1):

    return {key.replace(' ', ''): value for key, value in dict1.items()}


assert exercise_5(dict1) == {"a": 1, "bbb": 2, "e": 3}