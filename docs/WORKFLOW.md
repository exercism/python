##  Tests

We recommend you install [pytest](http://pytest.org/latest/) and [pytest-cache](http://pythonhosted.org/pytest-cache/). Pytest is a testing tool that will give you more flexibility over running your unit tests.

If you choose not to install pytest, you can still run tests individually:

```bash
$ cd exercism/python/bob
$ python bob_test.py
```

### Installation

```bash
$ pip install pytest pytest-cache
```

##  Pytest Examples

####Run All Tests

```bash
$ cd exercism/python/bob
$ py.test bob_test.py
```

####Stop After First Failure

```bash
$ cd exercism/python/bob
$ py.test -x bob_test.py
```

####Failed Tests First

Pytest-cache remembers which tests failed, and can run those tests first.

```bash
$ cd exercism/python/bob
$ py.test --ff bob_test.py
```

### Recommended

We recommend you run this command while working on exercises.

```bash
$ cd exercism/python/bob
$ py.test -x --ff bob_test.py
```

####Running All Tests for All Exercises

```bash
$ cd exercism/python/
$ py.test
```

####PDB

Will drop you into the python debugger when a test fails.
To learn how to use pdb, check out the [documentation](https://docs.python.org/2/library/pdb.html#debugger-commands).

You may also be interested in watching [Clayton Parker's "So you think you can pdb?" PyCon 2015 talk](https://www.youtube.com/watch?v=P0pIW5tJrRM)

```bash
$ cd exercism/python/bob
$ py.test --pdb bob_test.py
```

####PEP8

PEP8 is the [python style guide](https://www.python.org/dev/peps/pep-0008/). If you would like to test for compliance to the style guide, install [pytest-pep8](https://pypi.python.org/pypi/pytest-pep8)

```bash
$ pip install pytest-pep8
```

and add the pep8 flag to your command

```bash
$ cd exercism/python/bob
$ py.test --pep8 bob_test.py
```

Read the [pytest documentation](http://pytest.org/latest/contents.html#toc) and [pytest-cache](http://pythonhosted.org/pytest-cache/) documentation to learn more.
