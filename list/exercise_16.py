# Write a Python program to insert an element before each element of a list.

def exercise_16(list1: list, element) -> list:
    # Your code here

    filtered_list = []

    for x in list1:

        filtered_list.append(element)
        filtered_list.append(x)

    return filtered_list


list1 = [1, 2, 3, 4]
list2 = exercise_16(list1, '-')
assert list2 == ["-", 1, "-", 2, "-", 3, "-", 4]

list1 = [1, 2, 3]
list2 = exercise_16(list1, '*')
assert list2 == ["*", 1, "*", 2, "*", 3]