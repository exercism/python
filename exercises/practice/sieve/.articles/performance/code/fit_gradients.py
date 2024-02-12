import pandas as pd
import numpy as np
from numpy.linalg import lstsq


# These dataframes are slow to create, so they should be saved in Feather format

try:
    df = pd.read_feather('./run_times.feather')
except FileNotFoundError:
    print("File './run_times.feather' not found!")
    print("Please run './Benchmark.py' to create it.")
    exit(1)

# To plot and fit the slopes, the df needs to be log10-transformed and transposed

inputs = [10, 30, 100, 300, 1_000, 3_000, 10_000, 30_000, 100_000]

pd.options.display.float_format = '{:,.2g}'.format
log_n_values = np.log10(inputs)
df[df == 0.0] = np.nan
transposed = np.log10(df).T
transposed = transposed.set_axis(log_n_values, axis=0)
transposed.to_feather('transposed_logs.feather')
print("\nDataframe saved to './transposed_logs.feather'")

n_values = (10, 30, 100, 300, 1_000, 3_000, 10_000, 30_000, 100_000)
log_n_values = np.log10(n_values)
row_headers = ["nested_loops_1",
               "nested_loops_2",
               "set_ops_1",
               "set_ops_2",
               "set_ops_3",
               "generator_comprehension",
               "list_comprehension"]


# Do a least-squares fit to get the slopes, working around missing values
# Apparently, it does need to be this complicated

def find_slope(name):
    log_times = transposed[name]
    missing = np.isnan(log_times)
    log_times = log_times[~missing]
    valid_entries = len(log_times)
    A = np.vstack([log_n_values[:valid_entries], np.ones(valid_entries)]).T
    m, _ = lstsq(A, log_times, rcond=None)[0]
    return m


# Print the slope results
slopes = [(name, find_slope(name)) for name in row_headers]
print('\nSlopes of log-log plots:')
for name, slope in slopes:
    print(f'{name:>14} : {slope:.2f}')

