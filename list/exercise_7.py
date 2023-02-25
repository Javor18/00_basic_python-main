string_list = ['abc', 'xyz', 'abc', '1221']

# Write a Python program to remove duplicates from a list.

def exercise_7(sample_list: list) -> set:
    # Your code here
    # TODO: Can you create another version without using set?
    return set(sample_list)

assert exercise_7(string_list) == set('abc', 'xyz', '1221')