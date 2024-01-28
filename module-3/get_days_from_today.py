#!/usr/local/bin/python3

from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Transforming date string into date object
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # Getting today's date
        today = datetime.today().date()
        # Calculating the difference between dates
        delta = today - given_date
        # Returning the difference in days
        return delta.days
    except ValueError:
        # Returning an error message if the date format is wrong
        return "Неправильний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'."

# Testing the function
print(get_days_from_today("2021-10-09"))  
