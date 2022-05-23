# About

Recursion is a way to repeatedly execute code inside a function through the function calling itself.
Functions that call themselves are know as _recursive_ functions.
Recursion can be viewed as another way to loop/iterate. 
And like looping, a Boolean expression or `True/False` test is used to know when to stop the recursive execution.
_Unlike_ looping, recursion without termination in Python cannot not run infinitely.
Values used in each function call are placed in their own frame on the Python interpreter stack.
If the total amount of function calls takes up more space than the stack has room for, it will result in an error.
There may be some situations that are more readable and/or easier to reason through when expressed through recursion than when expressed through looping.

## Tail Call

A tail call is when the last statement of a function only calls itself and nothing more.
This example is not a tail call, as the function adds 1 to the result of calling itself

```python
def print_increment(step, max_value):
    if step > max_value:
        return 1
    print(f'The step is {step}')
    return 1 + print_increment(step + 1, max_value)


def main():
    retval = print_increment(1, 2)
    print(f'retval is {retval} after recursion')

if __name__ == "__main__":
    main()

```

This will print

```
The step is 1
The step is 2
retval is 3 after recursion
```

To refactor it to a tail call, make `j` a parameter of `printIncrement`

```python
def print_increment(step, max_value, retval):
    if step > max_value:
        return retval
    print(f'The step is {step}')
    return print_increment(step + 1, max_value, retval + 1)


def main():
    retval = print_increment(1, 2, 1)
    print(f'retval is {retval} after recursion')

if __name__ == "__main__":
    main()

```

You may find that a tail call may be easier to reason through than a recursive call that is not a tail call.
However, it is always important when using recursion to know that there will not be so many iterations that the stack will overflow.

## Recursion Limit

Some languages are able to optimize tail calls so that each recursive call reuses the stack frame of the first call to the function, instead of adding another stack frame.
Python is not one of those languages.
To guard against stack overflow, Python has a recursion limit, which by default is set to one thousand.
Python will raise a [RecursionError][RecursionError] exception when the interpretor detects that the recursion limit has been exceeded.
It is possible to use the [sys.setrecursionlimit][setrecursionlimit] method to increase the recursion limit, but doing so runs the risk of having a runtime segmentation fault that will crash the program.


## Why Recursion? (Indira's Insecurity)

Indira has her monthly social security auto-deposited in her bank account on the second Wednesday of every month.
Indira is concerned about balancing her check book.
She is afraid she will write checks before her money is deposited.
She asks her granddaughter Adya to give her a list of dates her money will appear in her account.
Adya, who is just learning how to program in Python, writes a program based on her first thoughts.
She wants to return a list of the dates so it can be printed.
She decides to use the `date` class imported from `datetime`.
She wants to write a function that will work for any year.
In case the schedule changes, or in case other relatives want Adya to calculate the schedule for their deposits, she decides the function needs a parameter for the weekday. 
Finally, Adya decides that the function needs a parameter for which weekday of the month it is: the first, second, etc.
Putting all of that together, Adya comes up with this.

```python
from datetime import date


def paydates_for_year(year, weekday, ordinal):
    """Returns a list of the matching weekday dates.
    
    Keyword arguments:
    year    -- the year, e.g. 2022
    weekday -- the weekday, e.g. 3 (for Wednesday)
    ordinal -- which weekday of the month, e.g. 2 (for the second)
    """
    output = []

    for month in range(1, 13):
        for day_num in range(1, 8):
            if date(year, month, day_num).isoweekday() == weekday:
                output.append(date(year, month, day_num + (ordinal - 1) * 7))
                break
    return output

# find the second Wednesday of the month for all the months in 2022
print(paydates_for_year(2022, 3, 2))

```

The program works, but Adya wonders if she can refactor the code to use fewer lines with less nested looping.
She would also like to use less mutating of variables, such as `output`, `month`, and `day_num`, because she's read that it is good to minimize mutating state.
She's heard about recursion and thinks about how to change her program to use a recursive approach.
The variables that are created and mutated in her looping function will now be passed in as arguments.
Instead of mutating the variables inside her function, she will pass updated values as arguments to the next call of her function.
With those intentions she arrives at this recursive approach

```python
from datetime import date



def paydates_for_year_rec(year, weekday, ordinal, month, day_num, output):
    """Returns a list of the matching weekday dates
    
    Keyword arguments:
    year    -- the year, e.g. 2022
    weekday -- the weekday, e.g. 3 (for Wednesday)
    ordinal -- which weekday of the month, e.g. 2 (for the second)
    month   -- the month currently being processed
    day_num -- the day of the month currently being processed
    output  -- the list to be returned
    """
    if month == 13:
        return output
    if date(year, month, day_num).isoweekday() == weekday:
        return paydates_for_year_rec(year, weekday, ordinal, month + 1, 1, output
                                     + [date(year, month, day_num + (ordinal - 1) * 7)])
    return paydates_for_year_rec(year, weekday, ordinal, month, day_num + 1, output)

    # find the second Wednesday of the month for all the months in 2022
    print(paydates_for_year_rec(2022, 3, 2, 1, 1, []))
    
```

Adya is happy that there are no more nested loops, no mutated state, and 2 fewer lines of code than her looping solution.
Later, when she learns about tuples,  Adya may consider other approaches, such as using a list comprehension with `Calendar.itermonthdates`.
She may also become concerned that the recursive approach uses more steps than the looping approach, and so is less performant.
But, when faced with a solution that involves a lot of nested looping, extensive state mutation, and complex conditional logic, Adya may try to work it out recursively first.
She may find it easier to initially reason through the problem when nesting, mutation, and complexity are minimized.
After she's worked out the basic logic she can then work at optimizing the recursive solution into a more performant looping approach.


## Resources

To learn more about using recursion in Python you can start with 
- [python-programming: recursion][python-programming: recursion]
- [Real Python: python-recursion][Real Python: python-recursion]
- [Real Python: python-thinking-recursively][Real Python: python-thinking-recursively]

[python-programming: recursion]: https://www.programiz.com/python-programming/recursion
[Real Python: python-recursion]: https://realpython.com/python-recursion/
[Real Python: python-thinking-recursively]: https://realpython.com/python-thinking-recursively/
[RecursionError]: https://docs.python.org/3.8/library/exceptions.html#RecursionError
[setrecursionlimit]: https://docs.python.org/3.8/library/sys.html#sys.setrecursionlimit
