# Write a Python program to create a multidimensional list (lists of lists) with zeros. Go to the editor
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

def exercise_19(col, row) -> list:
    # Your code here

    result = []

    for i in range(col):

        list = [0] * row

        result.append(list)

    return result


assert exercise_19(2, 3) == [
    [0, 0, 0],
    [0, 0, 0]
]