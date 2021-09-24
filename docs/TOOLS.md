# Tools

IMPORTANT TODO: UPDATE URL PATHS OF IMAGES

Before you can start coding, make sure that you have the proper version of Python installed. Exercism currently supports `Python 3.8` and above. For more information, please refer to [Installing Python locally](https://exercism.org/docs/tracks/python/installation).

## Visual Studio Code

Visual studio code (VS Code) is a code editor created by Microsoft. It is not specialized to work for a specific programming language, but to be an editor that can do everything. You can extend the editor using extensions, but it comes with some great extensions as well.

### Python for VS Code

_Extension-id: ms-python.python_

![Python Extension Header on VS Code](C:\Users\jobko\OneDrive\Documenten\GitHub\python\docs\img\VSCode-EXT-Python-Header.png)

The Python extension from Microsoft is extremely useful because of its range of features. Notably it supports testing and has a testing explorer! It has many other features that you can view on [its homepage](https://marketplace.visualstudio.com/items?itemName=ms-python.python). 

#### Selecting the interpreter

The Python extensions supports the switching multiple `interpreters`, this way you can use different Python versions for different projects. This is also useful for when you are using `venv` or `conda`, which you find more about [here]().

![Interpreter selection]()

Click on the "Select interpreter" button in the lower left-hand of your window, another window should pop up where you can select the interpreter you want to use.

![Interpreter selection PT2](C:\Users\jobko\OneDrive\Documenten\GitHub\python\docs\img\VSCode-EXT-Python-SelectInterpreter-2.png)

Here, click on the Python installation you want to use and you can start coding!

#### Included testing

The Python extension comes with a `Testing` tab on your side-bar. This can be really useful to test your solutions with. 

![Python Testing Tab](C:\Users\jobko\OneDrive\Documenten\GitHub\python\docs\img\VSCode-EXT-Python-TestingConfiguration.png)

Configuration is easy, click on the `Configure Python Tests` button. A window will pop up asking you to select a _testing framework_, select `pytest` (find more about the installation of Pytest [here](/TESTS.md)) and then select the directory where the extension can find the tests. If the tests are in your current directory, select `root`.

![Tests Statuses](C:\Users\jobko\OneDrive\Documenten\GitHub\python\docs\img\VSCode-EXT-Python-TestsStatuses.png)

It will now show a collapsible tree of all the directories containing tests, it even shows you every test per file. Hovering over a directory or file will show a play button that, when pressed, runs all the tests inside of it. Pressing the play button on  a single test will only run that specific test, handy for when you're trying to fix a specific problem.



## Code Style and Linting

There's a style guide called [PEP8](http://legacy.python.org/dev/peps/pep-0008/) that many Python projects adhere to.
Read it when you get a chance!

If you just want a quick overview of some problems in your code, use [pylint](http://www.pylint.org/)!
It can be pretty picky though, so take its results with a grain of salt.
If you don't agree with one of its points, that's a good topic for a discussion in the comments for your program!

If you'd rather have a tool take care of your style issues, take a look at [autopep8](https://github.com/hhatto/autopep8)!
Run `autopep8 -d mycode.py` to get a diff of the changes it proposes and `autopep8 -i mycode.py` to format the code in place!
