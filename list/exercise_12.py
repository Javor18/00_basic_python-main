# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def exercise_12(list_colors: list) -> bool:
    # Your code here

    # del list_colors[5]
    # del list_colors[4]
    # del list_colors[0]
    #
    # return list_colors

    # TODO: Here, you could go simple
    #   You could remove elements by value as well using
    #   remove: https://www.w3schools.com/python/python_lists_remove.asp
    filtered_list = []

    for x in range(len(list_colors)):

        if x != 0 and x != 4 and x != 5:

            filtered_list.append(list_colors[x])

    return filtered_list

list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

assert exercise_12(list1) == ['Green', 'White', 'Black']