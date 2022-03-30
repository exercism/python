# Tests

We use [pytest][pytest: Getting Started Guide] as our website test runner.
You will need to install `pytest` on your development machine if you want to download and run exercise tests for the Python track locally.
You should also install the following `pytest` plugins:

- [pytest-cache][pytest-cache]
- [pytest-subtests][pytest-subtests]

We also recommend using the code linting program [pylint][pylint], as it is part of our automated feedback on the website and can be a very useful static code analysis tool.
For ease-of-use, the [pytest-pylint][pytest-pylint] plugin for `pytest` will allow you to run `pylint` via `pytest` on the command line.

Pylint configuration can be a bit much, so this [tutorial][tutorial from pycqa.org]  from pycqa.org can be helpful for getting started, as can this overview of [Code Quality: Tools and Best Practices][Code Quality: Tools and Best Practices] from Real Python.


## Installing pytest

Pytest can be installed and updated using the built-in Python utility [`pip`][pip].

For additional tips, Brett Cannon has a nice [quick-and-dirty guide on how to install packages for python][brett cannon: quick-and-dirty], along with a great explanation on [why you should use `python -m pip`][brett cannon: python-m-pip].
For more on Python's command line arguments, see [command line and environment][python command line arguments] in the Python documentation.

**Note:** `Python3` may or may not be an alias for Python on your system.
Please adjust the install commands below accordingly.
To install `pytest` in a virtual environment, ensure the environment **is activated** prior to executing commands.
Otherwise, the pytest installation will be global.


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


To check if installation was successful:

```bash
$ python3 -m pytest --version
pytest 6.2.5
```

## Running the tests

To run the tests, go to the folder where the exercise is stored using `cd` in your terminal (_replace `{exercise-folder-location}` below with your path_).

```bash
$ cd {exercise-folder-location}
```

The file you will want to run usually ends in `_test.py`.
This file contains the tests for the exercise solution, and are the same tests that run on the website when a solution is uploaded.
Next, run the following command in your terminal, replacing `{exercise_test.py}` with the location/name of the test file:

```bash
$ python3 -m pytest -o markers=task {exercise_test.py}
==================== 7 passed in 0.08s ====================
```

### Common pytest options

- `-o` : override default `ini` (_you can use this to avoid marker warnings_)
- `-v` : enable verbose output.
- `-x` : stop running tests on first failure.
- `--ff` : run failures from previous test before running other test cases.

For other options, see `python3 -m pytest -h`.


### Fixing warnings

If you do not use the `pytest -o markers=task` in the command above, is possible that you will get `warnings` about "unknown markers" when running a test that uses our _new_ syntax.

To avoid typing `pytest -o markers=task` for every test you run, you can use a `pytest.ini` configuration file, which can be downloaded from the top level of the Python track directory: [pytest.ini][pytest.ini].

You can also create your own `pytest.ini` file with the following content:

```ini
[pytest]
markers =
    task: A concept exercise task.
```

Placing this file in the _root_ or _working_ directory for the Python track exercises will register the marks and stop the warnings.
More information on pytest marks can be found in the `pytest` documentation on [marking test functions][pytest: marking test functions with attributes] and the `pytest` documentation on [working with custom markers][pytest: working with custom markers].

_More information on customizing pytest configurations can be found in the pytest documentation on [configuration file formats][pytest: configuration file formats]_


### Recommended Workflow

We recommend using the following commands to make your debugging easier and (possibly) faster:

First change your working directory to the directory of the exercise you want to test:

```bash
$(my_venv) cd path/to/exercise
```

Then, run the tests together with the previously explained arguments `-x` and`--ff`:

```bash
$(my_venv) python3 -m pytest -o markers=task -x --ff <example_file_test.py>
```

This will test your solution.
When `pytest` encounters a failed test, the program will stop and tell you which test failed.
When you make fixes and run the test again, `pytest` will first run the previous test that failed, then continue with the remaining tests.


### Using PDB, the Python Debugger, with pytest

You can use the `--pdb` argument after the `pytest` command and drop into the built-in [Python debugger][pdb], `PDB` on test failure:

```bash
$(my_venv) python3 -m pytest -o markers=task -x --ff --pdb <example_file_test.py>
=============== 4 passed in 0.15s ===============
```

Dropping into `PDB` will allow you to step through your code viewing the current scope, as well as checking the value of variables and the signature of different functions.
More details on the `PDB` module can be found in the [Python documentation on PDB][pdb].
Additionally, the [pytest docs on PDB][pytest-pdb] and [this guide from Real Python](https://realpython.com/python-debugging-pdb/) are extremely helpful.

## Extending your IDE

If you'd like to extend your IDE with some tools that will help you with testing and improving your code, the Python track [tools page][Python track tools page] on exercism.org goes over some options.

[Code Quality: Tools and Best Practices]: https://realpython.com/python-code-quality/
[Pytest: Getting Started Guide]: https://docs.pytest.org/en/latest/getting-started.html
[Python track tools page]: https://exercism.org/docs/tracks/python/tools
[brett cannon: python-m-pip]: https://snarky.ca/why-you-should-use-python-m-pip/
[brett cannon: quick-and-dirty]: https://snarky.ca/a-quick-and-dirty-guide-on-how-to-install-packages-for-python/
[pdb]: https://docs.python.org/3.9/library/pdb.html
[pip]: https://pip.pypa.io/en/stable/getting-started/
[pylint]: https://pylint.pycqa.org/en/latest/user_guide/
[pytest-cache]:http://pythonhosted.org/pytest-cache/
[pytest-pdb]: https://docs.pytest.org/en/6.2.x/usage.html#dropping-to-pdb-python-debugger-on-failures
[pytest-pylint]:https://github.com/carsongee/pytest-pylint
[pytest-subtests]:https://github.com/pytest-dev/pytest-subtests
[pytest.ini]: https://github.com/exercism/python/blob/main/pytest.ini
[pytest: configuration file formats]: https://docs.pytest.org/en/6.2.x/customize.html#configuration-file-formats
[pytest: marking test functions with attributes]: https://docs.pytest.org/en/6.2.x/mark.html#raising-errors-on-unknown-marks
[pytest: working with custom markers]: https://docs.pytest.org/en/6.2.x/example/markers.html#working-with-custom-markers
[python command line arguments]: https://docs.python.org/3/using/cmdline.html
[tutorial from pycqa.org]: https://pylint.pycqa.org/en/latest/tutorial.html
