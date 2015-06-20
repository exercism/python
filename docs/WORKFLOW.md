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

### Running All Tests for All Exercises

```bash
$ cd exercism/python/
$ py.test
```

Read the [pytest documentation](http://pytest.org/latest/contents.html#toc) and [pytest-cache](http://pythonhosted.org/pytest-cache/) documentation to learn more.
