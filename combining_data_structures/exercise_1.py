# Write a program to filter cars whose prices >= 3000

cars = [
    {
        "brand": "Chevrolet",
        "model": "2016 Chevrolet Impala 2LT",
        "year": 2016,
        "mileage": "119862",
        "price": "$2500"
    },
    {
        "brand": "Chevrolet",
        "model": "2006 Honda CR-V EX",
        "year": 2006,
        "mileage": "117861",
        "price": "$9500"
    },
    {
        "brand": "Nissan",
        "model": "2013 Nissan Sentra FE+ SV",
        "year": 2013,
        "mileage": "62092",
        "price": "$3000"
    },
    {
        "brand": "Nissan",
        "model": "2011 Nissan Sentra 2.0 SR",
        "year": 2011,
        "mileage": "77868",
        "price": "$7999"
    },
    {
        "brand": "Jaguar",
        "model": "2000 Jaguar S-Type 4.0",
        "year": 2000,
        "mileage": "57010",
        "price": "$2995"
    }
]


def exercise_1(cars):

    filtered_cars = []

    for car in cars:

        if int(car["price"].replace("$", "")) >= 3000:

            filtered_cars.append(car)
            # print(filtered_cars)

    return filtered_cars


assert exercise_1(cars) == [
    {
        "brand": "Chevrolet",
        "model": "2006 Honda CR-V EX",
        "year": 2006,
        "mileage": "117861",
        "price": "$9500"
    },
    {
        "brand": "Nissan",
        "model": "2013 Nissan Sentra FE+ SV",
        "year": 2013,
        "mileage": "62092",
        "price": "$3000"
    },
    {
        "brand": "Nissan",
        "model": "2011 Nissan Sentra 2.0 SR",
        "year": 2011,
        "mileage": "77868",
        "price": "$7999"
    }
]