# Test-Driven Development

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
At the bottom, in the `Test Failure` section, is the specific reason why this rest failed.
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

Sometimes, the expected datat and returned data are too large to all be placed in the `Test Failure` section.
It may look something like this:

```
AssertionError: '("Sc[67 chars]\')\n\n(\'Brass Spyglass\', \'Abandoned Lighth[952 chars]')\n' != '("Sc[67 chars]\')\n(\'Brass Spyglass\', \'Abandoned Lighthou[928 chars]')\n'
Diff is 970 characters long. Set self.maxDiff to None to see it.
```

There may still be enough data to see what the problem is.
In the case above, there are two line feeds returned (e.g. `\n\n(\'Brass Spyglass`) when only one is expected (e.g. `\n(\'Brass Spyglass`).
