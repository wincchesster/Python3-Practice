#!/usr/local/bin/python3

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today()
    upcoming_birthdays = []

    for user in users:
        birthday_str = user["birthday"]
        birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta = (birthday_this_year - today).days

        if 0 <= delta <= 7:
            if birthday_this_year.weekday() in [5, 6]:  # Субота або неділя
                offset = 7 - birthday_this_year.weekday()
                birthday_this_year = birthday_this_year + timedelta(days=offset)

        upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

        return upcoming_birthdays


# Testing the function
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)