import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


# These dataframes are slow to create, so they should be saved in Feather format

try:
    df = pd.read_feather('./run_times.feather')
except FileNotFoundError:
    print("File './run_times.feather' not found!")
    print("Please run './Benchmark.py' to create it.")
    exit(1)

try:
    transposed = pd.read_feather('./transposed_logs.feather')
except FileNotFoundError:
    print("File './transposed_logs.feather' not found!")
    print("Please run './Benchmark.py' to create it.")
    exit(1)

# Ready to start creating plots

mpl.rcParams['axes.labelsize'] = 18

# bar plot of actual run times
ax = df.plot.bar(figsize=(10, 7),
                 logy=True,
                 ylabel="time (s)",
                 fontsize=14,
                 width=0.8,
                 rot=0)
plt.savefig('../timeit_bar_plot.svg')

# log-log plot of times vs n, to see slopes
transposed.plot(figsize=(8, 6),
                marker='.',
                markersize=10,
                ylabel="$log_{10}(time)$ (s)",
                xlabel="$log_{10}(n)$",
                fontsize=14)
plt.savefig('../slopes.svg')
