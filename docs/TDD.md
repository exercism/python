# Test-Driven Development

Test-driven development ([TDD][TDD]) refers to a style of programming where tests are written as artifacts to drive the implementation of the program design in code.

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
The tests may be viewed by the student to gather a more detailed understanding of what a passing solution should provide.
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

## After all the tests pass

Congratulations!
All the tests have passed.
What next?
The solution could be published right away.
Or, now that the code works, if you would like to refactor it for any reason, you can modify the code and submit another iteration.
If you think the code could be better, but you don't know how, you can request mentoring for the solution.
If a mentor is available with ideas for other approaches to a solution, they may contact you to share those ideas.
You could allow comments when publishing your solution, and other students may take the opportunity to make comments or ask questions.


[refactoring]: https://www.agilealliance.org/glossary/refactoring
[TDD]: https://www.agilealliance.org/glossary/tdd
[unit tests]: https://www.agilealliance.org/glossary/unit-test
