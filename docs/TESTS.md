# Installing `pytest`

First of all, install `pytest` through `pip`.
```
pip install pytest
```
In case your system wouldn't be able to find `pip` and return a _command not found_, response,  [here](https://pip.pypa.io/en/stable/installing/) you can find a tutorial on how to install it.

# Running the Tests

To run the tests for a specific exercise (we will take the `bob.py` exercise as an example here), place yourself in the directory where that exercise has been fetched and run:

```
pytest bob_test.py
```

This will run all the tests, wethere they fail or not. If you'd rather stop the process and exit on the first failure, run:

```
pytest -x bob_test.py
```

**Note:** To run the tests you have to pass the name of the testsuite file to `pytest` (generally, the file ending with `_test.py`), **NOT** the file you created to solve the problem (which is, your _implementation_). This because in the latter case, since there are no defined test cases in your implementation, `pytest` will just return a positive result, specifying that it ran zero tests. Like this:

```
=============================  bob.py  ==============================

----------------------------------------------------------------------

Ran 0 tests in 0.000s

OK
```
