#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script for timing Acronym Solutions.

Creates timing table and timing graphs for
multiple approaches to the Acronym problem in Python.

Created Feb 2024
@authors: bethanygarcia, colinleach
"""

import timeit
import re
from functools import reduce

import pandas as pd
import numpy as np


# ------------ FUNCTIONS TO TIME ------------- #
def abbreviate_list_comprehension(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    return ''.join([word[0] for word in phrase])


def abbreviate_genex(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    letters = (word[0] for word in phrase)
    return ''.join(letters)


def abbreviate_loop(to_abbreviate):
    phrase = to_abbreviate.replace('-', ' ').replace("_", " ").upper().split()
    acronym = ""

    for word in phrase:
        acronym += word[0]

    return acronym


def abbreviate_map(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()

    return ''.join(map(lambda word: word[0], phrase))


def abbreviate_reduce(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()

    return reduce(lambda start, word: start + word[0], phrase, "")


def abbreviate_regex_join(phrase):
    removed = re.findall(r"[a-zA-Z']+", phrase)
    return ''.join(word[0] for word in removed).upper()


def abbreviate_finditer_join(to_abbreviate):
    return ''.join(word[0][0] for word in
                   re.finditer(r"[a-zA-Z']+", to_abbreviate)).upper()


def abbreviate_regex_sub(to_abbreviate):
    pattern = re.compile(r"(?<!_)\B[\w']+|[ ,\-_]")
    return re.sub(pattern, "", to_abbreviate).upper()


def abbreviate_regex_findall(to_abbreviate):
    return ''.join(re.findall(r"(?<!')\b[a-zA-Z]|(?<=_)[^ _']", to_abbreviate.upper()))


## ---------END FUNCTIONS TO BE TIMED-------------------- ##

## --------  Timing Code Starts Here ---------------------##


# Input Data Setup
inputs = ['Ruby on Rails',
  "Halley's Comet",
  'First In, First Out',
  'The Road _Not_ Taken',
  'Portable Network Graphics',
  'GNU Image Manipulation Program',
  'Something - I made up from thin air',
  'Complementary metal-oxide semiconductor',
  'Ruby on Rails Ruby on Rails Ruby on Rails ',
  "Halley's Comet Halley's Comet Halley's Comet ",
  'First In, First Out First In, First Out First In, First Out ',
  'The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken ',
  'Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me',
  'Portable Network Graphics Portable Network Graphics Portable Network Graphics ',
  'GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program ',
  'Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air ',
  'Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor ',
  'Ruby on Rails Ruby on Rails Ruby on Rails Ruby on Rails Ruby on Rails Ruby on Rails Ruby on Rails Ruby on Rails Ruby on Rails Ruby on Rails ',
  "Halley's Comet Halley's Comet Halley's Comet Halley's Comet Halley's Comet Halley's Comet Halley's Comet Halley's Comet Halley's Comet Halley's Comet ",
  'First In, First Out First In, First Out First In, First Out First In, First Out First In, First Out First In, First Out First In, First Out First In, First Out First In, First Out First In, First Out ',
  'The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken The Road _Not_ Taken ',
  'Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me ',
  'Portable Network Graphics Portable Network Graphics Portable Network Graphics Portable Network Graphics Portable Network Graphics Portable Network Graphics Portable Network Graphics Portable Network Graphics Portable Network Graphics Portable Network Graphics ',
  'GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program GNU Image Manipulation Program ',
  'Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air ',
  'Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor Complementary metal-oxide semiconductor ',
  'The Road _Not_ Taken Graphics Portable Network Graphics GNU Image Manipulation Program GNU Image Manipulation Program Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Something - I made up from thin air Complementary metal-oxide semiconductor Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me'
  "Ruby on Rails Halley's Comet First In, First Out The Road _Not_ Taken Portable Network Graphics GNU Image Manipulation Program Something - I made up from thin air Complementary metal-oxide semiconductor Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Ruby on Rails Halley's Coment First In, First Out The Road _Not_ Taken Portable Network Graphics GNU Image Manipulation Program Something - I made up from thin air Complementary metal-oxide semiconductor Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"   
  'Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me '
  "Ruby on Rails Halley's Comet First In, First Out The Road _Not_ Taken Portable Network Graphics GNU Image Manipulation Program Something - I made up from thin air Complementary metal-oxide semiconductor Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Ruby on Rails Halley's Coment First In, First Out The Road _Not_ Taken Portable Network Graphics GNU Image Manipulation Program Something - I made up from thin air Complementary metal-oxide semiconductor Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Ruby on Rails Halley's Coment First In, First Out The Road _Not_ Taken Portable Network Graphics GNU Image Manipulation Program Something - I made up from thin air Complementary metal-oxide semiconductor Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me Ruby on Rails Halley's Coment First In, First Out The Road _Not_ Taken Portable Network Graphics GNU Image Manipulation Program Something - I made up from thin air Complementary metal-oxide semiconductor Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
]


# #Set up columns and rows for Pandas Data Frame
col_headers = [f'Length: {len(item)}'for item in inputs]
row_headers = ["loop with str.replace",
               "list_comprehension with str.join()",
               "map() with str.replace()",
               "functools.reduce() with str.replace()",
               "generator expression with str.join()",
               "regex to clean with str.join()",
               "re.finditer() with str.join()",
               "re.sub() to clean and join",
               "re.findall() 1st letters w/ str.join()"]

# # empty dataframe will be filled in one cell at a time later
df = pd.DataFrame(np.nan, index=row_headers, columns=col_headers)

# #Function List to Call When Timing
functions = [abbreviate_loop,
             abbreviate_list_comprehension,
             abbreviate_map,
             abbreviate_reduce,
             abbreviate_genex,
             abbreviate_regex_join,
             abbreviate_finditer_join,
             abbreviate_regex_sub,
             abbreviate_regex_findall]

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
    df.loc[title, 'Length: 13':'Length: 1114'] = timing_result

# The next bit is useful for `introduction.md`
pd.options.display.float_format = '{:,.2e}'.format
print('\nDataframe in Markdown format:\n')
print(df.to_markdown(floatfmt=".2e"))