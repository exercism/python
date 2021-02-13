:wave: Thank you for your interest in contributing to the exercism Python track!  

:warning: **Please Note** :warning:

We are currently in the middle of re-arranging and re-configuring  our track for exercism V3. 

We're **super-excited** :tada: :rocket: -- _and we really want you to be involved!_ -- but all that inital configuration work means **our maintainers can't accept unsolicited contributions at this time.**

Please check our [issue list](https://github.com/exercism/python/labels/help%20wanted) for tasks we've flagged as `[help wanted]`  -- _and check back_ -- we'll be adding (_many more!_) tasks with that flag in the coming weeks as we update our documentation and identify exercises, documents, and bugs that need to be worked on before our V3 launch.

---

# Exercism Python Track

[![Build Status](https://github.com/exercism/python/workflows/Exercises%20check/badge.svg)](https://github.com/exercism/python/actions?query=workflow%3A%22Exercises+check%22)
[![Join the chat at https://gitter.im/exercism/python](https://badges.gitter.im/exercism/python.svg)](https://gitter.im/exercism/python?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Exercism exercises in Python  


## Contributing Guide

Our WIP V3 documentation can be found here:  [exercism V3](https://github.com/exercism/docs).


### Testing

All exercises must be compatible with Python version 3.8 upwards.  We no longer support Python 2.x.

To test a single exercise:
```
python3 test/check-exercises.py [exercise-name]
```

To test all exercises:
```
python3 test/check-exercises.py
```


### Code Style

The Python code in this repo is meant to follow the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) (a stylized version http://pep8.org).

This repo uses [flake8](http://flake8.readthedocs.org/en/latest/) with default settings to enforce the coding standard.


### CI build


## License
This repository uses the [MIT License](/LICENSE).
