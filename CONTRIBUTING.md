<br>

<img align="left" width="90" height="90" src="https://github.com/exercism/website-icons/blob/main/tracks/python.svg">
<p vertical-align="middle"><h1>Contributing</h1></p>

<br>
<br>

Hi. &nbsp;👋🏽 &nbsp;👋 &nbsp; **We are happy you are here.**&nbsp; 🎉🌟

Thank you so much for your interest in contributing!

**`exercsim/Python`** is one of many programming language tracks on [exercism(dot)org][exercism-website].
This repo holds all the instructions, tests, code, & support files for Python *exercises* currently under development or implemented & available for students.

 🌟 &nbsp;&nbsp;Track exercises support Python `3.8`.  
 🌟 &nbsp;&nbsp;Track tooling (_test-runner, representer, analyzer, and Continuous Integration_) runs on Python `3.9`.

Exercises are grouped into **concept** exercises which teach the [Python syllabus][python-syllabus], and **practice** exercises, which are unlocked by progressing in the syllabus tree &nbsp;🌴 &nbsp;. Concept exercises are constrained to a small set of language or syntax features. Practice exercises are open-ended, and can be used to practice concepts learned, try out new techniques, and _play_.  These two exercise groupings can be found in the track [config.json][config-json], and under the `python/exercises` directory.

<br>

<img align="left" width="110" height="100" src="https://github.com/exercism/website-icons/blob/main/exercism/logo-big-bordered.png">

🌟🌟&nbsp; If you have not already done so, please take a moment to read our [Code of Conduct][exercism-code-of-conduct].&nbsp;🌟🌟&nbsp;  
It might also be helpful to look at [Being a Good Community Member][being-a-good-community-member] & [The words that we use][the-words-that-we-use].

Some defined roles in our community:  [Contributors][exercism-contributors] **|** [Mentors][exercism-mentors] **|** [Maintainers][exercism-track-maintainers]  **|** [Admins][exercism-admins]

<br>
<img align="left" width="100" height="100" src="https://github.com/exercism/website-icons/blob/main/exercises/word-search.svg">

✨&nbsp;🦄&nbsp; _**Want to jump directly into Exercism specifications & detail?**_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Structure][exercism-track-structure] **|** [Tasks][exercism-tasks] **|** [Concepts][exercism-concepts] **|** [Concept Exercises][concept-exercises] **|** [Practice Exercises][practice-exercises] **|** [Presentation][exercise-presentation]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Writing Style Guide][exercism-writing-style] **|** [Markdown Specification][exercism-markdown-specification] (_&nbsp;✨ &nbsp; versions available in [contributing][website-contributing-section] on [exercism(dot)org][exercism-website]._)

<br>

## 🐛 **Did you find a bug?**

It is not uncommon to discover typos, confusing directions, or incorrect implementations of certain tests or code examples.  Or you might have a great suggestion for a hint to aid students (&nbsp;💙 &nbsp;), see optimizations for exemplar or test code, find missing test cases to add, or want to correct factual and/or logical errors.  Or maybe you have a great idea for an exercise or feature (❗&nbsp;).

_Our track is always a work in progress!_ 🌟🌟  
Please&nbsp;📛&nbsp;[ Open an issue ][open-an-issue]📛&nbsp;, and let us know what you have found/suggest.

<br>

## 🚧  **Did you write a patch that fixes a bug?**

 💛 💙&nbsp; **We Warmly Welcome Pull Requests that are:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1️⃣  &nbsp;&nbsp;&nbsp; Small, contained fixes for typos/grammar/punctuation/code syntax on [one] exercise,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2️⃣&nbsp;&nbsp;&nbsp;&nbsp; Medium changes that have been agreed/discussed via a filed issue,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3️⃣ &nbsp;&nbsp;&nbsp;&nbsp;Contributions from our [help wanted][help-wanted] issue list,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4️⃣ &nbsp;&nbsp;&nbsp;&nbsp;Larger (_and previously agreed-upon_) contributions from recent & regular (_within the last 6 months_) contributors.

When in doubt,&nbsp;📛&nbsp;[ Open an issue ][open-an-issue]📛&nbsp;. We will happily discuss your proposed change.  
🐍 &nbsp;_But we should talk before you take a whole lot of time or energy implementing anything._

<br>

## In General

<br>

- Maintainers are happy to review your work and help you.&nbsp;💛&nbsp;💙&nbsp;
  - They may be in a different timezone&nbsp;⌚&nbsp;, or tied up &nbsp;🧶&nbsp; with other tasks.
  - Maintainers will review your request as soon as they are able to.
  - **Please wait at least 72 hours before pinging.**
- If you'd like in-progress feedback or discussion, please mark your Pull Request as a **`[draft]`**
- Pull requests should be focused around a single exercise, issue, or change.
- Pull Request titles and descriptions should make clear **what** has changed and **why**.
  - Please link &nbsp;🔗&nbsp; to any related issues the PR addresses.
- 📛&nbsp;[ Open an issue ][open-an-issue]📛&nbsp; and discuss it with &nbsp;🧰 &nbsp;maintainers _**before**_:
  - creating a Pull Request making significant or breaking changes.
  - for changes across multiple exercises, even if they are typos or small.
  - anything that is going to require doing a lot of work (_on your part or the maintainers part_).
- Follow coding standards found in [PEP8][PEP8] (["For Humans" version here][pep8-for-humans]).
- All files should have a proper [EOL][EOL] at the end. This means one carriage return at the end of the final line of text in files.
- Otherwise, watch out &nbsp;⚠️&nbsp; for trailing spaces, extra blank lines, extra spaces, and spaces in blank lines.
- Continuous Integration is going to run **a lot** of checks on your PR. Pay attention to the failures, try to understand and fix them.
- If you need help, comment in the PR or issue.&nbsp; 🙋🏽‍♀️ &nbsp;  The maintainers are happy to help troubleshoot.

  <details>
    <summary>⚠️&nbsp;&nbsp;<b><em>Pre-Commit Checklist</em></b>&nbsp;⚠️</summary>

1. Run [`configlet-lint`][configlet-lint] if the track [config.json](config-json) has been modified.
2. Run [Prettier][prettier] on all markdown files.
   - (_Optionally_) run [yapf][yapf] to help format your code, and give you a head start on making the linters happy.
3. Run [flake8][flake8] & [pylint][pylint] to ensure all Python code files conform to general code style standards.
4. Run `test/check-exercises.py [EXERCISE]` to check if your test changes function correctly.
5. Run the `example.py` or `exemplar.py` file against the exercise test file to ensure that it passes without error.
6. If you modified or created a `hints.md` file for a practice exercise, [regenerate](#generating-exercise-readmes) it.
  </details>
<br>


## 📄 A Little More on Prose Writing Style and Standards

<br>

Non-code content (_exercise introductions & instructions, hints, concept write-ups, documentation etc._) should be written in [American English][american-english]. We strive to watch [the words we use][the-words-that-we-use].

When a word or phrase usage is contested | ambiguous, we default to what is best understood by our international community of learners, even if it "sounds a little weird"  to a "native" American English speaker.

Our documents use [Markdown][markdown-language], with certain [alterations][exercism-markdown-widgets] & [additions][exercism-internal-linking]. Here is our full [Markdown Specification][exercism-markdown-specification]. &nbsp;📐 We format/lint our Markdown with [Prettier][prettier].&nbsp;✨


<br>

## A Little More on Coding Standards
<br>

1.  We follow [PEP8][PEP8] (["For Humans" version here][pep8-for-humans]).
    In particular, we (mostly) follow the [Google flavor][google-coding-style] of PEP8.
2.  We use [flake8][flake8] to help us format Python code nicely.
    Our `flake8` config file is [.flake8][.flake8] in the top level of this repo.
3.  We use [pylint][pylint] to catch what `flake8` doesn't.
    Our `pylint` config file is [pylintrc][pylintrc] in the top level of this repo.
4.  We use [yapf][yapf] to auto-format our python files.
    Our `.style.yapf` config file is [.style.yapf][.style.yapf] in the top level of this repo.

If you have any questions or issues, don't hesitate to ask the maintainers -- they're always happy to help&nbsp;💛&nbsp;💙&nbsp;

Some of our code is old and does not (yet) conform to all these standards.  We know it, and trust us, we're fixing it. But if you see &nbsp;👀&nbsp; something, &nbsp;👄&nbsp; say something.  It'll motivate us to fix it! 🌈


### General Code Style TL;DR:

- _**spaces**_, never `Tabs`
- **4 space** indentation
- **120 character per line limit** (_as opposed to the Google limit of 79_)
- Variable, function, and method names should be `lower_case_with_underscores` (_aka "snake case"_)
- Classes should be named in `TitleCase` (_aka "camel case"_)
- **No single letter variable names** outside of a `lambda`.  This includes loop variables and comprehensions.
- Refrain from putting `list`, `tuple`, `set`, or `dict` members on their own lines.
  Fit as many data members as can be easily read on one line, before wrapping to a second.
- If a data structure spreads to more than one line and a break (_for clarity_) is needed, prefer breaking after the opening bracket.
- Avoid putting closing brackets on their own lines. Prefer closing a bracket right after the last element.
- Use **`'`** and not **`"`** as the quote character by default.
- Use **`"""`** for docstrings.
- Prefer [implicit line joining][implicit-line-joining] for long strings.
- Prefer enclosing imports in **`()`**, and putting each on their own line when importing multiple methods.
- Two lines between `Classes`, one line between `functions`.  Other vertical whitespace as needed to help readability.
- Always use an **`EOL`** to end a file.


### Concept Exercise Test Files

- We have historically used [Unittest.TestCase][unittest] syntax, with [PyTest][pytest] as a test runner.
- We are transitioning to using (many) more PyTest features and syntax, but are leaving `Unittest` syntax in place where possible.
- Always check with a maintainer before introducing a PyTest feature in your tests.  Not all PyTest features may be supported.
- Test **Classes** should be titled `<ExerciseSlug>Test`. e.g. `class CardGamesTest(unittest.TestCase):`
  This is to help our test runner re-write them for display on the website.
- Test _methods_ or functions should begin with `test_`, and follow PEP8 naming.  Try to make test case names descriptive but not too long.
- Favor [_parameterizing_][distinguishing-test-iterations] tests that vary only by input data. We use [unittest.TestCase.subTest][subtest] for this. An [example from Guido's Gorgeous Lasagna][guidos-gorgeous-lasagna-testfile].  A second [example from Card Games][card-games-testfile].
- Avoid excessive line breaks or indentation - especially in parameterized tests.  Excessive breaks & indentation within the `for` loops cause issues when formatting the test code for display on the website.
- Use [`enumerate()`][enumerate] where possible when looping in test cases. See [Card Games][card-games-testfile] for example usage.
- Favor using variable names like `inputs`, `data`, `input_data`, `test_data`, or `test_case_data` for test inputs.
- Favor using variable names like `results`, `expected`, `result_data`, `expected_data`, `expected_results` or `expected_outputs` for expected test outcomes.
- Favor putting the (not optional) assert failure message on it's own line outside of the `self.assert` method, and naming it `failure_msg`.  See [Card Games][card-games-testfile] for example usage.
- Use `f-strings` over other methods for test failure messages.  Make your messages as relevant and human-readable as possible.
- We relate the test cases for a particular task in an exercise to the **task number** via a custom [PyTest Marker][pytestmark]. These are decorators that take the form of ``@pytest.mark.task(taskno=<task-number-here>)`.  See [Guido's Gorgeous Lasagna][guidos-gorgeous-lasagna-testfile] for an example usage.
- For exercises that have large sets of data for inputs/outputs, we prefer to have **test data files**.  These should be named with `_data` or `_test_data` at the end of the filename, and saved alongside the test case file.  See the [Cater-Waiter][cater-waiter] exercise directory for an example of how we set this up.
- Test data files need to be added to the `editor` key within an exercises [`config.json` `files` key][exercise-config-json].  Check with a maintainer if you have questions or issues.
- For new test files going forward, omit `if __name__ == "__main__":
    unittest.main()`.  `Unittest` will not be able to run these files stand-alone.
- Test files should be linted with both `flake8` and `pylint`.  Both are known to toss false positives for imports and unused variables in test code.  Where necessary, deploy the [`#noqa`][flake8-noqa] or [`#pylint disable=<check-name>`][pylint-disable-check] comments to suppress false-positive warnings.  See **line 16** of [Guido's Gorgeous Lasagna][guidos-gorgeous-lasagna-testfile] test file for an example of a pylint "skip".

<br>

##   🏋️ A Little More on Exercises 🏋🏽‍♀️

- Each exercise must be self-contained. Please do not use or reference files that reside outside the given exercise directory. "Outside" files will not be included if a student fetches the exercise via the CLI.

- Each exercise/problem should include a complete test suite, an example/exemplar solution, and a stub file ready for student implementation.

  - See  [Concept Exercise Anatomy][concept-exercise-anatomy],  or  [Practice Exercise Anatomy][practice-exercise-anatomy] depending on which type of exercise you are contributing to.

  <details>
    <summary>Concept Exercise Checklist</summary>>
  </details>

    <br>

     <details>
        <summary>Practice Exercise Checklist</summary>>
      </details>

- **Practice exercise**, descriptions and instructions come from a centralized, cross-track  [problem specifications][problem-specifications] repository.

  - Any updates or changes need to be proposed/approved in `problem-specifications` first.
  - If Python-specific changes become necessary, they  need to be appended to the canonical instructions by creating a `instructions.append.md` file in this (`exercism/Python`) repository.

- Practice Exercise **Test Suits** for many practice exercises are similarly [auto-generated][##Auto-Generated Test Files and Test Templates] from data in [problem specifications][problem-specifications].
  - Any changes to them need to be proposed/discussed in the `problem-specifications` repository and approved by **3 track maintainers**, since changes could potentially affect many (_or all_) exercism language tracks.
  - If Python-specific test changes become necessary, they can be appended to the exercise `tests.toml` file.
  - 📛&nbsp;[ **Please file an issue**][open-an-issue]&nbsp;📛 &nbsp;and check with maintainers before adding any Python-specific tests.


<br>


## Python Versions

<br>

This track officially supports Python = `3.8`  The track `test runner`, `analyzer`, and `representer` run in docker on `python:3.9-slim`.

Although the majority of test cases are written using `unittest.TestCase`,

*  All exercises should be written for compatibility with Python = `3.8` or `3.9`.
*  Version backward _incompatibility_ (*e.g* an exercise using a `3.8` or `3.9` **only** feature)  should be clearly noted in any exercise hits, links, introductions or other notes.

*  Here is an example of how the Python documentation handles [version-tagged &nbsp;🏷&nbsp;][version-tagged-language-features] feature introduction.

* _Most_ exercises will work with Python `3.6+`, and _many_ are compatible with Python `2.7+`. Please do not change existing exercises to add new language features without consulting with a maintainer first. We &nbsp;💛&nbsp;💙&nbsp; modern Python, but we _also_ want to avoid student confusion when it comes to which Python versions support brand-new features.

- All test suites and example solutions must work in all Python versions that we currently support. When in doubt about a feature, please check with maintainers.

<br>

## External Libraries and Dependencies

Our tooling (_runners, analyzers and representers_) runs in isolated containers within the exercism website.  Because of this, exercises cannot rely on third-party or external libraries.  Any library needed for an exercise or exercise tests must be incorporated as part of the tooling build, and noted for students who are using the CLI to solve problems locally.

If your exercise depends on a third-party library (_aka not part of standard Python_), please consult with maintainers about it.  We may or may not be able to accommodate the package.

<br>

## Auto-Generated Test Files and Test Templates

<br>

[**Practice exercises**][practice-exercise-files] inherit their definitions from the [problem-specifications][problem-specifications] repository in the form of _description files_.  Exercise introductions, instructions and (_in the case of **many**, but not **all**_) test files are then machine-generated for each language track.

Changes to practice exercise _specifications_ should be raised/PR'd in  [problem-specifications][problem-specifications] and approved by **3 track maintainers**. After an exercise change has gone through that process , related documents and tests for the Python track will need to be [re-generated](#generating-practice-exercise-documents) via [configlet][configlet]. Configlet is also used as part of the track CI, essential track and exercise linting, and other verification tasks.

If a practice exercise has an auto-generated `<exercise_slug>_test.py` file, there will be a  `.meta/template.j2` and a `.meta/tests.toml` file  in the exercise directory. If an exercise implements  Python track-specific tests, there may be a `.meta/additional_tests.json` to define them. These `additional_tests.json` files will automatically be included in test generation.

Practice exercise `<exercise_slug>_test.py` files are  generated/regenerated via the [Python Track Test Generator][python-track-test-generator]. Please reach out to a maintainer if you need any help with the process.

<br>

### Python Practice Exercise structure for auto-generated tests

```Bash
[<exercise-slug>/
├── .docs
│   └── instructions.md
├── .meta
│   ├── config.json
│   ├── example.py
│   ├── template.j2
│   └── tests.toml
├── <exercise_slug>.py #stub file
└── <exercise_slug_test.py #test file
```

## Generating Practice Exercise Documents

**You will need:**
- A local clone of the [problem-specifications] repository.
- [configlet]

**Regenerating all Practice Exercise Documents:**

```
configlet generate <path/to/track> --spec-path path/to/problem/specifications
```

**Regenerating an Individual Exercises Documents:**

```
configlet generate <path/to/track> --spec-path path/to/problem/specifications --only example-exercise
```

### Implementing Practice Exercise Tests

If an unimplemented exercise has a `canonical-data.json` file in the [problem-specifications] repository, a generation template must be created. See the Python track [test generator documentation][python-track-test-generator] for more information.

If an unimplemented exercise does not have a `canonical-data.json` file, the test file must be written manually.

### Practice Exercise Example solutions

Example solution files serve two purposes:

1. Verification of the tests
2. Example implementation for mentor/student reference

Unlike concept exercise, practice exercise `example.py` files are NOT intended as as a "best practice" or "standard".  They are provided as proof that there is an acceptable and testable answer to the practice exercise.


## Implementing Track-specific Practice Exercises

Similar to implementing a canonical exercise that has no `canonical-data.json`, but the exercise documents will also need to be written manually. Carefully follow the structure of generated exercise documents and the [exercism practice exercise specification][practice-exercises].


[.flake8]: https://github.com/exercism/python/blob/main/.flake8
[EOL]: https://en.wikipedia.org/wiki/Newline
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[american-english]: https://github.com/exercism/docs/blob/main/building/markdown/style-guide.md
[being-a-good-community-member]: https://github.com/exercism/docs/tree/main/community/good-member
[cater-waiter]: https://github.com/exercism/python/tree/main/exercises/concept/cater-waiter
[card-games-testfile]: https://github.com/exercism/python/blob/main/exercises/concept/card-games/lists_test.py
[concept-exercise-anatomy]: https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md
[concept-exercises]: https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md
[config-json]: https://github.com/exercism/javascript/blob/main/config.json
[configlet-general]: https://github.com/exercism/configlet
[configlet]: https://github.com/exercism/docs/blob/main/building/configlet/generating-documents.md
[configlet-lint]: https://github.com/exercism/configlet#configlet-lint
[distinguishing-test-iterations]: https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests
[enumerate]: https://docs.python.org/3/library/functions.html#enumerate
[exercise-config-json]: https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md#full-example
[exercise-presentation]: https://github.com/exercism/docs/blob/main/building/tracks/presentation.md
[exercism-admins]: https://github.com/exercism/docs/blob/main/community/administrators.md
[exercism-code-of-conduct]: https://exercism.org/docs/using/legal/code-of-conduct
[exercism-concepts]: https://github.com/exercism/docs/blob/main/building/tracks/concepts.md
[exercism-contributors]: https://github.com/exercism/docs/blob/main/community/contributors.md
[exercism-internal-linking]: https://github.com/exercism/docs/blob/main/building/markdown/internal-linking.md
[exercism-markdown-specification]: https://github.com/exercism/docs/blob/main/building/markdown/markdown.md
[exercism-markdown-widgets]: https://github.com/exercism/docs/blob/main/building/markdown/widgets.md
[exercism-mentors]: https://github.com/exercism/docs/tree/main/mentoring
[exercism-tasks]: https://exercism.org/docs/building/product/tasks
[exercism-track-maintainers]: https://github.com/exercism/docs/blob/main/community/maintainers.md
[exercism-track-structure]: https://github.com/exercism/docs/tree/main/building/tracks
[exercism-website]: https://exercism.org/
[exercism-writing-style]: https://github.com/exercism/docs/blob/main/building/markdown/style-guide.md
[flake8]: http://flake8.pycqa.org/
[flake8-noqa]: https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html#in-line-ignoring-errors
[google-coding-style]: https://google.github.io/styleguide/pyguide.html
[guidos-gorgeous-lasagna-testfile]: https://github.com/exercism/python/blob/main/exercises/concept/guidos-gorgeous-lasagna/lasagna_test.py
[help-wanted]: https://github.com/exercism/python/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22
[implicit-line-joining]: https://google.github.io/styleguide/pyguide.html#32-line-length
[markdown-language]: https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
[open-an-issue]: https://github.com/exercism/python/issues/new/choose
[pep8-for-humans]: https://pep8.org/
[practice-exercise-anatomy]: https://github.com/exercism/docs/blob/main/building/tracks/practice-exercises.md
[practice-exercise-files]: https://github.com/exercism/docs/blob/main/building/tracks/practice-exercises.md#exercise-files
[practice-exercises]: https://github.com/exercism/docs/blob/main/building/tracks/practice-exercises.md
[prettier]: https://prettier.io/
[problem-specifications]: https://github.com/exercism/problem-specifications
[pylint]: https://pylint.pycqa.org/en/v2.11.1/user_guide/index.html
[pylintrc]: https://github.com/exercism/python/blob/main/pylintrc
[pylint-disable-check]: https://pylint.pycqa.org/en/latest/user_guide/message-control.html#block-disables
[pytest]: https://docs.pytest.org/en/6.2.x/contents.html
[pytestmark]: https://docs.pytest.org/en/6.2.x/example/markers.html
[python-syllabus]: https://exercism.org/tracks/python/concepts
[python-track-test-generator]: https://github.com/exercism/python/blob/main/docs/GENERATOR.md
[.style.yapf]: https://github.com/exercism/python/blob/main/.style.yapf
[subtest]: https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest
[the-words-that-we-use]: https://github.com/exercism/docs/blob/main/community/good-member/words.md
[unittest]: https://docs.python.org/3/library/unittest.html#unittest.TestCase
[version-tagged-language-features]: https://docs.python.org/3/library/stdtypes.html#dict.popitem
[website-contributing-section]: https://exercism.org/docs/building
[yapf]: https://github.com/google/yapf
