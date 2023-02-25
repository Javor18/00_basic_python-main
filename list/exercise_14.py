# Write a Python program to get the frequency of the elements in a list.
def exercise_14(list1: list) -> dict:
    # Your code here

    #TODO: I would rename this something more explicit because this is not a list
    filtered_list = {}

    # TODO: Python implement a simple way to do that as well:
    #   https://docs.python.org/3/library/collections.html#collections.Counter
    for x in list1:
        # TODO: I would do it in the other way to be more readable if x in filtered_.. else ..
        if not x in filtered_list:

            filtered_list[x] = 1

        else:
            filtered_list[x] += 1

    return filtered_list


list1 = ["a", "a", "b", "b", "c", "d", "d", "d"]

assert exercise_14(list1) == {
    'a': 2,
    'b': 2,
    'c': 1,
    'd': 3
}