from datetime import date, timedelta
from calendar import isleap
import random


def shared_birthday(birthdates):
    if not birthdates:
        return False

    if isinstance(birthdates[0], str):
        birthdays = [(birthday.month, birthday.day) for birthday in
                     [date.fromisoformat(bdate) for bdate in birthdates]]
    else:
        birthdays = [(birthday.month, birthday.day) for birthday in birthdates]

    return len(birthdays) > len(set(birthdays))

def random_birthdates(groupsize):
    return [random_birthdate() for _ in range(1, groupsize + 1)]

def random_birthdate():
    rand_year = random.randrange(1900, date.today().year)
    no_leaps = rand_year - 1 if isleap(rand_year) else rand_year
    return date(no_leaps, 1, 1) + timedelta(days=random.randrange(0, 365))

def estimated_probability_of_shared_birthday(groupsize):
    reps = 100
    are_shared = [shared_birthday(random_birthdates(groupsize)) for _ in range(1, reps)]
    return sum(are_shared) / reps
