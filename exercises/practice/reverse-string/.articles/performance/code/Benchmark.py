#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script for timing Reverse String Solutions.

Creates timing table and timing graphs for
multiple approaches to reversing a stirng in Python.

Created Jan 2024
@author: bethanygarcia
"""


import timeit

import pandas as pd
import numpy as np


# ------------ FUNCTIONS TO TIME ------------- #


def reverse_slice(text):
    return text[::-1]


def reverse_iterate_and_prepend(text):
    output = ''
    for codepoint in text:
        output = codepoint + output
    return output


def reverse_range(text):
    return "".join(text[index] for index in range(len(text) - 1, -1, -1))


def reverse_half_swap(text):
    output = list(text)
    length = len(text) // 2  # Cut the amount of iteration in half.

    for index in range(length):

        # Swap values at given indexes in output list.
        output[index], output[length - index - 1] = output[length - index - 1], output[index]
    return ''.join(output)


def reverse_list_reverse(text):
    output = list(text)
    output.reverse()

    return ''.join(output)


def reverse_reversed(text):
    return (''.join(reversed(text)))


def reverse_map(text):
    return "".join(map(lambda x: text[(-x - 1)], range(len(text))))

## ---------END FUNCTIONS TO BE TIMED-------------------- ##



## --------  Timing Code Starts Here ---------------------##
# Input Data Setup for ASCII Solutions

long = 'Sünnipäevanädalalõpupeopärastlõunaväsimatus Pneumonoultramicroscopicsilicovolcanoconiosis Aequeosalinocalcalinoceraceoaluminosocupreovitriolic'

words = [
        'Ramen',
        'Euouae',
        'racecar',
        'Strengths',
        "I'm hungry!",
        'Otorhinolaryngological',
        'Antidisestablishmentarianism',
        'Pseudopseudohypoparathyroidism',
        'Hippopotomonstrosesquippedaliophobia',
        'Sünnipäevanädalalõpupeopärastlõunaväsimatus',
        'Aequeosalinocalcalinoceraceoaluminosocupreovitriolic',
        'Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas',
        'Miinibaashkiminasiganibiitoosijiganibadagwiingweshiganibakwezhigan',
        'Rindfleisch­etikettierungs­überwachungs­aufgaben­übertragungs­gesetz',
        'Incomprehensibilities Otorhinolaryngological cyfrwngddarostyngedigaeth',
        'Antidisestablishmentarianism Spectrophotofluorometrically Antidisestablishmentarianism',
        'Sünnipäevanädalalõpupeopärastlõunaväsimatus Pneumonoultramicroscopicsilicovolcanoconiosis Aequeosalinocalcalinoceraceoaluminosocupreovitriolic',
        long * 10,
        long * 100,
        long * 1000
]

# #Set up columns and rows for Pandas Data Frame
col_headers = [f'Str Len: {len(string)}' for string in words]
row_headers = ['reverse slice', 'iterate & prepend', 'iterate with range', 'list swap', 'list reverse',
               'reversed builtin', 'map and join']
labels = row_headers

# # empty dataframe will be filled in one cell at a time later
df = pd.DataFrame(np.nan, index=row_headers, columns=col_headers)

# #Function List to Call When Timing
functions = [reverse_slice, reverse_iterate_and_prepend, reverse_range, reverse_half_swap, reverse_list_reverse,
             reverse_reversed, reverse_map]

# Run timings using timeit.autorange().  Run Each Set 3 Times.
for function, title in zip(functions, row_headers):
    timings = [[
            timeit.Timer(lambda: function(data), globals=globals()).autorange()[1] /
            timeit.Timer(lambda: function(data), globals=globals()).autorange()[0]
            for data in words] for rounds in range(3)]

    # Only the fastest Cycle counts.
    timing_result = min(timings)

    # timing_result = [round(min(timeit.repeat(lambda: function(data), repeat=3, number=1000000, globals=globals())), 6) for data in words_II]
    print(f'{title}', f'Timings : {timing_result}')

    # Insert results into the dataframe
    df.loc[title, 'Str Len: 5':'Str Len: 142000'] = timing_result

# The next bit is useful for `introduction.md`
pd.options.display.float_format = '{:,.2e}'.format
print('\nDataframe in Markdown format:\n')
print(df.to_markdown(floatfmt=".2e"))
