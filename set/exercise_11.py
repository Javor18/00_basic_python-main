# Write a Python program to find maximum and the minimum value in a set.


def exercise_11(prices: set):
    # Your code here

    max_numm = max(prices)
    min_num = min(prices)

    return max_numm, min_num


prices = {20000, 400, 30, 72000}

assert exercise_11(prices) == 72000, 30
