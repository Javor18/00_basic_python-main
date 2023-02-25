# Write a Python program to convert given a dictionary to a list of tuples.
# Sample Output:
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

dic = eval(input())

# TODO: Here dic.items() is already a list of tuples
sort_dic = [(key, value) for key, value in dic.items()]

print(sort_dic)