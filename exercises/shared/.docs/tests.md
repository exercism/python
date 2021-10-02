# Tests

To run the included *test files*, run the test file using the `pytest` module, replacing `{exercise_name}`:

```bash
$ python3 -m pytest {exercise_name}_test.py
```

Many IDE's and code editors have built-in support for using Pytest to run tests; check them out [here](https://github.com/exercism/python/blob/main/docs/TOOLS.md#editors-and-ides).

For more information about running tests using `pytest`, checkout our [Python testing guide](https://github.com/exercism/python/blob/main/docs/TESTS.md#pytest).

### Common pytest options

- `-v` : enable verbose output.
- `-x` : stop running tests on first failure.
- `--ff` : run failures from previous test before running other test cases.

For other options, see `python3 -m pytest -h`.
