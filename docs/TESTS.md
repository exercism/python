## Installing `pytest`

We recommend you install [pytest](http://pytest.org/latest/) and
[pytest-cache](http://pythonhosted.org/pytest-cache/). `pytest` is a testing
tool that will give you more flexibility over running your unit tests.

If you want to install `pytest` for Python 2, then use `pip`.

```bash
pip install pytest pytest-cache
```
If you instead want the version of `pytest` for Python 3, then use `pip3`.

```bash
pip3 install pytest pytest-cache
```

If you get a `command not found` response from your system, you can find a
tutorial on how to install `pip`
[here](https://pip.pypa.io/en/stable/installing/).

**Note:** Whichever version of `pytest` you install last will be the default one used whenever `pytest` is executed, regardless of whether you have installed both versions.

If you want to check what the default version of `pytest` being used is, run the following:

```bash
pytest --version
```

If you have either version of `pytest` installed and you want to specifically run one of the versions, you can run that version by using `python` with the `-m` flag.

For example, you could run the Python 3 version of pytest like so:

```bash
$ python3 -m pytest --version
This is pytest version 3.2.3, imported from /usr/local/lib/python3.5/dist-packages/pytest.py
```

If you choose not to install `pytest`, you can still run tests individually and
skip the rest of this tutorial:

```bash
cd exercism/python/bob
python bob_test.py
```

## Running the Tests

### Run All Tests

To run all tests for a specific exercise (we will take the `bob.py` exercise as
an example here), place yourself in the directory where that exercise has been
fetched and run:

```bash
pytest bob_test.py
```

**Note:** To run the tests you need to pass the name of the testsuite file to
`pytest` (generally, the file ending with `_test.py`), **NOT** the file you
created to solve the problem (which is your _implementation_). This is because
in the latter case, since there are no defined test cases in your
implementation, `pytest` will just return a positive result, specifying that
it ran zero tests. Like this:

```
=============================  bob.py  ==============================

---------------------------------------------------------------------

Ran 0 tests in 0.000s

OK
```

### More `pytest` Examples

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

We recommend you run this command while working on exercises.

```bash
cd exercism/python/bob
pytest -x --ff bob_test.py
```

## PDB

Will drop you into the python debugger when a test fails. To learn how to use
pdb, check out the
[documentation](https://docs.python.org/3/library/pdb.html#debugger-commands).

```bash
pytest --pdb bob_test.py
```

You may also be interested in watching [Clayton Parker's "So you think you can
pdb?" PyCon 2015 talk](https://www.youtube.com/watch?v=P0pIW5tJrRM).

## PEP8

PEP8 is the [Style Guide for Python
Code](https://www.python.org/dev/peps/pep-0008/). If you would like to test for
compliance to the style guide, install
[pytest-pep8](https://pypi.python.org/pypi/pytest-pep8).

```bash
pip install pytest-pep8
```

Then, just add the `--pep8` flag to your command

```bash
pytest --pep8 bob_test.py
```

Read the [pytest documentation](http://pytest.org/latest/contents.html#toc) and
[pytest-cache](http://pythonhosted.org/pytest-cache/) documentation to learn
more.
