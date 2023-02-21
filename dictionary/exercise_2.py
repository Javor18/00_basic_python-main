# Write a Python program to remove duplicates from Dictionary.

dict1 = {
    ("1"): 2,
    ("2"): 2,
    ("3"): 4
}


def exercise_2(dict1):
    # Your code here

    unique_dict = {}

    for key, value in dict1.items():

        if value not in unique_dict.values():

            unique_dict[key] = value

    return unique_dict


assert exercise_2(dict1) == {("3"): 4}
