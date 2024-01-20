import pandas as pd
import numpy as np
from numpy.linalg import lstsq


# These dataframes are slow to create, so they should be saved in Feather format

try:
    transposed = pd.read_feather('./transposed_logs.feather')
except FileNotFoundError:
    print("File './transposed_logs.feather' not found!")
    print("Please run './Benchmark.py' to create it.")
    exit(1)

n_values = (12, 30, 100, 300, 1_000, 3_000, 10_000, 30_000, 100_000)
log_n_values = np.log10(n_values)
row_headers = ["cubic", "quad_loose", "quad_tight", "linear_loop", "linear_comp"]


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

