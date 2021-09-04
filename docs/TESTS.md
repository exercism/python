# Tests

## Tools to install

We recommend you install [pytest](http://pytest.org/en/latest/) with the following plugins:

-  [pytest-cache](http://pythonhosted.org/pytest-cache/)
-  [pytest-subtests](https://github.com/pytest-dev/pytest-subtests)
-  [pytest-pylint](https://github.com/carsongee/pytest-pylint)

The PyTest [Getting Started Guide](https://docs.pytest.org/en/latest/getting-started.html) has quick general instructions, although they do not cover installing the plugins.
Continue reading below for plugin installation.

We also recommend [pylint](https://pylint.pycqa.org/en/latest/user_guide/), as it is part of our automated feedback on the website, and can be a very useful (if noisy!) code analysis tool.

Pylint can be a bit much, so this [tutorial](https://pylint.pycqa.org/en/latest/tutorial.html) can be helpful for getting started, as can this overview of [Code Quality: Tools and Best Practices](https://realpython.com/python-code-quality/) from Real Python.

Finally, [this site](https://pycodequ.al/docs/pylint-messages.html) is a great place to look up more human-readable descriptions of Pylint linting messages.


### Installing `pytest`

To install `pytest`, run the following command in the environment (_active `venv`, `conda env`, `docker container`, `vm` or other project space with Python 3.8 installed_):

```bash
pip3 install pytest pytest-cache pytest-subtests pytest-pylint
```

If you get a `command not found` response from your system, you can find a
tutorial on how to install `pip`
[here](https://pip.pypa.io/en/stable/installing/).

Once the installation has completed, you can check what the default version of `pytest` is by running the following:

```bash
pytest --version
```

## Testing

### Run All Tests for an Exercise

To run all tests for a specific exercise (_we will take the `bob.py` exercise as
an example here_), navigate to the directory where that exercise has been
downloaded and run the following in the terminal:

```bash
pytest bob_test.py
```

**Note:** To run the tests you need to pass the name of the testsuite file to
`pytest` (_generally, this will be the file ending with `_test.py`_), **NOT** the file that was
created to solve the exercsim problem (which is the _solution implementation_).
`PyTest` needs the test definitions in the `_test.py` file in order to know how to call, run, and exercise the _solution implementation_ code.
Since there are no test cases defined in the _solution implementation_, `pytest` will just return a positive result, specifying that it found and ran zero tests. Like this:


```
=============================  bob.py  ==============================

---------------------------------------------------------------------

Ran 0 tests in 0.000s

OK
```


### More `pytest` Examples

Below are some additional examples and details for getting up and running quickly with Pytest.
[How to invoke pytest](https://docs.pytest.org/en/latest/how-to/usage.html#usage) and [pytest command-line flags](https://docs.pytest.org/en/latest/reference/reference.html#command-line-flags) offer full details on all of pytests run options.


#### Stop After First Failure
The above will run all the tests, whether they fail or not. If you'd rather stop
the process and exit on the first failure, run:

```bash
pytest -x bob_test.py
```

#### Failed Tests First

`pytest-cache` remembers which tests failed, and can run those tests first.

```bash
pytest --ff bob_test.py
```

#### Running All Tests for All Exercises

```bash
cd exercism/python/
pytest
```

## Recommended Workflow

Try this command while working on exercises:

```bash
cd exercism/python/bob
pytest -x --ff bob_test.py
```

## PDB

Typing pdb on the command line will drop you into the python debugger when a test fails.
To learn how to usepdb, check out the
[documentation](https://docs.python.org/3/library/pdb.html#debugger-commands).

```bash
pytest --pdb bob_test.py
```
