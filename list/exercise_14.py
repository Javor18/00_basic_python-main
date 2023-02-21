# Write a Python program to get the frequency of the elements in a list.
def exercise_14(list1: list) -> dict:
    # Your code here

    filtered_list = {}

    for x in list1:

        if not x in filtered_list:

            filtered_list[x] = 1

        else:
            filtered_list[x] += 1

    return filtered_list


list1 = ["a", "a", "b", "b", "c", "d", "d", "d"]

assert exercise_14(list1) == {
    'a': 2,
    'b': 2,
    'c': 1,
    'd': 3
}