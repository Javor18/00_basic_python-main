# Write a Python program to drop empty Items from a given Dictionary.

# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


def exercise_7(list):

    # TODO: Rename this variable, not a list :)
    new_list = {}

    for key, value in list.items():

        if value is not None:

            new_list[key] = value

    return new_list


list = eval(input())

print(exercise_7(list))