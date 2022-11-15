import timeit

loops = 1_000_000

val = timeit.timeit("""leap_year(1900)""",
                    """
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

""", number=loops) / loops

print(f"if statements 1900: {val}")

val = timeit.timeit("""leap_year(2000)""",
                    """
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

""", number=loops) / loops

print(f"if statements 2000: {val}")


val = timeit.timeit("""leap_year(2019)""",
                    """
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

""", number=loops) / loops

print(f"if statements 2019: {val}")

val = timeit.timeit("""leap_year(2020)""",
                    """
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

""", number=loops) / loops

print(f"if statements 2020: {val}")

val = timeit.timeit("""leap_year(1900)""",
                    """
def leap_year(year):
    return not year % 400 if not year % 100 else not year % 4

""", number=loops) / loops

print(f"ternary 1900:       {val}")

val = timeit.timeit("""leap_year(2000)""",
                    """
def leap_year(year):
    return not year % 400 if not year % 100 else not year % 4

""", number=loops) / loops

print(f"ternary 2000:       {val}")

val = timeit.timeit("""leap_year(2019)""",
                    """
def leap_year(year):
    return not year % 400 if not year % 100 else not year % 4

""", number=loops) / loops

print(f"ternary 2019:       {val}")

val = timeit.timeit("""leap_year(2020)""",
                    """
def leap_year(year):
    return not year % 400 if not year % 100 else not year % 4

""", number=loops) / loops

print(f"ternary 2020:       {val}")

val = timeit.timeit("""leap_year(2019)""",
                    """
import datetime

def leap_year(year):
    return (datetime.datetime(year, 2, 28) + 
    datetime.timedelta(days=1)).day == 29

""", number=loops) / loops

print(f"datetime add 2019:  {val}")
