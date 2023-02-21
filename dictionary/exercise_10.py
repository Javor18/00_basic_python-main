# A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary.
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}


dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
x = 0

for key in dict.keys():

    if key == 'Math':

        value_list = dict['Math']

        for i in range(len(value_list)):

            value_list[i] += 1

        dict['Math'] = value_list

    elif key == 'Physics':
        value_list = dict['Physics']

        for i in range(len(value_list)):

            value_list[i] -= 2

        dict['Physics'] = value_list


print(dict)