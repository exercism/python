# Installing Python

If Python isn't already available on your system, detailed instructions by platform can be found in the [Python Setup and Usage][using python] section of the official documentation.
Real Python also offers a [nice guide][helpful guide] to installation on various platforms, including iOS and Android.

Finally, these posts by Brett Cannon [A quick-and-dirty guide][quick-and-dirty] and [Why you should use `python -m pip`][python-m-pip], give very helpful advice on how to manage Python installations and packages.

**Note for MacOS users:**  prior to MacOS Monterey (12.3), `Python 2.7` came pre-installed with the operating system.
Using `Python 2.7` with Exercism or most other programs is not recommended.
You should instead install Python 3 via one of the methods detailed below.
As of MacOS Monterey (12.3), no version of Python will be pre-installed via MacOS.

Some quick links into the documentation by operating system:

-  [Windows][windows] Additionally, this Microsoft article on [installing Python on windows][python-on-windows] is helpful.
-  [Unix & Linux Systems][unix-and-linux] (_these largely work for MacOS as well_)
-  [MacOS][macos] : **This is outdated.**
   We recommend reviewing some of the methods outlined in the Real Python article [Installing Python][installing-python] or the articles by Brett Cannon linked above.


Exercism tests and tooling currently support `Python 3.8` (_tests_) and `Python 3.9` (_tooling_).
This means that the [newest features of Python `3.10`][310-new-features] are **not** currently supported.
Please refer to the [Python 3.9.x documentation][3.9 docs] for what is currently supported.

[3.9 docs]: https://docs.python.org/3.9/
[310-new-features]: https://docs.python.org/3/whatsnew/3.10.html
[helpful guide]: https://realpython.com/installing-python/
[installing-python]: https://realpython.com/installing-python/#what-your-options-are_1
[macos]: https://docs.python.org/3/using/mac.html
[python-m-pip]: https://snarky.ca/why-you-should-use-python-m-pip/
[python-on-windows]: https://docs.microsoft.com/en-us/windows/python/beginners
[quick-and-dirty]: https://snarky.ca/a-quick-and-dirty-guide-on-how-to-install-packages-for-python/
[unix-and-linux]: https://docs.python.org/3/using/unix.html
[using python]: https://docs.python.org/3/using/index.html
[windows]: https://docs.python.org/3/using/windows.html
