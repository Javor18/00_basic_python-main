string_list = ['abc', 'xyz', 'abc', '1221']

# Write a Python program to remove duplicates from a list.

def exercise_7(sample_list: list) -> set:
    # Your code here

    return set(sample_list)

assert exercise_7(string_list) == {'abc', 'xyz', '1221'}