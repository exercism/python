import timeit
import pandas as pd
import numpy as np


n_values = (12, 30, 100, 300, 1_000, 3_000, 10_000, 30_000, 100_000)
col_headers = [str(n) for n in n_values]
row_headers = ["cubic", "quad_loose", "quad_tight", "linear_loop", "linear_comp"]

# empty dataframe will be filled in one cell at a time later
df = pd.DataFrame(np.nan, index=row_headers, columns=col_headers)

# create a dictionary with all the solution codes

code = {
    'cubic': """
def triplets_with_sum(number):
    triplets = []
    for a in range(1, number + 1):
        for b in range(a + 1, number + 1):
            for c in range(b + 1, number + 1):
                if a**2 + b**2 == c**2 and a + b + c == number:
                    triplets.append([a, b, c])
    return triplets
""",

    'quad_loose': """
def triplets_with_sum(number):
    triplets = []
    for a in range(1, number + 1):
        for b in range(a + 1, number + 1):
            c = number - a - b
            if a ** 2 + b ** 2 == c ** 2:
                triplets.append([a, b, c])
    return triplets
""",

    'quad_tight': """
def triplets_with_sum(number):
    result = []
    for c in range(5, number - 1):
        c_sq = c * c
        for a in range(3, (number - c + 1) // 2):
            b = number - a - c
            if a < b < c and a * a + b * b == c_sq:
                result.append([a, b, c])
    return result
""",

    'linear_loop': """
from math import sqrt

def triplets_with_sum(number):
    N = float(number)
    triplets = []
    for c in range(int(N / 2) - 1, int((sqrt(2) - 1) * N), -1):
        D = sqrt(c ** 2 - N ** 2 + 2 * N * c)
        if D == int(D):
            triplets.append([int((N - c - D) / 2), int((N - c + D) / 2), c])
    return triplets
""",

    'linear_comp': """
def triplets_with_sum(number):
    def calculate_medium(small):
        return (number ** 2 - 2 * number * small) / (2 * (number - small))

    two_sides = ((int(medium), small) for small in range(3, number // 3)
                 if small < (medium := calculate_medium(small))
                 and medium.is_integer())

    return [[small, medium, (medium ** 2 + small ** 2) ** 0.5]
            for medium, small in two_sides]
"""
}

# Workaround for needing to do fewer runs with slow code

run_params = {
    'cubic': (5, n_values[:5]),
    'quad_loose': (0, n_values[:-1]),
    'quad_tight': (0, n_values[:-1]),
    'linear_loop': (1000, n_values),
    'linear_comp': (1000, n_values)
}

# Run the timing tests - SLOW!

for descriptor in row_headers:
    loops = run_params[descriptor][0]
    for n in run_params[descriptor][1]:
        # ugly hack for the quadratic runs
        if descriptor.startswith('quad'):
            loops = 10 if n <= 10_000 else 3

        # including a string comprehension in the timed part of the run would
        # normally be a bad idea.
        # For the slow runs, the overhead is insignificant in this exercise.
        function_call = f"triplets_with_sum({n})"
        val = timeit.timeit(function_call, code[descriptor], number=loops) / loops

        print(f"{descriptor}, n = {n:6n}: {val:.2e}")
        df.loc[descriptor, str(n)] = val

# Save the data to avoid constantly regenerating it

df.to_feather('run_times.feather')
print("\nDataframe saved to './run_times.feather'")

# The next bit will be useful for `introduction.md`
pd.options.display.float_format = '{:,.2e}'.format
print('\nDataframe in Markdown format:\n')
print(df.to_markdown(floatfmt=".1e"))


# To plot and fit the slopes, the df needs to be log10-transformed and transposed

pd.options.display.float_format = '{:,.2g}'.format
log_n_values = np.log10(n_values)
df[df == 0.0] = np.nan
transposed = np.log10(df).T
transposed = transposed.set_axis(log_n_values, axis=0)
transposed.to_feather('transposed_logs.feather')
print("\nDataframe saved to './transposed_logs.feather'")
