import datetime


def leap_year(year):
    return (datetime.datetime(year, 2, 28)
            + datetime.timedelta(days=1)).day == 29
