# Write a Python program to check all values are same in a dictionary.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False

list = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}


def exercise_8(list: dict, value:any) -> bool:

    return all(x == value for x in list.values())

print(exercise_8(list, 12))
print(exercise_8(list, 10))