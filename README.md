# Exercism Python Track

[![Build Status](https://github.com/exercism/python/workflows/Exercises%20check/badge.svg)](https://github.com/exercism/python/actions?query=workflow%3A%22Exercises+check%22)
[![Join the chat at https://gitter.im/exercism/python](https://badges.gitter.im/exercism/python.svg)](https://gitter.im/exercism/python?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Exercism exercises in Python


## Contributing Guide

Please see the [Exercism contributing guide](https://github.com/exercism/docs/blob/master/contributing-to-language-tracks/README.md)
and the [Python track contributing guide](CONTRIBUTING.md)


## Working on the Exercises

We welcome both improvements to the existing exercises and new exercises.
A list of missing exercise can be found here: https://github.com/exercism/python/issues/417#issuecomment-366040062


### Conventions

- We use minimalistic stub files for all exercises ([#272](https://github.com/exercism/python/issues/272)).
- We use `unittest` (Python Standard Library) and no 3rd-party-framework.
- We use the parameter order `self.assertEqual(actual, expected)` ([#440](https://github.com/exercism/python/issues/440)).
- We use context managers (`with self.assertRaises(\<exception type\>):`) for testing for exceptions ([#477](https://github.com/exercism/python/issues/477)).
- We use an established utility method to confirm that expected exceptions contain a non-empty message. This method must be included for any test class with an exception-based test case ([#1080](https://github.com/exercism/python/issues/1080#issuecomment-442068539)).
- We use `assertIs(actual, True)` and `assertIs(actual, False)` rather than `assertTrue(actual)` or `assertFalse(actual)` ([#419](https://github.com/exercism/python/pull/419)).
- We use a comment string in the test file to reference the version of the exercise's `canonical-data.json` that tests were adapted from (wording can be found in: [#784](https://github.com/exercism/python/issues/784)).


### Testing

All exercises must be compatible with Python version 3.4 upwards.

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

This repo uses `travis-ci` in the following configuration: [travis.yml](https://github.com/exercism/python/blob/master/.travis.yml)

It will automatically check the code style, the problem configuration, and run the unittests with all supported Python versions.


## Pull Requests

We :heart: pull requests!
We even :sparkling_heart: them if they contain well written commit messages!

Please write the first line of your commit message in the following style:

```exercise-name: Change some things```

Please try to follow the [The seven rules of a great Git commit message](https://chris.beams.io/posts/git-commit/#seven-rules) like to capitalize the subject line and use the imperative mood. If there are more details to add, put those into the body of the commit message.

If you're interested, Tim Pope even has an [entire blog post](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) on good commit messages.

If you're new to Git, take a look at [this short guide](https://github.com/exercism/docs/blob/master/contributing-to-language-tracks/README.md#git-basics).

## License
This repository uses the [MIT License](/LICENSE).
