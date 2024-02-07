import timeit

import pandas as pd
import numpy as np


# ------------ FUNCTIONS TO TIME ------------- #

def nested_loops_1(number):
    not_prime = []
    prime = []

    for item in range(2, number + 1):
        if item not in not_prime:
            prime.append(item)
            for element in range(item * item, number + 1, item):
                not_prime.append(element)

    return prime


def nested_loops_2(limit):
    limit += 1
    l = [True for _ in range(limit)]
    for i in range(2, limit):
        if not l[i]:
            continue
        for j in range(2 * i, limit, i):
            l[j] = False
    return [i for i, v in enumerate(l) if i > 1 and v]


def set_ops_1(number):
    numbers = set(item for item in range(2, number + 1))

    not_prime = set(not_prime for item in range(2, number + 1)
                    for not_prime in range(item ** 2, number + 1, item))

    # sorting adds .2ms, but the tests won't pass with an unsorted list
    return sorted(list((numbers - not_prime)))


def set_ops_2(number):
    # fastest
    not_prime = set()
    primes = []

    for num in range(2, number + 1):
        if num not in not_prime:
            primes.append(num)
            not_prime.update(range(num * num, number + 1, num))

    return primes


def set_ops_3(limit: int) -> list[int]:
    start = set(range(2, limit + 1))
    return sorted(start - {m for n in start for m in range(2 * n, limit + 1, n)})


def generator_comprehension(number):
    # slowest
    primes = (item for item in range(2, number + 1) if item not in
              (not_prime for item in range(2, number + 1) for
               not_prime in range(item * item, number + 1, item)))
    return list(primes)


def list_comprehension(limit):
    return [x for x in range(2, limit + 1)
            if all(x % y != 0 for y in range(2, x))] if limit >= 2 else []


## ---------END FUNCTIONS TO BE TIMED-------------------- ##

## --------  Timing Code Starts Here ---------------------##


# Input Data Setup
inputs = [10, 30, 100, 300, 1_000, 3_000, 10_000, 30_000, 100_000]

# #Set up columns and rows for Pandas Data Frame
col_headers = [f'Number: {number}' for number in inputs]
row_headers = ["nested_loops_1",
               "nested_loops_2",
               "set_ops_1",
               "set_ops_2",
               "set_ops_3",
               "generator_comprehension",
               "list_comprehension"]

# Empty dataframe will be filled in one cell at a time later
df = pd.DataFrame(np.nan, index=row_headers, columns=col_headers)

# Function List to Call When Timing
functions = [nested_loops_1,
             nested_loops_2,
             set_ops_1,
             set_ops_2,
             set_ops_3,
             generator_comprehension,
             list_comprehension]

# Run timings using timeit.autorange().  Run Each Set 3 Times.
for function, title in zip(functions, row_headers):
    timings = [[
        timeit.Timer(lambda: function(data), globals=globals()).autorange()[1] /
        timeit.Timer(lambda: function(data), globals=globals()).autorange()[0]
        for data in inputs] for rounds in range(3)]

    # Only the fastest Cycle counts.
    timing_result = min(timings)

    print(f'{title}', f'Timings : {timing_result}')

    # Insert results into the dataframe
    df.loc[title, 'Number: 10':'Number: 100000'] = timing_result

# Save the data to avoid constantly regenerating it
df.to_feather('run_times.feather')
print("\nDataframe saved to './run_times.feather'")
#
# The next bit is useful for `introduction.md`
pd.options.display.float_format = '{:,.2e}'.format
print('\nDataframe in Markdown format:\n')
print(df.to_markdown(floatfmt=".2e"))
