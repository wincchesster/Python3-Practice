# Module 3: Python Data Structures

## Task 1 ( Calculate days between current date and a given date )
```python
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
print(get_days_from_today("2022-10-09"))  
```

Output:
```
476
```

## Task 2 ( Lottery game )
```
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
```

Output:
```
[3, 4, 5, 7, 8, 10]
```

## Task 3 ( Beutify phone number )
```
import re

def normalize_phone(phone_number):

    beautify_phone = re.sub(r'\D', '', phone_number.strip())
    if not beautify_phone.startswith('+'):
        if beautify_phone.startswith('380'):
            beautify_phone = '+' + beautify_phone
        else: 
            beautify_phone = '+38' + beautify_phone
    return beautify_phone

# Testing the function
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",

]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
```

Output:
```
Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```

## Task 4 ( Upcoming birthdays )
```
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_str = user["birthday"]
        birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta = (birthday_this_year - today).days

        if 0 <= delta <= 7:
            if birthday_this_year.weekday() in [5, 6]: 
                offset = 7 - birthday_this_year.weekday()
                birthday_this_year = birthday_this_year + timedelta(days=offset)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.29"},
    {"name": "Jane Smith", "birthday": "1990.02.01"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
```

Output:
```
Список привітань на цьому тижні: [{'name': 'John Doe', 'congratulation_date': '2024.01.29'}, {'name': 'Jane Smith', 'congratulation_date': '2024.02.01'}]
```