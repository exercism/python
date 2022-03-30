# Tools

A list of tools, IDEs, and editors that can help with writing and debugging Python code.

<br>

---

- [Environments](#virtual-environments)
  - [Venv](#creating-a-virtual-environment-with-venv)
  - [Conda](#creating-a-virtual-environment-using-conda)
  - [Virtual Environment Wrapper](#virtual-environment-wrapper)
- [Editors and IDEs](#editors-and-ides)
  - [Visual Studio Code](#visual-studio-code)
    - [Python for Visual Studio Code](#python-for-vs-code)
  - [PyCharm](#pycharm)
  - [Spyder IDE](#spyder-ide)
  - [Emacs](#emacs)
  - [Vim](#vim)
  - [SpaceMacs](#spacemacs)
  - [Sublime text](#sublime-text)

---


<br>


**Disclaimer:** This is a collection of tools that are popular in our community.
It is not intended to be prescriptive nor exhaustive.
We think these tools do their job well, but there are most certainly other tools that are also good.
If you have an editor, IDE, tool, or plugin recommendation, we encourage you to add it to this document [on GitHub][python track on github].
Exercism does not have any financial affiliation with any of the tools listed below.

Before you start, make sure that you have a recent version of Python installed.
The Exercism platform currently supports `Python 3.8` (_exercises and tests_) and `Python 3.9` (_tooling_).
For more information, please refer to [Installing Python locally][Installing Python locally].

<br>

## Virtual Environments

Python virtual environments offer lightweight runtime and package isolation.
 They can help to organize your projects by keeping the Python packages you install bundled together inside a particular environment directory.
Different environments can hold different versions of the Python runtime together with any project or library dependencies.
This helps avoid bugs and incompatibilities caused by upgrading a library for one project that "breaks" a dependency in a different one.

There are two major *virtual environment* tools in use today, the Python standard library [`venv`][venv] and the third-party [`conda env`][condaenv], using the [`conda`][conda] package manager and (_usually_) the Anaconda Python distribution.
Both of are straightforward to use and/or install.

Additionally, [`PyEnv`][pyenv] and [virtualenvwrapper][virtualenvwrapper] are tools that can help to manage multiple versions of Python and multiple Python environments on the same machine.

### Creating a virtual environment with `venv`

To create a virtual environment using `venv`, `cd` to the directory you want to store your environments in.
This should be a directory **separate from** the code for your project, and one you will **not** be checking into source control.
Next, run the `venv` command with the name of a folder where you want to store this particular **environment**.
Common convention is to call that folder `<project-name-here>_venv`:

**Windows**

```powershell
PS C:\Users\foobar> py -m venv {name_of_virtualenv}
```
To activate the virtual environment, run the following command:

```powershell
PS> .\{name_of_virtual_env}\Scripts\activate.bat
(venv) PS> _
```

<br>

**Linux/MacOS**

```bash
$ python3 -m venv {name_of_virtualenv}
created virtual environment ... in 8568ms
```

To activate the virtual environment, run the following command:

```bash
$ source {name_of_virtual_env}/bin/activate
(venv) $ _
```

Once a `venv` is activated, you can run `pip` commands for package installation "inside" the environment.
Installed packages will be associated with the `venv`s version of Python, and located inside `{name_of_virtual_env}/Lib`.

_Deactivating_ a virtual environment can be done by calling the `deactivate` script, located in the same directory as `activate`.

<br>

### Creating a Virtual Environment using `conda`

*The latest `conda` version can be installed via [miniconda][miniconda].*
This [`conda` cheatsheet][conda-cheatsheet] is very helpful, as are the [`conda` docs][conda-docs].

Originally created as a Python package manager for the popular [`Anaconda distribution`][anaconda] of "scientific Python", `conda` was later generalized and extended.
`conda` environments are similar to `venv`s, with the key difference being that `conda` can create virtual environments and install packages for many other programming languages in addition to Python.
Currently supported languages include `R`, `JavaScript`, `Ruby`, `Fortran`, `C/C++`, `Scala`, `Java`, and more.
For a comparison of `conda` commands vs `venv` commands, see the conda [command reference][conda command ref].


#### MacOS/Linux

To create a `conda` environment, type the following, replacing `{name of environment}` with your chosen name, and `python={version}` with your desired version of Python.
This can be followed by any additional packages you wish to install inside the environment:

```bash
$ conda create --name {name of environment} python={version} "pytest>6.0" pylint
...

## Package Plan ##

  environment location: /usr/local/anaconda3/envs/test_env

  added / updated specs:
    - pylint
    - pytest[version='>6']
    - python=3.10


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    astroid-2.11.1             |  py310h2ec42d9_0         364 KB  conda-forge
    dill-0.3.4                 |     pyhd8ed1ab_0          62 KB  conda-forge
    lazy-object-proxy-1.7.1    |  py310he24745e_0          32 KB  conda-forge
    libzlib-1.2.11             |    h6c3fc93_1014          60 KB  conda-forge
    mccabe-0.7.0               |     pyhd8ed1ab_0          11 KB  conda-forge
    openssl-3.0.2              |       h6c3fc93_1         2.5 MB  conda-forge
    pip-22.0.4                 |     pyhd8ed1ab_0         1.5 MB  conda-forge
    platformdirs-2.5.1         |     pyhd8ed1ab_0          15 KB  conda-forge
    pylint-2.13.1              |     pyhd8ed1ab_0         284 KB  conda-forge
    pytest-7.1.1               |  py310h2ec42d9_0         464 KB  conda-forge
    python-3.10.4              |h1cc4136_0_cpython        13.2 MB  conda-forge
    setuptools-61.1.1          |  py310h2ec42d9_0         1.3 MB  conda-forge
    sqlite-3.37.1              |       hb516253_0         1.8 MB  conda-forge
    tzdata-2022a               |       h191b570_0         121 KB  conda-forge
    wrapt-1.14.0               |  py310h1961e1f_0          46 KB  conda-forge
    zlib-1.2.11                |    h6c3fc93_1014          89 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        21.8 MB

Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate test_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

<br>

#### Windows

Creating a `conda` environment on Windows uses the same general commands as above.
However, it is recommended that you use either the Anaconda `cmd` or `powershell` prompts over adding `conda` to your path:

```powershell
(base) PS C:\Users\foobar> conda create --name {name_of_environment} python={version} "pytest>6" pylint
...

Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\ProgramData\Anaconda3\envs\test_env

  added / updated specs:
    - pylint
    - pytest[version='>6']
    - python=3.10


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    astroid-2.11.1             |  py310h5588dad_0         364 KB  conda-forge
    attrs-21.4.0               |     pyhd8ed1ab_0          49 KB  conda-forge
    bzip2-1.0.8                |       h8ffe710_4         149 KB  conda-forge
    ca-certificates-2021.10.8  |       h5b45459_0         176 KB  conda-forge
    dill-0.3.4                 |     pyhd8ed1ab_0          62 KB  conda-forge
    isort-5.10.1               |     pyhd8ed1ab_0          79 KB  conda-forge
    lazy-object-proxy-1.7.1    |  py310he2412df_0          34 KB  conda-forge
    libffi-3.4.2               |       h8ffe710_5          41 KB  conda-forge
    libzlib-1.2.11             |    h8ffe710_1014          64 KB  conda-forge
    mccabe-0.7.0               |     pyhd8ed1ab_0          11 KB  conda-forge
    openssl-3.0.2              |       h8ffe710_1        10.1 MB  conda-forge
    packaging-21.3             |     pyhd8ed1ab_0          36 KB  conda-forge
    pip-22.0.4                 |     pyhd8ed1ab_0         1.5 MB  conda-forge
    platformdirs-2.5.1         |     pyhd8ed1ab_0          15 KB  conda-forge
    pluggy-1.0.0               |  py310h5588dad_2          26 KB  conda-forge
    py-1.11.0                  |     pyh6c4a22f_0          74 KB  conda-forge
    pylint-2.13.1              |     pyhd8ed1ab_0         284 KB  conda-forge
    pyparsing-3.0.7            |     pyhd8ed1ab_0          79 KB  conda-forge
    pytest-7.1.1               |  py310h5588dad_0         483 KB  conda-forge
    python-3.10.4              |hcf16a7b_0_cpython        16.2 MB  conda-forge
    python_abi-3.10            |          2_cp310           4 KB  conda-forge
    setuptools-61.1.1          |  py310h5588dad_0         1.3 MB  conda-forge
    sqlite-3.37.1              |       h8ffe710_0         1.2 MB  conda-forge
    tk-8.6.12                  |       h8ffe710_0         3.5 MB  conda-forge
    tomli-2.0.1                |     pyhd8ed1ab_0          16 KB  conda-forge
    typing-extensions-4.1.1    |       hd8ed1ab_0           8 KB  conda-forge
    typing_extensions-4.1.1    |     pyha770c72_0          29 KB  conda-forge
    tzdata-2022a               |       h191b570_0         121 KB  conda-forge
    vc-14.2                    |       hb210afc_6          13 KB  conda-forge
    vs2015_runtime-14.29.30037 |       h902a5da_6         1.3 MB  conda-forge
    wheel-0.37.1               |     pyhd8ed1ab_0          31 KB  conda-forge
    wrapt-1.14.0               |  py310he2412df_0          49 KB  conda-forge
    xz-5.2.5                   |       h62dcd97_1         211 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        37.5 MB

Proceed ([y]/n)? y
...
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate test_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

<br>

### Virtual Environment wrapper

Documents and background: [virtualenvwrapper][virtualenvwrapper].

The `virtualenvwrapper` package works on top of `venv` to manage all your virtual environments in one place.
 You can create, copy, delete and switch between environments with linux-like commands such as `lsvirtualenv` (_to list envs_) and `mkvirtualenv` (_to make an env_).
  It also allows you to add additional management tools using extensions.
  You can even create your own extensions to the tool using [this tutorial][venv wrapper tutorial].


### PyEnv

`pyenv` is the Python fork of the popular `rbenv`/`ruby-build` tools modified for Python.
It is essentially a set of scripts and shims that allow for setting Python versions on both a global and user-specific basis.
It tries to adhere to the Unix tradition of a single-purpose, unobtrusive tool that does one thing well.

`pyenv` and the `pyenv` docs can be found on [GitHub][pyenv on github].


<br>


## Editors and IDEs

### Visual Studio Code

[Visual studio code (VS Code)][vscode] is a free code editor created by Microsoft.
It includes great support for both [virtual/conda environments][virtual environments in vscode], as well as [`docker`][docker in vscode] (_via the [docker plug-in][vs code docker plugin]_) and can be extended with many different plugins for [testing][python testing in vscode], [linting][linting python in vscode], [formatting][formatting python in vscode], and [web development][python web dev in vscode].

#### Python for VS Code

Extension: _Extension-id: ms-python.python_

![Python Extension Header on VS Code](https://raw.githubusercontent.com/exercism/python/main/docs/img/VSCode-EXT-Python-Header.png)

The [Python extension from Microsoft][MS Python extension] is the official Microsoft Python extension to VS Code, and a highly recommended installation.
It has a wide range of features, including environment management, test management, linting, and debugging.
As of the [latest release][vs code python latest release], installing the MS Python extension will also download [pylance][vs code pylance] (_a popular package for linting and validating Python code_), and [jupyter][vs code jupyter] (_for working with Jupyter Notebooks_).

- A setup tutorial is available [here][python extension setup tutorial] and the [settings reference][vs code python settings reference] is very helpful.
- Information on setting up Python versions/working with virtual environments can be found [here][virtual environments in vscode].
- Information on setting up and working with unittest and pytest in VS Code can be found [here][python testing in vscode].

<br>

### PyCharm

[PyCharm][pycharm download] is an `IDE` (_Integrated Development Environment_) built by [JetBrains][jetbrains].
 It is purpose-built for Python and is popular among professionals .
 Like VS Code, it can be extended with various paid and unpaid plugins, themes, and formatters.
 The paid version also supports [Django development][pycharm django dev], [Docker development][pycharm docker], and [Database integration][pycharm database tools].

- Information on setting up Python versions can be found in [configuring a Python Interpreter][pycharm interpreter config] and [configuring a virtual environment][pycharm config venv].
- Steps for setting up pytest with pycharm can be found [here][pycharm pytest docs].
  - Pycharm defaults to using `unittest`, so you must have `pytest` installed into the environment you are using with pycharm (_see the interpreter and environment documents above_), and then point pycharm to it.
  - [Running Tests][pycharm gui running tests] directly from the GUI is really easy, but don't forget to take a good look at the underlying [pytest parameters](TESTS.md#extra-arguments), so that it is set up to your liking.
- General documentation for running tests and debugging in pycharm can be found [here][pycharm run tests].
- Additional debugging tools and guidance can be found [here][pycharm debugging tools].
  -  **warning**:  The `coverage` plugin for `pytest` will break pycharm's debugger.
     See [run/debug configuration: pytest][pycharm debug configuration] for more information.

<br>

### Spyder IDE

[Spyder][spyder-ide] is a cross-platform free and open source Python IDE tailored for the scientific community.
It is commonly included with the Anaconda distribution of Python, but can be [installed by itself][spyder standalone installers] and used with any version of Python.
We recommend a standalone installation to ensure maximum flexibility, and that there are no package conflicts.

Spyder fully supports `venv` and `conda` environments.
It includes an integrated [IPython][ipython] interactive terminal, an interactive debugger, and rich support for in-editor graphing and data exploration.
Additional code completion and linting are provided via [kite][kite].
Integrations with [Jupyter Notebooks][spyder notebook plugin] and [testing tools][spyder unittest plugin] are provided via community-developed plugins.
You can also write [plugins of your own][writing spyder plugins], using the Spyder API.

- Setting Python [versions/virtual environments][spyder environments] in Spyder
- Setting up Spyder to run `unittest` and `pytest` tests via [spyder unittest plugin][spyder unittest plugin]
- Spyder [installation guide][spyder installation guide]
  - [Standalone installers][spyder standalone installers]
  - [Alternative installation methods][spyder alternate installation]
  - [Notes on upgrading Spyder][spyder updating install]
- Spyder [quickstart guide][spyder quickstart guide]
  - [First steps video][spyder first steps]
  - [Running via Anaconda][spyder with Anaconda]
  - [Creating a conda env just for Spyder][spyder conda env]
- Spyder [FAQ][spyder faq]
- Spyder [troubleshooting guide][spyder troubleshooting guide]
- Additional [spyder plugins][spyder plugins list]

<br>

### Emacs

[Emacs][emacs] is a free, open source, and highly customizable text editor written in Lisp.
A great [installation and setup guide][emacs setup at real python] is available at Real Python.

- The [Emacs Wiki][emacs wiki python programming] also has a good guide to Python programming with Emacs.
- [Full Stack Python][emacs at fullstack python] also collects some good information and links for getting started with Emacs.

<br>

### Vim

[Vim][vimdotorg] is a free and "improved" version of the Unix standard `vi` text editor.
It is available on a wide variety of operating systems and Linux/Unix flavors.
A great [installation and setup guide][vim setup at real python] is available at Real Python, and handy cheat sheets are available at [vimsheet][vim cheat sheet], [glump][glump vim cheatsheet], and [rtorr][rtorr vim cheat sheet].


Even if you decide editing Python code in `vim` is not for you, it is recommended that you familiarise with a basic set of commands.
`vim` or `vi` is often a "base" or "default" text editor in Linux and Unix distributions and is the default editor for `git` commit messages (_among other things_) on those systems.
Chances are good you will find yourself on a *nix system needing to edit a configuration file with only `vi` available, so knowing how to [quit vim][how do I quit vim] is (_at the very least_) good self defense.

<br>

### Spacemacs

[Spacemacs][spacemacs] (_[github repo][spacemacs github repo]_) is a free community-driven distribution of Emacs that combines functionality from both Emacs and Vim.

- Official documentation can be found [here][spacemacs official docs]
- This [guide][opensource spacemacs guide] at opensource gives a quick rundown of installation and configuration options.
- The spacemacs [python layer][spacemacs python layer] adds functionality for testing, linting, environment management, and code formatting.

<br>

### Sublime text

[Sublime text][sublime text 4] is a paid text editor for coding, made by *Sublime HQ Pty Ltd*.
It is similar to [VS Code](#visual-studio-code) and [Atom][atom], with many [packages and plugins][sublime package control] for customization.
You can also [develop plugins][sublime plugin development] of your own for the editor using Python.

- [Purchasing and installing][sublime purchasing and installing] Sublime
- Sublime [documentation][sublime official docs] and [support documentation][sublime support docs]
- Sublime [community documentation][sublime community docs]
- Full Stack Python has a great guide on [Sublime Text][sublime at fullstack python], with many links to tutorials.
- Real Python also offers a great guide to [setting up Sublime Text 3][sublime text at real python]
- The Chromium project also has [setup and usage][sublime chromium setup] instructions.

[Installing Python locally]: https://exercism.org/docs/tracks/Python/installation
[MS Python extension]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[anaconda]: https://www.anaconda.com/products/individual
[atom]: https://atom.io/
[conda command ref]: https://docs.conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands
[conda-cheatsheet]: https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf
[conda-docs]: https://docs.conda.io/projects/conda/en/latest/user-guide/index.html
[conda]: https://docs.conda.io/projects/conda/en/latest/index.html
[condaenv]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[docker in vscode]: https://code.visualstudio.com/docs/containers/overview
[emacs at fullstack python]: https://www.fullstackpython.com/emacs.html
[emacs setup at real python]: https://realpython.com/emacs-the-best-python-editor
[emacs wiki python programming]: https://www.emacswiki.org/emacs/PythonProgrammingInEmacs#h5o-4
[emacs]: https://www.gnu.org/software/emacs/
[formatting python in vscode]: https://code.visualstudio.com/docs/python/editing#_formatting
[glump vim cheatsheet]: https://www.glump.net/_media/howto/desktop/vim-graphical-cheat-sheet-and-tutorial/vi-vim-cheat-sheet-and-tutorial.pdf
[how do I quit vim]: https://stackoverflow.com/questions/11828270/how-do-i-exit-the-vim-editor
[ipython]: https://ipython.org/
[jetbrains]: https://www.jetbrains.com/
[kite]: https://www.kite.com/
[linting python in vscode]: https://code.visualstudio.com/docs/python/linting
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[opensource spacemacs guide]: https://opensource.com/article/19/12/spacemacs
[pycharm config venv]: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
[pycharm database tools]: https://www.jetbrains.com/help/pycharm/relational-databases.html
[pycharm debug configuration]: https://www.jetbrains.com/help/pycharm/run-debug-configuration-py-test.html
[pycharm debugging tools]: https://www.jetbrains.com/help/pycharm/debugging-code.html
[pycharm django dev]: https://www.jetbrains.com/help/pycharm/django-support7.html
[pycharm docker]: https://www.jetbrains.com/help/pycharm/docker.html
[pycharm download]: https://www.jetbrains.com/pycharm/download/
[pycharm gui running tests]: https://www.jetbrains.com/help/pycharm/pytest.html#run-pytest-test
[pycharm interpreter config]: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
[pycharm pytest docs]: https://www.jetbrains.com/help/pycharm/pytest.html
[pycharm run tests]: https://www.jetbrains.com/help/pycharm/performing-tests.html
[pyenv on github]: https://github.com/pyenv/pyenv
[pyenv]: https://github.com/pyenv/pyenv
[python extension setup tutorial]: https://code.visualstudio.com/docs/python/python-tutorial
[python testing in vscode]: https://code.visualstudio.com/docs/python/testing
[python track on github]: https://github.com/exercism/python/blob/main/docs/TOOLS.md
[python web dev in vscode]: https://code.visualstudio.com/docs/python/tutorial-django
[rtorr vim cheat sheet]: https://vim.rtorr.com/
[spacemacs github repo]: https://github.com/syl20bnr/spacemacs
[spacemacs official docs]: https://github.com/syl20bnr/spacemacs#documentation
[spacemacs python layer]: https://www.spacemacs.org/layers/+lang/python/README.html
[spacemacs]: https://www.spacemacs.org/
[spyder alternate installation]: https://docs.spyder-ide.org/current/installation.html#alternative-methods
[spyder conda env]: https://docs.spyder-ide.org/current/installation.html#new-conda-environment
[spyder environments]: https://docs.spyder-ide.org/5/faq.html#using-existing-environment
[spyder faq]: https://docs.spyder-ide.org/5/faq.html
[spyder first steps]: https://docs.spyder-ide.org/current/videos/first-steps-with-spyder.html
[spyder installation guide]: https://docs.spyder-ide.org/current/installation.html
[spyder notebook plugin]: https://github.com/spyder-ide/spyder-notebook
[spyder plugins list]: https://docs.spyder-ide.org/5/faq.html#using-plugins
[spyder quickstart guide]: https://docs.spyder-ide.org/current/quickstart.html
[spyder standalone installers]: https://docs.spyder-ide.org/current/installation.html#standalone-installers
[spyder troubleshooting guide]: https://github.com/spyder-ide/spyder/wiki/Troubleshooting-Guide-and-FAQ
[spyder unittest plugin]: https://github.com/spyder-ide/spyder-unittest
[spyder updating install]: https://docs.spyder-ide.org/current/installation.html#updating-spyder
[spyder with Anaconda]: https://docs.spyder-ide.org/current/installation.html#anaconda
[spyder-ide]: https://www.spyder-ide.org/
[sublime at fullstack python]: https://www.fullstackpython.com/sublime-text.html
[sublime chromium setup]: https://chromium.googlesource.com/chromium/src.git/+/HEAD/docs/sublime_ide.md
[sublime community docs]: https://docs.sublimetext.io/
[sublime official docs]: https://www.sublimetext.com/docs/index.html
[sublime package control]: https://packagecontrol.io/
[sublime plugin development]: https://docs.sublimetext.io/guide/extensibility/plugins/
[sublime purchasing and installing]: https://www.sublimetext.com/download
[sublime support docs]: https://www.sublimetext.com/support
[sublime text 4]: https://www.sublimetext.com/
[sublime text at real python]: https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/
[venv wrapper tutorial]: https://virtualenvwrapper.readthedocs.io/en/latest/plugins.html#plugins
[venv]: https://docs.python.org/3.9/tutorial/venv.html
[vim cheat sheet]: https://vimsheet.com/
[vim setup at real python]: https://realpython.com/vim-and-python-a-match-made-in-heaven/
[vimdotorg]: https://www.vim.org/
[virtual environments in vscode]: https://code.visualstudio.com/docs/python/environments
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/
[vs code docker plugin]: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
[vs code jupyter]: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
[vs code pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
[vs code python latest release]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[vs code python settings reference]: https://code.visualstudio.com/docs/python/settings-reference
[vscode]: https://code.visualstudio.com/
[writing spyder plugins]: https://docs.spyder-ide.org/current/workshops/plugin-development.html
