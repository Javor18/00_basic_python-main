# Write a Python program to create a multidimensional list (lists of lists) with zeros. Go to the editor
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

def exercise_19(col, row) -> list:
    # Your code here

    result = []

    # TODO: You could a list comprehension here as well and do it in one line
    for i in range(col):

        # TODO: here be careful about the naming
        #   list is reserved because of the list type + could be more specific
        #   I would have potentially do a one liner with list=.. and append here because simple
        list = [0] * row

        result.append(list)

    return result


assert exercise_19(2, 3) == [
    [0, 0, 0],
    [0, 0, 0]
]