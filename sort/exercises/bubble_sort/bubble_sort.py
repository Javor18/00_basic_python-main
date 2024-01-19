# https://www.youtube.com/watch?v=Jdtq5uKz-w4

numbers = [5, 7, 4, 2, 8, 3, 6, 1]

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(numbers)

bubble_sort(numbers)