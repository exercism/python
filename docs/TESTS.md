# Installing `pytest`

First of all, install `pytest` through `pip`.
```
pip install pytest
```
If you get a `command not found` response from your system, you can find a tutorial on how to install `pip`   [here](https://pip.pypa.io/en/stable/installing/).

# Running the Tests

To run the tests for a specific exercise (we will take the `bob.py` exercise as an example here), place yourself in the directory where that exercise has been fetched and run:

```
py.test bob_test.py
```

This will run all the tests, whether they fail or not. If you'd rather stop the process and exit on the first failure, run:

```
py.test -x bob_test.py
```

**Note:** To run the tests you need to pass the name of the testsuite file to `pytest` (generally, the file ending with `_test.py`), **NOT** the file you created to solve the problem (which is your _implementation_). This is because in the latter case, since there are no defined test cases in your implementation, `pytest` will just return a positive result, specifying that it ran zero tests. Like this:

```
=============================  bob.py  ==============================

----------------------------------------------------------------------

Ran 0 tests in 0.000s

OK
```
