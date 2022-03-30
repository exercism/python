# Tests

We use [pytest][Getting Started Guide] as our website test runner.
You will need to install `pytest` on your development machine if you want to download and run exercise tests for the Python track locally.
You should also install the following `pytest` plugins:

- [pytest-cache][pytest-cache]
- [pytest-subtests][pytest-subtests]

We also recommend using the code linting program [pylint][pylint], as it is part of our automated feedback on the website and can be a very useful static code analysis tool.
For ease-of-use, the [pytest-pylint][pytest-pylint] plugin for `pytest` will allow you to run `pylint` via `pytest` on the command line.

Pylint configuration can be a bit much, so this [tutorial from pycqa.org][tutorial from pycqa.org] can be helpful for getting started, as can this overview of [Code Quality: Tools and Best Practices][Code Quality: Tools and Best Practices] from Real Python.


## Installing pytest

Pytest can be installed and updated using the built-in Python utility [`pip`][pip].

For additional tips, Brett Cannon has a nice [quick-and-dirty guide on how to install packages for python][quick-and-dirty], along with a great explanation on [why you should use `python -m pip`][python-m-pip].
For more on Python's command line arguments, see [command line and environment][python command line] in the Python documentation.

**Note:** `Python3` and `py` may or may not be aliases for Python on your system.
Please adjust the install commands below accordingly.
To install `pytest` in a virtual environment, ensure the environment **is activated** prior to executing commands.
Otherwise, the `pytest` installation will be global.


#### Windows

```powershell
PS C:\Users\foobar> py -m pip install pytest pytest-cache pytest-subtests pytest-pylint
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

### Fixing warnings

If you do not use the `pytest -o markers=task` in the command above, is possible that you will get `warnings` about "unknown markers" when running a test that uses our _new_ syntax.

To avoid typing `pytest -o markers=task` for every test you run, you can use a `pytest.ini` configuration file, which can be downloaded from the top level of the Python track directory: [pytest.ini][pytest.ini].

You can also create your own `pytest.ini` file with the following content:

```ini
[pytest]
markers =
    task: A concept exercise task.
```

Placing this file in the _root_ or _working_ directory for Exercism exercises will register the marks and stop the warnings.
More information on pytest marks can be found in the `pytest` documentation on [marking test functions][marking test functions with attributes] and the `pytest` documentation on [working with custom markers][working with custom markers].

_More information on customizing pytest configurations can be found in the pytest documentation on [configuration file formats][configuration file formats]_


### Test Failures

When tests fail, `pytest` prints the text of each failed test, along with the expected and actual `return` values of each to the terminal.
Below is an generic example of a failed test:

```bash
$(my_venv) python3 -m pytest -o markers=task {exercise_test.py}

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

If you really want to be specific about what pytest returns on your screen, here are some handy command-line arguments that allows you to configure its behavior.


#### Return All Details [`-v`]

Adding the `-v` (_verbose_) flag will return both environment information and a test summary in addition to test failures:

```bash
$(my_venv)  python3 -m pytest -o markers=task -v exercises/<exercise_name>/<test_file_test.py> 

======================================== test session starts ===========================================
platform darwin -- Python 3.9.0, pytest-6.2.5, -- /usr/local/envs/my_env/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.9.0', 'Platform': 'macOS-10.14.6-x86_64-i386-64bit', 'Packages': {'pytest': '6.2.1'}, 'Plugins': {'subtests': '0.5.0', 'pylint': '0.18.0'}
rootdir: /Users/<user>/exercism/python, configfile: pytest.ini
plugins: subtests-0.5.0, pylint-0.18.0

collected 5 items                                                                                                                                                                                         

exercises/exercise-name/exercise_file_test.py::ExerciseNameTest::test_one FAILED                          [ 20%]
exercises/exercise-name/exercise_file_test.py::ExerciseNameTest::test_two FAILED
exercises/exercise-name/exercise_file_test.py::ExerciseNameTest::test_three PASSED                        [ 40%]
exercises/concept/exercise-name/exercise_file_test.py::ExerciseNameTest::test_four FAILED
exercises/concept/exercise-name/exercise_file_test.py::ExerciseNameTest::test_five PASSED                 [ 60%]
exercises/concept/exercise-name/exercise_file_test.py::ExerciseNameTest::test_six FAILED
exercises/concept/exercise-name/exercise_file_test.py::ExerciseNameTest::test_seven PASSED                [ 80%]
exercises/concept/exercise-name/exercise_file_test.py::ExerciseNameTest::test_eight FAILED
exercises/concept/exercise-name/exercise_file_test.py::ExerciseNameTest::test_nine PASSED                 [100%]

================================================ FAILURES ======================================================
# Failed tests are then individually printed out below

.......
```

#### Stop After First Failure [`-x`]

Using the `-x` flag will run the tests as normal, but stop the test run upon the first test failure.
This helps when you want to debug a single task or test failure at a time:

```bash
$(my_venv) python3 -m pytest -o markers=task -x exercises/<exercise_name>/<test_file_test.py> 

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

The `pytest-cache` plugin remembers which tests failed last time you ran `pytest`, so using the flag `--ff` will tell `pytest` to run previously failed tests **first**, then continue with the remainder of the tests.
This might speed up your testing if you are making a lot of smaller fixes around one particular task or set of inputs.


```bash
$(my_venv) python3 -m pytest -o markers=task --ff <example_file_test.py>
==================== 7 passed in 503s ====================
```

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

If you want to "debug like a pro", you can use the `--pdb` argument after the `pytest` command, and drop into the built-in [Python debugger][pdb], `PDB`.

```bash
$(my_venv) python3 -m pytest -o markers=task -x --ff --pdb <example_file_test.py>
=============== 4 passed in 0.15s ===============
```

When a test fails, dropping into `PDB` will allow you to step through your code viewing the current scope, as well as checking the value of variables and the signature of different functions.
More details on the `PDB` module can be found in the [Python documentation on PDB][pdb].
Additionally, the [pytest docs on PDB][pytest-pdb] and [this guide from Real Python](https://realpython.com/python-debugging-pdb/) are extremely helpful.


## Extending your IDE

If you'd like to extend your IDE with some tools that will help you with testing and improving your code, check the [tools](./tools) page.
We explore multiple IDEs, editors and some useful extensions for linting and debugging there.


## Additional information

### Adding python to your PATH

**Note:** If you have installed Python on Windows via the [PSF Installer][psf-installer], then the command will be `py` as opposed to `python3`.

Typing `python3 -m` every time you want to run a module can get a little annoying.
To avoid this, you can add the `Scripts` folder of your Python installation to your path.
If you do not know where you have installed Python, run the following command in your terminal:

```bash
$ python3 -c "import os, sys; print(os.path.dirname(sys.executable))"
{python_directory}
```

The _returned_ directory is where your current active Python version is installed, in this section it is referred to as `{python_directory}`.

#### Windows

Click the `Windows Start` button and lookup _Edit the system environment variables_ and press enter.
Next press, `Environment Variables...`:

![Press the blue button, lol](https://raw.githubusercontent.com/exercism/python/main/docs/img/Windows-SystemProperties.png)

Then find the `Path` variable in your _User variables_, select it, and click `Edit...`:

![Selecting the path variable](https://raw.githubusercontent.com/exercism/python/main/docs/img/Windows-EnvironmentVariables.png)

Then add a new line, as shown in the picture, replacing `{python_directory}` with your Python installation's directory:

![Add python to path](https://raw.githubusercontent.com/exercism/python/main/docs/img/Windows-AddPythonPath.png)


#### MacOS/Linux

The below should work for most Linux and MacOS flavors with a `bash` shell.
Commands may vary by Linux distro, and whether a `fish` or `zsh` shell is used.
Replace `{python_directory}` with the output of `python3 -c "import os, sys; print(os.path.dirname(sys.executable))"`

```bash
export PATH=”$PATH:{python_directory}}”
```

[pip]: https://pip.pypa.io/en/stable/getting-started/
[python command line]: https://docs.python.org/3/using/cmdline.html
[pytest-cache]:http://pythonhosted.org/pytest-cache/
[pytest-subtests]:https://github.com/pytest-dev/pytest-subtests
[pytest-pylint]:https://github.com/carsongee/pytest-pylint
[quick-and-dirty]: https://snarky.ca/a-quick-and-dirty-guide-on-how-to-install-packages-for-python/
[Getting Started Guide]: https://docs.pytest.org/en/latest/getting-started.html
[pytest.ini]: https://github.com/exercism/python/blob/main/pytest.ini
[python-m-pip]: https://snarky.ca/why-you-should-use-python-m-pip/
[tutorial from pycqa.org]: https://pylint.pycqa.org/en/latest/tutorial.html
[Code Quality: Tools and Best Practices]: https://realpython.com/python-code-quality/
[pylint]: https://pylint.pycqa.org/en/latest/user_guide/
[pdb]: https://docs.python.org/3.9/library/pdb.html
[pytest-pdb]: https://docs.pytest.org/en/6.2.x/usage.html#dropping-to-pdb-python-debugger-on-failures
[psf-installer]: https://www.python.org/downloads/
[marking test functions with attributes]: https://docs.pytest.org/en/6.2.x/mark.html#raising-errors-on-unknown-marks
[working with custom markers]: https://docs.pytest.org/en/6.2.x/example/markers.html#working-with-custom-markers
[configuration file formats]: https://docs.pytest.org/en/6.2.x/customize.html#configuration-file-formats
