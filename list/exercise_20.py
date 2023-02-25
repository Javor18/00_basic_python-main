# Write a Python program to count integer in a given mixed list.

def exercise_20(list1: list) -> int:
    # Your code here

    count = 0

    # TODO: You could also create a list comprehension
    #  taking only integers and doing a len on it

    for x in list1:

        if isinstance(x, int):

            count += x

    return count


list1 = [1, 2, 'a', 'b', 50]

assert exercise_20(list1) == 53
