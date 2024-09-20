# Dig Deeper
When working with dates and datetime in Python, it's essential to use the built-in `datetime` module. 

## General Guidance
### How to represent one gigasecond (1 billion)?
In python, there are multiple ways to represent 1 billion in numerical form:  
| Method              | Value                                              |  
| ------------------- | -------------------------------------------------- |  
| Exponentiation      | 10**9                                              |  
| Power function      | pow(10, 9), math.pow(10, 9) and numpy.pow(10,9)    |  
| Scientific notation | 1e9                                                |  
| Underscore notation | 1_000_000_000                                      |  
| Literal integer     | 1000000000                                         |

### What is a `datetime` and a `timedelta` ?
A `datetime` object is a way to represent a specific point in time, including the date and time of day. It contains multiple attributes, such as `year`, `month`, `day`, `hour`, `minute`, and `second`. However, updating a `datetime` object directly is not possible. Instead, we'll explore various approaches to solve the problem of adding a gigasecond to a given `datetime`.
The key to solving this problem lies in using the `timedelta` object, which represents a time interval. We can add or subtract a `timedelta` from a `datetime` object to create a new `datetime` object with the updated values.
Here is a quick example of how to use a date and time:
```py
from datetime import datetime
datetime_2000_01_25 = datetime(year = 2000, month = 1, day = 25)
wrong_date = datetime_2000_01_25 + "2 weeks" # This won't work at all
```
Instead, we have to use another one object, `timedelta`. It will be used to accomplish the same thing as shown in the previous example. This object is a time interval, which can be used to modify a `datetime` object. We can add or subtract the `timedelta` to a given `datetime` object to create a new `datetime` object with the updated values.
```py
from datetime import timedelta, datetime
datetime_2000_01_01 = datetime(year = 2000, month = 1, day = 1)
delta = timedelta(weeks=2) 
datetime_2000_01_15 = datetime_2000_01_01 + delta
```
To create a `timedelta`, you can use positional or named arguments. 
```py
# By default, timedelta is equal to:
a = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# Is equal to:
a = timedelta(0, 0, 0, 0, 0, 0, 0)
a = timedelta()
# Which can be confusing with large functions.
# For an example "days=0" mean "days" is an optional argument, and by default it is equal to 0.
# In python functions, arguments is positionnal, that mean if you want a 10 seconds "timedelta", you can do:
ten_seconds = timedelta(0, 10) # 0 days, 10 seconds
# Or you can directly name the argument:
ten_seconds = timedelta(seconds=10)
```
### Defining variables

You have several options for defining your variables
You can define variables with a global scope (outside functions) or local functions (inside).
Note that there are no immutable `constants` in python. To symbolize a constant, we write it in uppercase with underscore to replace spaces (Screaming Snake Case). Here is a quick example:
```py
GLOBAL_CONSTANT = "global" # Global scope variable (defined outside a function), in Screaming Snake Case (constant)
def test():
    LOCAL_CONSTANT = "local" # Local scope variable (defined inside a function), only accessible inside this function
```
You can choose both, with their pros and cons.
#### Global variables
You should define a global variable when:
* you want to reduce the size of functions
```py
def test():
    str1 = "abc"
    str2 = "def"
    return str1 + str2
    
# Became

STR1 = "abc"
STR2 = "def"
def test():
    return STR1 + STR2 
```
* you need to reuse a value multiple times, like constants (for example, the 1 trillion number)
```py
def add_number(n):
    return n + 10

def add_number_2_times(n):
    return n + 20

# Became

BONUS = 10
def add_number(n):
    return n + BONUS 

def add_number_2_times(n):
    return n + BONUS * 2
```
* you don't want to execute multiple times the same function, or creating a variable (for example, creating the `timedelta` object)
```py
def is_vowel(char):
    # This array will be recreated each time this function is executed.
    vowels = ["a","e","i","o","u"]
    return char in vowels

# Became

VOWELS = ["a","e","i","o","u"]
def is_vowel(char):
    return char in VOWELS
```
#### Local variables
You should define a local variable when:
* you don't need to reuse the variable
* the variable consumes too much memory (like a big array)
## Approach
### Approach: global variable with scientific notation
```py
from datetime import timedelta, datetime
ONE_BILLION = 1e9
GIGASECOND = timedelta(seconds=ONE_BILLION )
def add(moment: datetime) -> datetime: 
    return moment + GIGASECOND 
```
### Approach: without variable with exponentiation
```py
from datetime import timedelta, datetime
def add(moment: datetime) -> datetime: 
    return moment + timedelta(seconds=10**9)
```
### Approach: global number variable with underscore notation
```py
from datetime import timedelta, datetime
ONE_BILLION = 1_000_000_000
def add(moment: datetime) -> datetime: 
    return moment + timedelta(seconds=ONE_BILLION) 
```
### Approach: local variable with pow()
```py
from datetime import timedelta, datetime
def add(moment: datetime) -> datetime: 
    ONE_BILLION = pow(10, 9)
    GIGASECOND = timedelta(seconds=ONE_BILLION )
    return moment + GIGASECOND  
```
For more information, check the official [timedelta documentation](https://docs.python.org/3/library/datetime.html#timedelta-objects)
