# Find the sum of prices for cars in the list

# Filter cars whose prices >= 3000
from typing import List, Dict

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


def exercise_3(cars: List[Dict]) -> int:
    # Your code here, multiple options, try to find at least two different ways

    # --------First way--------
    # total_price = 0

    # for car in cars:
    #
    #     total_price += int(car["price"].replace("$", ""))
    #
    # print(total_price)
    # ----------------------------------------------


    # --------Second way--------
    total_price = sum([int(car["price"].replace("$", "")) for car in cars])
    # ----------------------------------------------


    return total_price


assert exercise_3(cars) == 25994
