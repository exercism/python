# xPython

[![Build Status](https://travis-ci.org/exercism/xpython.svg?branch=master)](https://travis-ci.org/exercism/xpython) [![Requirements Status](https://requires.io/github/exercism/xpython/requirements.svg?branch=master)](https://requires.io/github/exercism/xpython/requirements/?branch=master)
[![Join the chat at https://gitter.im/exercism/xpython](https://badges.gitter.im/exercism/xpython.svg)](https://gitter.im/exercism/xpython?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Exercism exercises in Python

## Contributing Guide

Please see the [contributing guide](https://github.com/exercism/x-common/blob/master/CONTRIBUTING.md)

## Working on the Exercises

We welcome both improvements to the existing exercises and new exercises.
A pool of exercise ideas can be found in the [x-common repo](https://github.com/exercism/x-common).

All exercises must be compatible with Python versions 2.7 and 3.3 upwards.
Therefore please test your changes with these versions.

Test a single exercise with Python 2.7:
```
python2.7 test/check-exercises.py [exercise-name]
```

Test a single exercise with Python 3.3:
```
python3.3 test/check-exercises.py [exercise-name]
```

Test all exercises:
```
python test/check-exercises.py
```

## Code Style

The Python code in this repo is meant to follow the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/).

This repo uses [flake8](http://flake8.readthedocs.org/en/latest/) with default settings to enforce the coding standard. When you submit a PR, it needs to pass the flake8 tool with no warnings, or it won't be accepted.

## Pull Requests

We :heart: pull requests! 
We even :sparkling_heart: them if they contain well written commit messages!

Please write the first line of your commit message in the following style:

```exercise-name: Changes some things``` 

If there are more details to add, put those into the body of the commit message.

If you're interested, Tim Pope even has an [entire blog post](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) on good commit messages.

If you're new to Git take a look at [this short guide](https://github.com/exercism/x-common/blob/master/CONTRIBUTING.md#git-basics).

## License

The MIT License (MIT)

Copyright (c) 2014 Katrina Owen, _@kytrinyx.com

## Python icon
The Python logo is an unregistered trademark. We are using a derived logo with the permission of the Python Software Foundation.
