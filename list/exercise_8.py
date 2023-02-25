# Write a Python program to check a list is empty or not.


def exercise_8(sample_list: list) -> bool:
    # Your code here

    # TODO: here you could also do it in one line: return bool(sample_list)
    if len(sample_list) != 0:
        return True

    return False


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_8(string_list) is True
string_list = []
assert exercise_8(string_list) is False
