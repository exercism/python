# xPython

[![Build Status](https://travis-ci.org/exercism/xpython.png?branch=master)](https://travis-ci.org/exercism/xpython)

Exercism exercises in Python

## Contributing Guide

Please see the [contributing guide](https://github.com/exercism/x-api/blob/master/CONTRIBUTING.md#the-exercise-data)

## Working on the Exercises

We welcome both improvements to the existing exercises and new exercises.
A pool of exercise ideas can be found in the [x-common repo](https://github.com/exercism/x-common).

All exercises must be compatible with Python versions 2.7 and 3.3 upwards.
Therefore please test your changes at least with Python2.7 and Python3.5.

To test a single exercise, say crypto-square, run:
```
python2.7 test/check-exercises.py crypto-square
```
and
```
python3.5 test/check-exercises.py crypto-square
```

To run the tests for all exercises type:
```
python test/check-exercises.py
```

## Code Style

The Python code in this repo is meant to largely obey the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) (not all code does though).
Try the [flake8](http://flake8.readthedocs.org/en/latest/) tool if you feel unsure about questions of style.

## Pull Requests

We :heart: pull requests! 
We even :sparkling_heart: them if they contain well written commit messages!

Please write the first line of your commit message in the following style:

```exercise-name: Changes some things``` 

If there are more details to add, put those into the body of the commit message.

If you're interested, Tim Pope even has an [entire blog post](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) on good commit messages.

If you're new to Git take a look at [this short guide](http://help.exercism.io/git-workflow.html).

## License

The MIT License (MIT)

Copyright (c) 2014 Katrina Owen, _@kytrinyx.com
