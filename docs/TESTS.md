# Tests

TODO: Change links to constant URL, not relative.

1. [Pytest](#pytest)
   - [Installation](#installing-pytest)
     - [Virtual environments](#virtual-environments)
   - [Running the tests](#running-the-tests)
     - [Failing tests](#failures)
   - [Extra arguments](#extra-arguments)
     - [Stop test after first failure](#stop-after-first-failure-[-x])
     - [Failed Tests First](#failed-tests-first-[--ff])
     - [Recommended setup](#recommended-workflow)
     - [Python Debugger in Pytest](#python-debugger)
2. [Tools for your IDE](#extending-your-ide)
3. [Additional Information](#additional-information)
   - [Adding python scripts to path](#adding-to-path) TODO



---

## Pytest

_Official Pytest documentation can be found on the [Pytest Wiki](https://pytest.org/en/latest/) page._

Pytest let's you test your solutions using our provided tests, it is what we use to validate your solutions on the website.

### Installing Pytest

Pytest can be installed and updated using the built-in Python utility `pip`. 

#### Windows

```powershell
PS C:\Users\foobar> python3 -m pip install pytest pytest-cache pytest-subtests pytest-pylint
Successfully installed pytest-6.2.5 ...
```

#### Linux / MacOS

```bash
$ sudo python3 -m pip install pytest pytest-cache pytest-subtests pytest-pylint
Successfully installed pytest-6.2.5 ...

```

To check if the installation was succesful:

```bash
$ python3 -m pytest --version
pytest 6.2.5
```

If you do not want to precede every command with `python3 -m` please refer to [adding to PATH](#adding-to-path) at the end of this document.

#### Virtual environments

*For more information about virtual environments please refer to the [TOOLS](.\TOOLS.md) file.* 

When installing Pytest or any other module(s), make sure that you have [activated your environment](.\TOOLS.md#activating-your-environment). After which you can run:

```bash
$ pip install pytest pytest-cache pytest-subtests pytest-pylint
Successfully installed pytest-6.2.5 ...
```

### Running the tests

To run your test, go to the folder where the exercise is stored using `cd` in your terminal (_replace `{exercise-folder-location}` below with the path_). 

```bash
$ cd {exercise-folder-location}
```

The file you'll want always ends with `_test.py`, this file contains the tests for your solution, and are the same tests run on the website. Now run the following command in your terminal, replacing `{exercise_test.py}` with the location/name of the the testing file:

```bash
$ python3 -m pytest {exercise_test.py}
==================== 7 passed in 0.08s ====================
```

#### Failures

When your code returns an incorrect or unexpected value, pytest returns all the failed tests and the returned and expected values of each. Look at the following failed test file:

```bash
$ python3 -m pytest {exercise_test.py}
=================== FAILURES ====================
______________ name_of_failed_test ______________
# Test code inside of {exercise_test.py} that failed.
...
E		TypeOfError: ReturnedValue != ExpectedValue

exercise_test.py:{line_of_failed_test}: TypeOfError
============ short test summary info ============
FAILED exercise_test.py::ExerciseTest::name_of_failed_test
========== 1 failed, 2 passed in 0.13s ==========
```

### Extra arguments

If you really want to be specific about what Pytest returns on your screen, here are some handy arguments that will make Pytest return a more specific dataset.

#### Stop After First Failure [`-x`]

Running the `pytest -x {exercise_test.py}` command, will run the tests like normal, but will stop the tests when it encounters a failed test. This will help when you want to debug a single failure at a time.

```bash
$ python -m pytest -x example_test.py
=================== FAILURES ====================
_______________ example_test_foo ________________
...
...
============ short test summary info ============
FAILED example_test.py::ExampleTest::example_test_foo
!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!
========== 1 failed, 5 passed in 0.28s ==========
```

#### Failed Tests First [`--ff`]

`pytest-cache` remembers which tests failed last time you ran `pytest`, running `pytest --ff {exercise_test.py}` will run those previously failed tests first, then it will continue with the rest of the tests. This might speed up your testing if you are making a lot of smaller fixes.

```bash
$ python -m pytest --ff bob_test.py
```

#### Recommended Workflow

We recommend using the following commands to make your debugging easier and (possibly) faster:

First change your working directory to the directory of the exercise you want to test:

```bash
cd path/to/exercise
```

Then, run the tests together with the previously explained arguments `-x` and`--ff`:

```bash
pytest -x -ff bob_test.py
```

This will test your solution. When `pytest` encounters a failed test, the program will stop and tell you which test failed. When you run the test again, `pytest` will first test that failed test, then continue with the rest.

#### Python Debugger

If you want to truly debug like a pro, use the `--pdb` argument after the `pytest` command. 

```bash
$ python3 -m pytest --pdb bob_test.py
```

When a test fails it allows you to look at variables and how your code responds. If you want to learn how to really use `PDB` module, have a look at the [Python Docs](https://docs.python.org/3/library/pdb.html#module-pdb) or [this](https://realpython.com/python-debugging-pdb/) Real Python article.

## Extending your IDE

If you'd like to extend your IDE with some tools that will help you with testing/improving your code, check [this]() page. We go into multiple IDEs and editors and some useful extensions.

## Additional information

### Adding to PATH

**Note:** If you are running a [virtual environment](.\TOOLS.md) you do not need to *add to path* as it should work fine.

Preceding every module you want to run with `python3 -m` might get a little annoying. You can add the `Scripts` folder of your Python installation to your path. If you do not know where you have installed Python, run the following command in your terminal:

```bash
$ python3 -c "import os, sys; print(os.path.dirname(sys.executable))"
{python_directory}
```

The *returned* directory is where your Python version is installed, in this tutorial it is referred to as `{python_directory}`.

#### Windows

Click the `Windows Start` button and lookup *Edit the system environment variables* and press enter. Next press, `Environment Variables...`:

![Press the blue button, lol](.\img\Windows-SystemProperties.png)

Then find the `Path` variable in your *User variables*, select it, and click `Edit...`:

![Selecting the path variable](.\img\Windows-EnvironmentVariables.png)

Then add a new line, as shown in the picture, replacing `{python_directory}` with your Python installation's directory:

![Add python to path](.\img\Windows-AddPythonPath.png)

#### MacOS X

TODO

#### Linux

TODO
