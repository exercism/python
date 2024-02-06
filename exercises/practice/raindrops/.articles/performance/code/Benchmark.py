#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script for timing Raindrops Solutions.

Creates timing table and timing graphs for
multiple approaches to the Randrops problem in Python.

Created Jan 2024
@authors: bethanygarcia, @colinleach
"""

import timeit

import pandas as pd
import numpy as np


# ------------ FUNCTIONS TO TIME ------------- #

def convert_if_statements(num):
    sounds = ''

    if num % 3 == 0: sounds += 'Pling'
    if num % 5 == 0: sounds += 'Plang'
    if num % 7 == 0: sounds += 'Plong'

    return sounds if sounds else str(num)


def convert_truthy_falsy(number):
    threes = '' if number % 3 else 'Pling'  # Empty string if there is a remainder
    fives = '' if number % 5 else 'Plang'
    sevens = '' if number % 7 else 'Plong'

    return f'{threes}{fives}{sevens}' or str(number)


def convert_loop(number):
    sounds = ''
    drops = ("i", 3), ("a", 5), ("o", 7)

    for vowel, factor in drops:
        if number % factor == 0:
            sounds += f'Pl{vowel}ng'

    return sounds or str(number)


def convert_sequence_join(number):
    drops = ["Pling", "Plang", "Plong"]
    factors = [3, 5, 7]
    sounds = ''.join(drops[index] for
                     index, factor in
                     enumerate(factors) if (number % factor == 0))

    return sounds or str(number)


def convert_dict(number):

    sounds = {3: 'Pling',
              5: 'Plang',
              7: 'Plong'}

    results = ''.join(sounds[divisor] for
                      divisor in sounds.keys()
                      if number % divisor == 0)

    return results or str(number)


def convert_dict_recommended(number):

    sounds = {3: 'Pling',
              5: 'Plang',
              7: 'Plong'}

    results = ''.join(sound for
                      divisor, sound in sounds.items()
                      if number % divisor == 0)

    return results or str(number)


from itertools import compress

def convert_itertools(number):
    sounds = ('Pling', 'Plang', 'Plong')
    mask = ((number % factor) == 0 for factor in (3, 5, 7))
    return ''.join(compress(sounds, mask)) or str(number)


from functools import reduce

def convert_functools(number):
    sounds = ('Pling', 'Plang', 'Plong')
    factors = ((number % factor) == 0 for factor in (3, 5, 7))
    result = reduce(lambda sound, item: sound + (item[0] * item[1]), zip(sounds, factors), '')

    return result or str(number)


def convert_pattern_matching(number):

    match [(number % factor) == 0 for factor in (3, 5, 7)]:
        case [True, True, True]:
            return 'PlingPlangPlong'
        case [True, True, False]:
            return 'PlingPlang'
        case [False, True, True]:
            return 'PlangPlong'
        case [True, False, True]:
            return 'PlingPlong'
        case [True, False, False]:
            return 'Pling'
        case [False, False, True]:
            return 'Plong'
        case [False, True, False]:
            return 'Plang'
        case _:
            return str(number)


## ---------END FUNCTIONS TO BE TIMED-------------------- ##

## --------  Timing Code Starts Here ---------------------##


# Input Data Setup
inputs = [1,5,7,6,8,9,10,14,15,21,27, 35, 49, 52, 70, 105, 144, 182,
          189, 195, 198, 203, 204, 210, 228, 231, 252, 315, 318, 329,
          340, 349, 379, 399, 409, 415, 497, 500, 525, 625, 735, 813,
          1575, 3125, 3250]


# #Set up columns and rows for Pandas Data Frame
col_headers = [f'Number: {number}'for number in inputs]
row_headers = ["if statements",
              "ternary with truthy/falsy",
              "loop with tuple",
              "sequence with join",
              "dictionary with join",
              "dictionary recommended"
              "itertools with join",
              "functools reduce",
              "structural pattern matching"]

# # empty dataframe will be filled in one cell at a time later
df = pd.DataFrame(np.nan, index=row_headers, columns=col_headers)

# #Function List to Call When Timing
functions = [convert_if_statements,
             convert_truthy_falsy,
             convert_loop,
             convert_sequence_join,
             convert_dict,
             convert_dict_recommended,
             convert_itertools,
             convert_functools,
             convert_pattern_matching]

# Run timings using timeit.autorange().  Run Each Set 3 Times.
for function, title in zip(functions, row_headers):
    timings = [[
            timeit.Timer(lambda: function(data), globals=globals()).autorange()[1] /
            timeit.Timer(lambda: function(data), globals=globals()).autorange()[0]
            for data in inputs] for rounds in range(3)]

    # Only the fastest Cycle counts.
    timing_result = min(timings)

    # timing_result = [round(min(timeit.repeat(lambda: function(data), repeat=3, number=1000000, globals=globals())), 6) for data in words_II]
    print(f'{title}', f'Timings : {timing_result}')

    # Insert results into the dataframe
    df.loc[title, 'Number: 1':'Number: 3250'] = timing_result

# The next bit is useful for `introduction.md`
pd.options.display.float_format = '{:,.2e}'.format
print('\nDataframe in Markdown format:\n')
print(df.to_markdown(floatfmt=".2e"))

