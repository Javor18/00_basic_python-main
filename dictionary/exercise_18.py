# Write a Python program to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')

dic = eval(input())

max_value = max(dic, key=dic.get)
min_value = min(dic, key=dic.get)

print((max_value, min_value))