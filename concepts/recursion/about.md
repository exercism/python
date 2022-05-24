# About

Recursion is a way to repeatedly execute code inside a function through the function calling itself.
Functions that call themselves are know as _recursive_ functions.
Recursion can be viewed as another way to loop/iterate. 
And like looping, a Boolean expression or `True/False` test is used to know when to stop the recursive execution.
_Unlike_ looping, recursion without termination in Python cannot not run infinitely.
Values used in each function call are placed in their own frame on the Python interpreter stack.
If the total amount of function calls takes up more space than the stack has room for, it will result in an error.

## Looping vs Recursive Implementation

Looping and recursion may _feel_ similar in that they are both iterative.
However, they both _look_ differently, both at the code level and at the implementation level.
Looping can take place within the same frame on the call stack.
It usually manages this by updating one or more variables to maintain state as it iterates.
This is an efficient implementation, but it can be somewhat cluttered at the code level.
Recursion, instead of updating state variables, can pass updated values as arguments to the next call of the same function.
This declutters the body of the function, but it is a less effficient implementation, as each call to the same function adds another frame to the stack.

## Recursion: Why and Why Not?

If there is risk of causing a stack error or overflow, why would anyone use a recursive strategy to solve a problem?
There may be situations where a solution is more readable and/or easier to reason through when expressed through recursion than when expressed through looping.
There may also be program constraints with using/mutating data, managing complexity, delegating responsibility, or organizing workloads.
Problems that lend themselves to recursion include complex but repetitive problems that grow smaller over time, particularly [divide and conquer][divide and conquer] algorithms and [cumulative][cumulative] algorithms.
However, due to Python's limit for how many frames are allowed on the stack, not all problems will benefit from a fully recursive strategy.
Problems less naturally suited to recursion include ones that have a steady state, but need to repeat for a certain number of cycles, problems that need to execute asynchronously, and situations calling for a great number of iterations.

## Looping vs Recursive Strategy: Indira's Insecurity

Indira has her monthly social security auto-deposited in her bank account on the **_second Wednesday_** of every month.
Indira is concerned about balancing her check book.
She is afraid she will write checks before her money is deposited.
She asks her granddaughter Adya to give her a list of dates her money will appear in her account.

Adya, who is just learning how to program in Python, writes a program based on her first thoughts.
She wants to return a `list` of the deposit dates so they can be printed.
She wants to write a function that will work for _any year_.
In case the schedule changes (_or in case other relatives want Adya to calculate their deposit schedules_),  she decides the function needs to take an additional parameter for the _weekday_.
Finally, Adya decides that the function needs a parameter for _which weekday_ of the month it is: the first, second, etc.
For all these requirements, she decides to use the `date` class imported from `datetime`.
Putting all of that together, Adya comes up with:

```
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

This  first iteration works, but Adya wonders if she can refactor the code to use fewer lines with less nested looping.
She's also read that it is good to minimize mutating state, so she'd like to see if she can avoid mutating some of her variables such as `output`, `month`, and `day_num` .  

She's read about recursion, and thinks about how she might change her program to use a recursive approach.
The variables that are created and mutated in her looping function could  be passed in as arguments instead.
Rather than  mutating the variables _inside_ her function, she could pass _updated values as arguments_ to the next function call.
With those intentions she arrives at this recursive approach:

```
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

Adya is happy that there are no more nested loops, no mutated state, and 2 fewer lines of code!  

She is a little concerned that the recursive approach uses more steps than the looping approach, and so is less "performant".
But re-writing the problem using recursion has definitely helped her deal with ugly nested looping (_a performance hazard_), extensive state mutation, and confusion around complex conditional logic.
It also feels more "readable" - she is sure that when she comes back to this code after a break, she will be able to read through and remember what it does more easily. 

In the future, Adya may try to work through problems recursively first.
She may find it easier to initially walk through the problem in clear steps when nesting, mutation, and complexity are minimized.
After working out the basic logic, she can then focus on optimizing her initial recursive steps into a more performant looping approach.

Even later, when she learns about `tuples`, Adya could consider further "optimizing" approaches, such as using a `list comprehension` with `Calendar.itermonthdates`, or memoizing certain values.

## Recursive Variation: The Tail Call

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

You may find a tail call even easier to reason through than a recursive call that is not a tail call.
However, it is always important when using recursion to know that there will not be so many iterations that the stack will overflow.

## Recursion Limits in Python

Some languages are able to optimize tail calls so that each recursive call reuses the stack frame of the first call to the function, instead of adding another stack frame.
Python is not one of those languages.
To guard against stack overflow, Python has a recursion limit that defaults to one thousand frames.
A [RecursionError](https://docs.python.org/3.8/library/exceptions.html#RecursionError) exception is raised when the interpreter detects that the recursion limit has been exceeded.
It is possible to use the [sys.setrecursionlimit](https://docs.python.org/3.8/library/sys.html#sys.setrecursionlimit) method to increase the recursion limit, but doing so runs the risk of having a runtime segmentation fault that will crash the program, and possibly the operating system.

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
[divide and conquer]: https://afteracademy.com/blog/divide-and-conquer-approach-in-programming
[cumulative]: https://www.geeksforgeeks.org/sum-of-natural-numbers-using-recursion/
