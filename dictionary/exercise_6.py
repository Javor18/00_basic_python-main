# Write a Python program to create a dictionary from two lists without losing duplicate values.

# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})

from collections import defaultdict

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]

def exercise_6(list1, list2):

    default_dict = defaultdict(set)

    for key, value in zip(list1, list2):

        default_dict[key].add(value)

    return default_dict

print(exercise_6(list1, list2))