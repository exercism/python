import timeit
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


loops = 1_000_000

row_headers = ["if-statements", "ternary", "datetime-add", "calendar-isleap"]
col_headers = ["1900", "2000", "2019", "2020"]

# empty dataframe will be filled in one cell at a time later
df = pd.DataFrame(np.nan, index=row_headers, columns=col_headers)

setups = {}

setups["if-statements"] = """
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
"""

setups["ternary"] = """
def leap_year(year):
    return not year % 400 if not year % 100 else not year % 4
"""

setups["datetime-add"] = """
from datetime import datetime, timedelta

def leap_year(year):
    return (datetime(year, 2, 28) + timedelta(days=1)).day == 29
"""

setups["calendar-isleap"] = """
from calendar import isleap

def leap_year(year):
    return isleap(year)
"""

for descriptor in row_headers:
    val = timeit.timeit("""leap_year(1900)""", setups[descriptor], number=loops) / loops
    year = '1900'
    print(f"{descriptor} {year}: {val}")
    df.loc[descriptor, year] = val

    val = timeit.timeit("""leap_year(2000)""", setups[descriptor], number=loops) / loops
    year = '2000'
    print(f"{descriptor} {year}: {val}")
    df.loc[descriptor, year] = val

    val = timeit.timeit("""leap_year(2019)""", setups[descriptor], number=loops) / loops
    year = '2019'
    print(f"{descriptor} {year}: {val}")
    df.loc[descriptor, year] = val

    val = timeit.timeit("""leap_year(2020)""", setups[descriptor], number=loops) / loops
    year = '2020'
    print(f"{descriptor} {year}: {val}")
    df.loc[descriptor, year] = val

mpl.rcParams['axes.labelsize'] = 18

# bar plot of actual run times
ax = df.plot.bar(figsize=(10, 7),
                 ylabel="time (s)",
                 fontsize=14,
                 width=0.8,
                 rot=0)
plt.savefig('../timeit_bar_plot.svg')


# The next bit will be useful for `introduction.md`
# pd.options.display.float_format = '{:,.2e}'.format
print('\nDataframe in Markdown format:\n')
print(df.to_markdown(floatfmt=".1e"))
