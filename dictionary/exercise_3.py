# Write a Python program to print all unique values in a dictionary.

dict1 = {
    1: 3,
    2: 3,
    4: 70,
    67: 9888
}


def exercise_4(dict1):

    # TODO: You can create without using a set here
    unique_values = set()

    for value in dict1.values():

        unique_values.add(value)

    print(unique_values)

    pass


exercise_4(dict1)
