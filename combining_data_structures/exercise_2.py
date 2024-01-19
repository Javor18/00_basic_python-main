# Write a program to sort cars by year from the oldest to the newest

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


def exercise_2(cars):
    # Your code here, multiple options, try to find two different ways
    # filtered_cars = [sorted(cars, key=lambda car: car["year"])]

    filtered_cars = []

    cars.sort(key=lambda car: car["year"])

    for car in cars:
            filtered_cars.append(car)

    return filtered_cars

assert exercise_2(cars) == [
    {
        "brand": "Jaguar",
        "model": "2000 Jaguar S-Type 4.0",
        "year": 2000,
        "mileage": "57010",
        "price": "$2995"
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
        "model": "2011 Nissan Sentra 2.0 SR",
        "year": 2011,
        "mileage": "77868",
        "price": "$7999"
    },
    {
        "brand": "Nissan",
        "model": "2013 Nissan Sentra FE+ SV",
        "year": 2013,
        "mileage": "62092",
        "price": "$3000"
    },
    {
        "brand": "Chevrolet",
        "model": "2016 Chevrolet Impala 2LT",
        "year": 2016,
        "mileage": "119862",
        "price": "$2500"
    }
]