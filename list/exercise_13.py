# Write a Python program to print the numbers of a specified list after removing even numbers from it.

def exercise_13(list1: list) -> bool:
    # Your code here

    filtered_list = [x for x in list1 if x % 2 != 0]

    return filtered_list


list1 = [1, 2, 46, 7, 8, 9, 56]
assert exercise_13(list1) == [1, 7, 9]

list1 = [1, 78, 26, 7, 56, 27, 304]
assert exercise_13(list1) == [1, 7, 27]