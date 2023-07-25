# Introduction

Most of the time, code is read rather than written, and writing a big number can be a challenge to read.

## General guidance

Here are two approaches to making big numbers more readable:

## Approach: Underscores in Numeric Literals

`_` can accept as a thousands operator

**ie:** 1\*000_000 is far more readable than 1000000

For more information check [Reference](https://peps.python.org/pep-0515/#:~:text=The%20syntax%20would%20be%20the,width%20of%2010%20with%20*%20separator.).

## Approach: Exponential notation or scientific notation

The e (or E) character followed by an integer represents the power of 10 by which the number preceding the e should be multiplied.

**ie:** `1e6`, 1 is multiplied by 10 raised to the power of 6, which equals `1000000`

For more information check [Reference](https://python-reference.readthedocs.io/en/latest/docs/float/scientific.html).
