# Exercism Python Track

[![Build Status](https://travis-ci.org/exercism/python.svg?branch=master)](https://travis-ci.org/exercism/python) [![Requirements Status](https://pyup.io/repos/github/exercism/python/shield.svg)](https://pyup.io/repos/github/exercism/python/)
[![Join the chat at https://gitter.im/exercism/python](https://badges.gitter.im/exercism/python.svg)](https://gitter.im/exercism/python?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Exercism exercises in Python


## Contributing Guide

Please see the [contributing guide](https://github.com/exercism/x-common/blob/master/CONTRIBUTING.md)


## Working on the Exercises

We welcome both improvements to the existing exercises and new exercises.
A list of missing exercise can be found here: http://exercism.io/languages/python/todo


### Conventions

- We use minimalistic stub files for all exercises (#272).
- We use `unittest` (Python Standard Library) and no 3rd-party-framework.
- We use the parameter order `self.assertEqual(actual, expected)` (#440).


### Testing

All exercises must be compatible with Python versions 2.7 and 3.3 upwards.

To test a single exercise (e.g., with Python 2.7):
```
python2.7 test/check-exercises.py [exercise-name]
```

To test all exercises (e.g., with Python 3):
```
python3 test/check-exercises.py
```


### Code Style

The Python code in this repo is meant to follow the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) (a stylized version http://pep8.org).

This repo uses [flake8](http://flake8.readthedocs.org/en/latest/) with default settings to enforce the coding standard.


### CI build

This repo uses `travis-ci` in the following configuration: [travis.yml](https://github.com/exercism/python/blob/master/.travis.yml)

It will check automatically the code style, the problem configuration and runns the unittests with all supported Python versions.


## Pull Requests

We :heart: pull requests! 
We even :sparkling_heart: them if they contain well written commit messages!

Please write the first line of your commit message in the following style:

```exercise-name: Changes some things``` 

If there are more details to add, put those into the body of the commit message.

If you're interested, Tim Pope even has an [entire blog post](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) on good commit messages.

If you're new to Git take a look at [this short guide](https://github.com/exercism/x-common/blob/master/CONTRIBUTING.md#git-basics).


## Python icon
The Python logo is an unregistered trademark. We are using a derived logo with the permission of the Python Software Foundation.
