# Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

list_z = eval(input())

new_list = []

keys = list_z.keys()

list_len = len(list(list_z.values())[0])

for x in range(list_len):

    new_dic = {}

    for key in keys:

        new_dic[key] = list_z[key][x]

    new_list.append(new_dic)

print(new_list)