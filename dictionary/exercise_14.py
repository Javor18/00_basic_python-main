# Write a Python program to find all keys in the provided dictionary that have the given value.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Find all keys in the said dictionary that have the specified value:
# ['Roxanne', 'Betty']

def find_specified_value(dic, value):

    names = []

    for name, num in dic.items():

        if num == value:

            names.append(name)

    return names

dic = eval(input())
value = int(input())

print(find_specified_value(dic, value))