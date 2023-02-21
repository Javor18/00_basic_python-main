# Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry

dic = {'physics': 1, 'math': 2, 'chemistry': 3}

list = list(dic.items())

for x in range(len(list)):

    key, value = list[x]

    print(key)