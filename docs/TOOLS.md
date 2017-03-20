## Visual Studio on Windows

Follow the installation instructions for [Python Tools for Visual Studio](https://pytools.codeplex.com/wikipage?title=PTVS%20Installation)

You can either start by creating your own project for working with the Exercism problems or you can download a Visual Studio solution that is already set up.

### Exercism.io Visual Studio Template

This is a Visual Studio template that comes pre-configured to work on the problems in as many languages as Visual Studio supports.

![Solution Explorer](/docs/img/SolutionExplorer.png)

1. Download the [Exercism.io Visual Studio Template](https://github.com/rprouse/Exercism.VisualStudio) from GitHub by clicking the Download Zip button on the page.
2. Unzip the template into your exercises directory, for example `C:\src\exercises`
2. Install the [Exercism CLI](http://exercism.io/cli)
3. Open a command prompt to your exercise directory
4. Add your API key to exercism `exercism configure --key=YOUR_API_KEY`
5. Configure your source directory in exercism `exercism configure --dir=C:\src\exercises`
6. [Fetch your first exercise](http://exercism.io/languages/python) `exercism fetch python hello-world`
7. Open the Exercism solution in Visual Studio
8. Expand the Exercism.python project
9. Click on **Show All Files** in Solution Explorer (See below)
10. The exercise you just fetched will appear greyed out. Right click on the folder and **Include In Project**
11. Get coding...

![Add files](/docs/img/AddFiles.png)

To run the tests, you can do so at the command line, or within Visual Studio.

![Test Explorer](/docs/img/TestExplorer.png)

## Code Style and Linting

There's a style guide called [PEP8](http://legacy.python.org/dev/peps/pep-0008/) that many Python projects adhere to.
Read it when you get a chance!

If you just want a quick overview of some problems in your code, use [pylint](http://www.pylint.org/)!
It can be pretty picky though, so take its results with a grain of salt.
If you don't agree with one of its points, that's a good topic for a discussion in the comments for your program!

If you'd rather have a tool take care of your style issues, take a look at [autopep8](https://github.com/hhatto/autopep8)!
Run `autopep8 -d mycode.py` to get a diff of the changes it proposes and `autopep8 -i mycode.py` to format the code inplace!
