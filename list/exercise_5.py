string_list = ['abc', 'xyz', 'aba', '1221']

# Write a Python program to count the number of strings
# where the string length is 2 or more
# and the first and last character are same from a given list of strings.


def exercise_5(strings: list) -> int:
    # Your code here

    strings_count = 0

    for string in string_list:

        if len(string) >= 2 and string[0] == string[-1]:

            strings_count += 1

    return strings_count


assert exercise_5(string_list) == 2
