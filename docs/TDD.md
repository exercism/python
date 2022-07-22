# Test-Driven Development

Test-driven development ([TDD][TDD]) refers to a style of programming where tests are written to guide the implementation of the program design in code.

One or more tests (particularly [unit tests][unit tests]) are written before coding.
The tests are intended to cover one aspect of the program's behavior, which may be focused on a single function or method.
The writing of the tests is a way to transform the program requirements and general architecture into an implementation-specific design.
The tests are run, and they should fail, because the code hasn't been implemented.
The code is implemented and the tests are run again.
If the tests pass, then either implementing the behavior is done or perhaps more necessary tests remain to be created.
If the tests don't pass, then the code is debugged and the tests are run again.
The cycle of testing and coding is repeated until all of the necessary tests pass, at which point the implementation for that aspect of the program's behavior is done... for now.

## Refactoring

[Refactoring][refactoring] is the rewriting of code to improve its design.
It is not simply rewriting code to fix bugs.
It is sometimes called "refactoring" to modify code to get it to pass the tests.
Although modifying the code _may_ include improving the design as a way to pass the tests, simply debugging is not necessarily improving the _design_ of the code, and so is not necessarily _refactoring_.

Following is an example of debugging without refactoring:

```python
# A function intended to return x added to y.
# x and y are bad parameter names, but we ignore that for now.
def add(x, y):
    # used multiply operator by mistake. It fails the tests.
    return x * y

# Function corrected. It passes the tests. It has been debugged, but not refactored.
def add(x, y):
    return x + y
```


Following is an example of refactoring, and then debugging:

```python

# Function name and parameter names are modified to something more meaningful. This is refactoring.
def lot_inventory(old_cars, new_cars):
    # Introduced multiply operator by mistake. It fails the tests. This is why we test.
    return old_cars * new_cars

# Function corrected. It passes the tests. This is debugging.
def lot_inventory(old_cars, new_cars):
    return old_cars + new_cars

```

## TDD and Python on Exercism

Exercism's Python track utilizes TDD methodology in its exercises.
Unit tests are already written.
The tests may be viewed by the student to gather a more detailed understanding of what is required for a solution to pass.
A solution stub may be provided to the student.

## Troubleshooting a Failed Test on Exercism in the Web Editor

When one or more tests fail for a Python solution, the corresponding task(s) will not have a green background.
The first failing task area will be expanded and its header will look something like

```
Task 1 Extract coordinates -
```

Clicking on the minus sign will collapse the task, so we can look at other tasks, but for now we will stick with this task.

Underneath will be an expanded Test area that will look something like

```
       Test 1                               ⌄
FAILED TisburyTreasure > get coordinate
```

where `Tisbury Treasure` indicates the exercise, and `get_coordinate` indicates the failing function or method.

`Test 1` is usually going to be a kind of template with a code section for setting up the tests.
It does not have information on the specific test(s) that failed.
It will say toward the bottom that

```
One or more variations of this test failed. Details can be found under each [variant#].
```

Clicking the `⌄` will collapse the test.

Beneath will be a collapsed test that looks something like:

```
       Test 2                                                    >
FAILED TisburyTreasure > get coordinate [variation #1] (item=
       ("Scrimshaw Whale's Tooth", '2A'), result='2A')

```

How it looks will vary depending on the width set for the right-hand pane.
Clicking the `>` will expand the test.
Input data and expected result data will likely be shown in a code section.
The data may be for all of the tests for this task.
At the bottom, in the `Test Failure` section, is the specific reason why this test failed.
It may look something like this:

```
AssertionError: ['2A'] != '2A'
```

In this particular case, it indicates that the returned value of `['2A']` did not equal the expected value of `'2A'`.

If we look at the code for `get_coordinate` we see it is implemented like so

```python
def get_coordinate(record):
    return [record[1]]
```

If we remove the list brackets (e.g. `return record[1]`) and run the tests again, the tests for Task 1 will pass.

If one or more tasks remain failing, then the above process is repeated with each one until all tests pass.

Sometimes, the expected data and returned data are too large to all be placed in the `Test Failure` section.
It may look something like this:

```
AssertionError: '("Sc[67 chars]\')\n\n(\'Brass Spyglass\', \'Abandoned Lighth[952 chars]')\n' != '("Sc[67 chars]\')\n(\'Brass Spyglass\', \'Abandoned Lighthou[928 chars]')\n'
Diff is 970 characters long. Set self.maxDiff to None to see it.
```

There may still be enough data to see what the problem is.
In the case above, there are two line feeds returned (e.g. `\n\n(\'Brass Spyglass`) when only one is expected (e.g. `\n(\'Brass Spyglass`).

## After All the Tests Pass

Congratulations!
All the tests have passed.
What next?
The solution could be published right away.
Or, now that the code works, if you would like to refactor it for any reason, you can modify the code and submit another iteration.
If you think the code could be better, but you don't know how, you can request mentoring for the solution.
If a mentor is available, they may contact you with ideas for other approaches to a solution.
When publishing your solution, you can allow comments and other students may take the opportunity to post comments or ask questions.

## Optimizing for Performance

Although "Premature optimization is the root of all evil" (a saying attributed to both Tony Hoare and Donald Knuth), there does come a time when, even though the solution works, it is desired to improve the solution's performance.
One of those times may be when the solution passes some tests but times out for others.
It can be helpful to know exactly how much time a piece of code is taking.
The [timeit][timeit] module can be used to time the execution of code down to very small durations.
The `timeit` function can take up to five arguments.
The `stmt` parameter defines the actual code to be run and timed.
The `stmt` code will be run for a specifed `number` of iterations.
The `setup` parameter defines the code that is run only once to prepare for running the `stmt` code.
The time for the `setup` code to run is included in the overall time.
The more iterations the `stmt` code is run, the less the `setup` time should count per iteration.
The `timer` parameter allows for passing in a different `Timer` from the default.
The default argument for the `timer` parameter is [perf_counter][perf_counter], which should suffice.
The `number` parameter defines the number of times the `stmt` code will be run.
The default argument for the `number` parameter is `1_000_000`.
The `globals` parameter specifies a namespace in which to execute the code.
The default argument for the `globals` parameter is `None`.

The following is an example of using `timeit` to see how long it takes to determine if a sentence contains all English vowels:

```python

import timeit

# run one million times
loops = 1_000_000

# first positional argument is for stmt
# second positional argument is for setup
# third (named) argument is for number
print(timeit.timeit("""has_all_vowels('Another piggy digs up the truffles.')""",
                    """

VOWELS = "AEIOU"

def has_all_vowels(sentence):
    return all(letter in sentence.casefold() for letter in VOWELS)
""", number=loops) / loops)

Running the code a million times took an average `4.965089999896008e-07` seconds per call (about `497` nanoseconds per call).

The following example is to see if taking the `casefold` call out of the list comprehension saves any time:

```python

import timeit

loops = 1_000_000

print(timeit.timeit("""has_all_vowels('Another piggy digs up the truffles.')""",
                    """

VOWELS = "AEIOU"

def has_all_vowels(sentence):
    sentence = sentence.casefold()
    return all(letter in sentence for letter in VOWELS)
""", number=loops) / loops)

Running the code a million times took an average `4.923898000270128e-07` seconds per call (about `492` nanoseconds per call.)
So, taking the `casefold` out of the list comprehension saved about `5` nanoseconds per call, or about `5` milliseconds total for a million calls.

[cProfile][cprofile] can also be used to profile code; however, it is not as granular, since it only goes down to millisecond durations.

[cprofile]: https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/
[perf_counter]: https://docs.python.org/3/library/time.html#time.perf_counter
[refactoring]: https://www.agilealliance.org/glossary/refactoring
[TDD]: https://www.agilealliance.org/glossary/tdd
[timeit]: https://docs.python.org/3/library/timeit.html
[unit tests]: https://www.agilealliance.org/glossary/unit-test
