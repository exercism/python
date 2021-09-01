# Tests

You can run the included tests by typing `pytest <exercisename>_test.py` on the command line from within the exercise's directory.

You can also tell Python to run the pytest module on the command line from either within the exercise directory or with a path to the exercise directory.
`python -m pytest <exercisename>_test.py` from within the exercise directory.

`python -m pytest /fully/qualified/path/to/<exercisename>/` OR `python -m pytest realtive/path/to/<exercisename>` from a non-exercise directory.

Many IDE's and code editors also have built-in support for using PyTest to run tests.

- [Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
- [PyCharm Professional & Community Editions](https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test)
- [Atom](https://atom.io/packages/atom-python-test)
- [Spyder](https://www.spyder-ide.org/blog/introducing-unittest-plugin/)
- [Sublime](https://github.com/kaste/PyTest)
- [vim-test](https://github.com/vim-test/vim-test)

See the [Python tests page](https://github.com/exercism/python/blob/main/docs/TESTS.md) for more information.

### Common `pytest` options

- `-v` : enable verbose output.
- `-x` : stop running tests on first failure.
- `--ff` : run failures from previous test before running other test cases.

For other options, see `python -m pytest -h`. PyTest documentation can be found [here](https://docs.pytest.org/en/latest/getting-started.html).
