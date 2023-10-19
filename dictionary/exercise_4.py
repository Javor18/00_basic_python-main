# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

from heapq import nlargest

dict1 = {
    'a': [10, 30, 100, 1, 200, 12, 13],
    'b': [1, 5, 3, 2, 14, 13, 19],
    'c': [4, 5, 123, 411, 213]
}

def exercise_4(dict1):

    top_3_nums_dict = {}

    for key, value in dict1.items():

        top_3_nums = nlargest(3, value)

        top_3_nums_dict[key] = top_3_nums

    return top_3_nums_dict

print(exercise_4(dict1))