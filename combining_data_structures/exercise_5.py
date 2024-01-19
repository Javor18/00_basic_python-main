# That's Halloween, and each kid collected candies in their bucket.
# Write a program returning a string telling which candy is the most popular
# The function should return a string including the most popular candy and the list of kids who have it.
from typing import List

# kids_candies_bucket_report = [
#     [1, 4, 5, 6, 2],  # Marty has those candies in his bag
#     [2, 4, 5],  # Leon has those candies in his bag
#     [6, 4, 2, 1],  # Anna has those candies in his bag
#     [3, 2, 1]  # Mary has those candies in his bag
# ]

kids_candies_bucket_report = {
    "Marty": [1, 4, 5, 6, 2],
    "Leon": [2, 4, 5],
    "Anna": [6, 4, 2, 1],
    "Mary": [3, 2, 1]
}


def exercise_5(report: List[List[int]]) -> str:
    # Your code here
    candies = {}
    for kid in report:
        for candy in kids_candies_bucket_report[kid]:
            if candy in candies:
                candies[candy] += 1
            else:
                candies[candy] = 1

    most_popular_candy = max(candies, key=candies.get)
    most_popular_candy_count = candies[most_popular_candy]

    kids_with_most_popular_candy = []

    for kid, candies in kids_candies_bucket_report.items():
        if most_popular_candy in candies:
            kids_with_most_popular_candy.append(kid)

    return f"Candy '{most_popular_candy}' is the most popular. " \
             f"{', '.join(kids_with_most_popular_candy)} picked it up"


assert exercise_5(kids_candies_bucket_report) == (
    "Candy '2' is the most popular. "
    "Marty, Leon, Anna, Mary picked it up"
)