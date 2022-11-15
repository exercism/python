def leap_year(year):
    return (not year % 400 if not year % 100 else not year % 4)
