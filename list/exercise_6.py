sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def exercise_6(sample_list: list) -> list:
    # Your code here

    sample_list.sort(key=lambda x: x[1])
    return sample_list


assert exercise_6(sample_list) == [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]