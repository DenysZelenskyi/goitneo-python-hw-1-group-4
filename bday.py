from datetime import datetime, timedelta
from collections import defaultdict
import calendar

def get_day_of_week_name(day_number):
    return calendar.day_name[day_number]

def get_birthdays_per_week(users):
    # Словник з іменем і днем
    birthday_dict = defaultdict(list)
    # Поточна дата
    today = datetime.today().date()

    # Перебір users
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Пройшов ДР в цьому році?
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з поточною датою
        delta_days = (birthday_this_year - today).days

        # Визначення дня тижня
        if delta_days < 7:
            birthday_date = today + timedelta(days=delta_days)
            day_of_week = birthday_date.weekday()

            # Якщо вихідний то переносимо на понеділок = 0
            if day_of_week >= 5:
                day_of_week = 0  

            birthday_weekday_name = get_day_of_week_name(day_of_week)
            birthday_dict[birthday_weekday_name].append(name)

    return birthday_dict


users = [
    {"name": "John Doe", "birthday": datetime(1980, 7, 15)},
    {"name": "Jane Smith", "birthday": datetime(1992, 4, 5)},
    {"name": "Alex Johnson", "birthday": datetime(1978, 9, 20)},
    {"name": "Emily Brown", "birthday": datetime(1989, 12, 13)},
    {"name": "Michael White", "birthday": datetime(1965, 2, 10)},
    {"name": "Samantha Taylor", "birthday": datetime(1973, 8, 22)},
    {"name": "David Miller", "birthday": datetime(1995, 11, 18)},
    {"name": "Olivia Davis", "birthday": datetime(1987, 6, 7)},
    {"name": "Daniel Wilson", "birthday": datetime(1979, 3, 25)},
    {"name": "Ella Thomas", "birthday": datetime(1990, 10, 12)},
]

result = get_birthdays_per_week(users)


for day, names in result.items():
    print(f"{day}: {', '.join(names)}")
