# Write a Python program to iteration over sets


def exercise_19(cars: set):
    # Your code here

    for car in cars:

        print(car)

    return True

cars = {"Ferrari", "Mercedes", "Peugeot"}

assert exercise_19(cars)