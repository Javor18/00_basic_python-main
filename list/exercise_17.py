# Write a Python program to sort a list of nested dictionaries.
# Sort fruits by qty ascending

def exercise_17(list1: list) -> list:
    # Your code here

    sorted_list = sorted(list1, key=lambda x: x['qty'])

    return sorted_list


list1 = [
    {"fruit": "Apple", "qty": 4},
    {"fruit": "Peach", "qty": 10},
    {"fruit": "Plum", "qty": 5},
    {"fruit": "Banana", "qty": 8},
]

assert exercise_17(list1)