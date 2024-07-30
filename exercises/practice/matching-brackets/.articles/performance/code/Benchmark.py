import timeit

import pandas as pd
import numpy as np
import requests


# ------------ FUNCTIONS TO TIME ------------- #

def stack_match1(input_string):
    bracket_map = {"]" : "[", "}": "{", ")":"("}
    tracking = []

    for element in input_string:
        if element in bracket_map.values():
            tracking.append(element)
        if element in bracket_map:
            if not tracking or (tracking.pop() != bracket_map[element]):
                return False
    return not tracking


def stack_match2(input_string):
    opening = {'[', '{', '('}
    closing = {']', '}', ')'}
    pairs = {('[', ']'), ('{', '}'), ('(', ')')}
    stack = list()

    for char in input_string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or (stack.pop(), char) not in pairs:
                return False
    return stack == []



def stack_match3(input_string):
    BRACKETS = {'(': ')', '[': ']', '{': '}'}
    END_BRACKETS = {')', ']', '}'}

    stack = []

    def is_valid(char):
        return stack and stack.pop() == char

    for char in input_string:
        if char in BRACKETS:
            stack.append(BRACKETS[char])
        elif char in END_BRACKETS and not is_valid(char):
            return False

    return not stack


def stack_match4(input_string):
  stack = []
  r = {')': '(', ']': '[', '}': '{'}
  for c in input_string:
    if c in '[{(':
      stack.append(c)
    if c in ']})':
      if not stack:
        return False
      if stack[-1] == r[c]:
        stack.pop()
      else:
        return False
  return not stack


from collections import deque
from typing import Deque


def stack_match5(text: str) -> bool:
    """
    Determine if the given text properly closes any opened brackets.
    """
    PUSH = {"[": "]", "{": "}", "(": ")"}
    PULL = set(PUSH.values())

    stack: Deque[str] = deque()
    for char in text:
        if char in PUSH:
            stack.append(PUSH[char])
        elif char in PULL:
            if not stack or char != stack.pop():
                return False
    return not stack


def repeated_substitution1(text):
    text = "".join(x for x in text if x in "()[]{}")
    while "()" in text or "[]" in text or "{}" in text:
        text = text.replace("()","").replace("[]", "").replace("{}","")
    return not text


def repeated_substitution2(input_string):
    symbols = "".join(c for c in input_string if c in "{}[]()")
    while (pair := next((pair for pair in ("{}", "[]", "()") if pair in symbols), False)):
        symbols = symbols.replace(pair, "")
    return not symbols


import re

def repeated_substitution3(str_: str) -> bool:
    str_ = re.sub(r'[^{}\[\]()]', '', str_)
    while str_ != (str_ := re.sub(r'{\}|\[]|\(\)', '', str_)): 
        pass
    return not bool(str_)


def repeated_substitution4(input_string):
    replaced = re.sub(r"[^\[\(\{\}\)\]]|\{\}|\(\)|\[\]", "", input_string)
    return not input_string if input_string == replaced else repeated_substitution4(replaced)

## ---------END FUNCTIONS TO BE TIMED-------------------- ##

## --------  Timing Code Starts Here ---------------------##

def get_file(url):
    resp = requests.get(url)
    return resp.text

short = "\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{x} &... x^2 \\end{array}\\right)"
mars_moons = get_file("https://raw.githubusercontent.com/colinleach/PTYS516/main/term_paper/term_paper.tex")
galaxy_cnn = get_file("https://raw.githubusercontent.com/colinleach/proj502/main/project_report/report.tex")


# Input Data Setup
inputs = [short, mars_moons, galaxy_cnn]

# Ensure the code doesn't terminate early with a mismatch
assert all([stack_match1(txt) for txt in inputs])

# #Set up columns and rows for Pandas Data Frame
col_headers = ['short', 'mars_moons', 'galaxy_cnn']
row_headers = [
    "stack_match1",
    "stack_match2",
    "stack_match3",
    "stack_match4",
    "stack_match5",
    
    "repeated_substitution1",
    "repeated_substitution2",
    "repeated_substitution3",
    "repeated_substitution4"
    ]

# Empty dataframe will be filled in one cell at a time later
df = pd.DataFrame(np.nan, index=row_headers, columns=col_headers)

# Function List to Call When Timing
functions = [stack_match1, stack_match2, stack_match3, stack_match4, stack_match5, 
             repeated_substitution1, repeated_substitution2, repeated_substitution3, repeated_substitution4]

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
    df.loc[title, col_headers[0]:col_headers[-1]] = timing_result

# Save the data to avoid constantly regenerating it
df.to_feather('run_times.feather')
print("\nDataframe saved to './run_times.feather'")

# The next bit is useful for `introduction.md`
pd.options.display.float_format = '{:,.2e}'.format
print('\nDataframe in Markdown format:\n')
print(df.to_markdown(floatfmt=".2e"))

