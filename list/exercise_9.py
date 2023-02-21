# Write a Python program to clone or copy a list


def exercise_9(sample_list: list) -> bool:
    # Your code here

    copied_list = sample_list.copy()

    return copied_list


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_9(string_list) is not string_list
assert exercise_9(string_list) == string_list