# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def exercise_12(list_colors: list) -> bool:
    # Your code here

    filtered_list = [x for x in list_colors if x != list_colors[0] and x != list_colors[4] and x != list_colors[5]]

    return filtered_list

list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

assert exercise_12(list1) == ['Green', 'White', 'Black']