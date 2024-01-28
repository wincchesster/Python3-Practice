#!/usr/local/bin/python3

import random

def get_numbers_ticket(min, max, quantity):
    # Checking if the input is correct
    if min >= 1 and max <= 1000 and 1 <= quantity <= (max - min + 1):
        # Generating a list of random numbers
        numbers = random.sample(range(min, max + 1), quantity)
        # returning the list
        return sorted(numbers)
    else:
        return []

# Testing the function
lottery_numbers = get_numbers_ticket(1, 10, 6)
print(lottery_numbers)