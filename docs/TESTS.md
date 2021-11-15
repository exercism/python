# Tests

We use [pytest](http://pytest.org/en/latest/) as our website test runner.
You will need to install pytest on your development machine if you want to download and run exercise tests for the Python track locally.
We also recommend you install the following pytest plugins:

- [pytest-cache](http://pythonhosted.org/pytest-cache/)
- [pytest-subtests](https://github.com/pytest-dev/pytest-subtests)
- [pytest-pylint](https://github.com/carsongee/pytest-pylint)

The PyTest [Getting Started Guide](https://docs.pytest.org/en/latest/getting-started.html) has quick general instructions, although they do not cover installing the plugins.
Continue reading below for more detailed instructions.

We also recommend using [pylint](https://pylint.pycqa.org/en/latest/user_guide/), as it is part of our automated feedback on the website, and can be a very useful (if noisy!) code analysis tool.

Pylint can be a bit much, so this [tutorial from pycqa.orgl](https://pylint.pycqa.org/en/latest/tutorial.html) can be helpful for getting started, as can this overview of [Code Quality: Tools and Best Practices](https://realpython.com/python-code-quality/) from Real Python.

---

- [Pytest](#pytest)
  - [Installing pytest](#installing-pytest)
  - [Running the tests](#running-the-tests)
  - [Extra arguments](#extra-arguments)
- [Extending your IDE](#extending-your-ide)
- [Additional information](#additional-information)

---

## Pytest

_Official pytest documentation can be found on the [pytest Wiki](https://pytest.org/en/latest/) page._

Pytest lets you test your solutions using our provided tests, and is what we use to validate your solutions on the website.

### Installing pytest

Pytest can be installed and updated using the built-in Python utility `pip`.

#### Windows

```powershell
PS C:\Users\foobar> python3 -m pip install pytest pytest-cache pytest-subtests pytest-pylint
Successfully installed pytest-6.2.5 ...
```

#### Linux / MacOS

```bash
$ python3 -m pip install pytest pytest-cache pytest-subtests pytest-pylint
Successfully installed pytest-6.2.5 ...

```

To check if the installation was successful:

```bash
$ python3 -m pytest --version
pytest 6.2.5
```

If you do not want to precede every command with `python3 -m` please refer to [adding to PATH](#adding-to-path) at the end of this document.

#### Installing pytest within a virtual environment

_For more information about virtual environments please refer to the [tools](./tools) file._

When installing pytest or any other module(s), make sure that you have [activated your environment](./tools#activating-your-virtual-environment). After which you can run:

```bash
$ pip install pytest pytest-cache pytest-subtests pytest-pylint
Successfully installed pytest-6.2.5 ...
```

### Running the tests

To run the tests, go to the folder where the exercise is stored using `cd` in your terminal (_replace `{exercise-folder-location}` below with the path_).

```bash
$ cd {exercise-folder-location}
```

The file you'll want always ends with `_test.py`.
This file contains the tests for your solution, and are the same tests which run on the website.
Now run the following command in your terminal, replacing `{exercise_test.py}` with the location/name of the test file:

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
E   TypeOfError: ReturnedValue != ExpectedValue

exercise_test.py:{line_of_failed_test}: TypeOfError
============ short test summary info ============
FAILED exercise_test.py::ExerciseTest::name_of_failed_test
========== 1 failed, 2 passed in 0.13s ==========
```

### Extra arguments

If you really want to be specific about what pytest returns on your screen, here are some handy arguments that allows you to configure its behavior.

#### Stop After First Failure [`-x`]

Running the `pytest -x {exercise_test.py}` command, will run the tests like normal, but will stop the tests after the first failed test. This will help when you want to debug a single failure at a time.

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
==================== 7 passed in 503s ====================
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

#### Using PDB, the Python Debugger, with pytest

If you want to truly debug like a pro, use the `--pdb` argument after the `pytest` command.

```bash
$ python3 -m pytest --pdb bob_test.py
=============== 4 passed in 0.15s ===============
```

When a test fails, `PDB` allows you to look at variables and how your code responds. If you want to learn how to use the `PDB` module, have a look at the [Python Docs](https://docs.python.org/3/library/pdb.html#module-pdb) or [this](https://realpython.com/python-debugging-pdb/) Real Python article.

## Extending your IDE

If you'd like to extend your IDE with some tools that will help you with testing and improving your code, check the [tools](./tools) page. We go into multiple IDEs, editors and some useful extensions.

## Additional information

### Adding pytest to your PATH

**Note:** If you are running a [virtual environment](./tools.md) you do not need to _add to path_ as it should work fine.

Typing `python3 -m` every time you want to run a module can get a little annoying. You can add the `Scripts` folder of your Python installation to your path. If you do not know where you have installed Python, run the following command in your terminal:

```bash
$ python3 -c "import os, sys; print(os.path.dirname(sys.executable))"
{python_directory}
```

The _returned_ directory is where your Python version is installed, in this tutorial it is referred to as `{python_directory}`.

#### Windows

Click the `Windows Start` button and lookup _Edit the system environment variables_ and press enter. Next press, `Environment Variables...`:

![Press the blue button, lol](https://raw.githubusercontent.com/exercism/python/main/docs/img/Windows-SystemProperties.png)

Then find the `Path` variable in your _User variables_, select it, and click `Edit...`:

![Selecting the path variable](https://raw.githubusercontent.com/exercism/python/main/docs/img/Windows-EnvironmentVariables.png)

Then add a new line, as shown in the picture, replacing `{python_directory}` with your Python installation's directory:

![Add python to path](https://raw.githubusercontent.com/exercism/python/main/docs/img/Windows-AddPythonPath.png)

### Fixing warnings

It is possible that you will get `warnings` about "unknown markers" when running a test that uses our _new_ syntax.

To resolve this issue, we use a `pytest.ini` file, which can be downloaded from the top level of the Python track directory: [pytest.ini](https://github.com/exercism/python/blob/main/pytest.ini).

You can also create your own file with the following content:

```ini
[pytest]
markers =
    task: A concept exercise task.
```

Whenever you run your tests, make sure that this file is in your _root_ or _working_ directory for Exercism exercises.

_More information on customizing pytest can be found in the [PyTest docs](https://docs.pytest.org/en/6.2.x/customize.html#pytest-ini)_
