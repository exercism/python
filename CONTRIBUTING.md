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

<img align="left" width="100" height="90" src="https://github.com/exercism/website-icons/blob/main/exercism/logo-big-bordered.png">

🌟🌟&nbsp; If you have not already done so, please take a moment to read our [Code of Conduct][exercism-code-of-conduct].&nbsp;🌟🌟&nbsp;  
It might also be helpful to look at [Being a Good Community Member][being-a-good-community-member] & [The words that we use][the-words-that-we-use].

Some defined roles in our community:  [Contributors][exercism-contributors] **|** [Mentors][exercism-mentors] **|** [Maintainers][exercism-track-maintainers]  **|** [Admins][exercism-admins]

<br>
<img align="left" width="85" height="80" src="https://github.com/exercism/website-icons/blob/main/exercises/word-search.svg">

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
<img align="left" width="90" height="80" src="https://github.com/exercism/website-icons/blob/main/exercises/hello-world.svg">
<p vertical-align="middle"><h2>In General</h2></p>
<br>

- Maintainers are happy to review your work and help troubleshoot with you.&nbsp;💛&nbsp;💙&nbsp;
  - Requests are reviewed as soon as is practical/possible.
  - (❗&nbsp;) Reviewers may be in a different timezone&nbsp;⌚&nbsp;, or tied up &nbsp;🧶&nbsp; with other tasks.
  - **Please wait at least 72 hours before pinging.**
- If you need help, comment in the Pull Request/issue.&nbsp; 🙋🏽‍♀️ &nbsp;
- If you would like in-progress feedback/discussion, please mark your Pull Request as a **`[draft]`**
- Pull Requests should be focused around a single exercise, issue, or change.
- Pull Request titles and descriptions should make clear **what** has changed and **why**.
  - Please link &nbsp;🔗&nbsp; to any related issues the PR addresses.
- 📛&nbsp;[ Open an issue ][open-an-issue]📛&nbsp; and discuss it with &nbsp;🧰 &nbsp;maintainers _**before**_:
  - creating a Pull Request making significant or breaking changes.
  - for changes across multiple exercises, even if they are typos or small.
  - anything that is going to require doing a lot of work (_on your part or the maintainers part_).
- Follow coding standards found in [PEP8][PEP8] (["For Humans" version here][pep8-for-humans]).
- All files should have a proper [EOL][EOL]. This means one carriage return at the end of the final line of text files.
- Otherwise, watch out &nbsp;⚠️&nbsp; for trailing spaces, extra blank lines, extra spaces, and spaces in blank lines.
- Continuous Integration is going to run **a lot** of checks. Try to understand & fix any failures.

<br>
  <details>
    <summary>⚠️&nbsp;&nbsp;<b><em>Pre-Commit Checklist</em></b>&nbsp;⚠️</summary>
    <br>

   1.  &nbsp;Run [`configlet-lint`][configlet-lint] if the track [config.json](config-json) has been modified.
   2.  &nbsp;Run [Prettier][prettier] on all markdown files.
       - (_Optionally_) run [yapf][yapf] ([_config file_][.style.yapf]) to help format your code, and give you a head start on making the linters happy.
   3.  &nbsp;Run [flake8][flake8] ([_config file_][.flake8]) & [pylint][pylint] ([_config file_][pylintrc]) to ensure all Python code files conform to general code style standards.
   4.  &nbsp;Run `test/check-exercises.py [EXERCISE]` to check if your test changes function correctly.
   5.  &nbsp;Run the `example.py` or `exemplar.py` file against the exercise test file to ensure that it passes without error.
   6.  &nbsp;If you modified or created a `hints.md` file for a practice exercise, [regenerate](#generating-practice-exercise-documents) it.

  </details>
<br>

<img align="left" width="90" height="80" src="https://github.com/exercism/website-icons/blob/main/exercism/logo-big-bordered.png">
<p vertical-align="middle"><h2 id="prose-writing-style-and-standards">Prose Writing Style and Standards</h2></p>

<br>

Non-code content (_exercise introductions & instructions, hints, concept write-ups, documentation etc._) should be written in [American English][american-english].
We strive to watch [the words we use][the-words-that-we-use].

When a word or phrase usage is contested/ambiguous, we default to what is best understood by our international community of learners, even if it "sounds a little weird" to a "native" American English speaker.

Our documents use [Markdown][markdown-language], with certain [alterations][exercism-markdown-widgets] & [additions][exercism-internal-linking]. Here is our full [Markdown Specification][exercism-markdown-specification]. &nbsp;📐 We format/lint our Markdown with [Prettier][prettier].&nbsp;✨


<br>
<img align="left" width="70" height="65" src="https://github.com/exercism/website-icons/blob/main/tracks/python.svg">
<p vertical-align="middle"><h2 id="coding-standards">Coding Standards</h2></p>

<br>

1.  We follow [PEP8][PEP8] (["For Humans" version here][pep8-for-humans]).
    In particular, we (mostly) follow the [Google flavor][google-coding-style] of PEP8.
2.  We use [flake8][flake8] to help us format Python code nicely.
    Our `flake8` config file is [.flake8][.flake8] in the top level of this repo.
3.  We use [pylint][pylint] to catch what `flake8` doesn't.
    Our `pylint` config file is [pylintrc][pylintrc] in the top level of this repo.
4.  We use [yapf][yapf] to auto-format our python files.
    Our `.style.yapf` config file is [.style.yapf][.style.yapf] in the top level of this repo.

<br>

<details>
    <summary>General Code Style Summary</summary>
<br>

- _**spaces**_, never `Tabs`
- **4 space** indentation
- **120 character per line limit** (_as opposed to the default limit of 79_)
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

 </details>

<details>
    <summary>Test File Style (<em>concept exercises</em>)</summary>
<br>

- [Unittest.TestCase][unittest] syntax, with [PyTest][pytest] as a test runner.
  - We are transitioning to using more PyTest features/syntax, but are leaving `Unittest` syntax in place where possible.
  - Always check with a maintainer before introducing a PyTest feature into your tests.
- Test **Classes** should be titled `<ExerciseSlug>Test`. **e.g.** `class CardGamesTest(unittest.TestCase):`
- Test method names should begin with `test_`.  Try to make test case names descriptive but not too long.
- Favor [_parameterizing_][distinguishing-test-iterations] tests that only vary input data. Use [unittest.TestCase.subTest][subtest] for parameterization.
  - An [example from Guido's Gorgeous Lasagna][guidos-gorgeous-lasagna-testfile].
  - A second [example from Card Games][card-games-testfile].
- Avoid excessive line breaks or indentation - particularly in parameterized tests.
  - Excessive breaks & indentation within the `for` loops cause issues when formatting the test code for display on the website.
- Use [`enumerate()`][enumerate] where possible when indexes are needed. See [Card Games][card-games-testfile] for example usage.
- Favor using names like `inputs`, `data`, `input_data`, `test_data`, or `test_case_data` for test inputs.
- Favor using names like `results`, `expected`, `result_data`, `expected_data`, or `expected_results` for test outcomes.
- Favor putting the assert failure message outside of `self.assert()`. Name it `failure_msg`.  See [Card Games][card-games-testfile] for example usage.
- Favor `f-strings` for dynamic failure messages.  Please make your error messages as relevant and human-readable as possible.
- We relate test cases to **task number** via a custom [PyTest Marker][pytestmark].
  - These take the form of `@pytest.mark.task(taskno=<task-number-here>)`. See [Guido's Gorgeous Lasagna][guidos-gorgeous-lasagna-testfile] for an example.
- We prefer **test data files** when test inputs/outputs are verbose.
  - These should be named with `_data` or `_test_data` at the end of the filename, and saved alongside the test case file.
  - See the [Cater-Waiter][cater-waiter] exercise directory for an example of this setup.
  - **Test data files** need to be added under an `editor` key within [`config.json "files"`][exercise-config-json].
  - Check with a maintainer if you have questions or issues, or need help with an exercise `config.json`.
- For new test files going forward, omit `if __name__ == "__main__":
    unittest.main()`.
- Lint with both `flake8` and `pylint`.
  - Both linters are known to toss false-positives for some testing patterns.
  - Where necessary, deploy the [`#noqa`][flake8-noqa] or [`#pylint disable=<check-name>`][pylint-disable-check] comments to suppress false-positive warnings.   - See **line 16** of [Guido's Gorgeous Lasagna][guidos-gorgeous-lasagna-testfile] test file for an example of an override.

 </details>
 <br>

If you have any questions or issues, don't hesitate to ask the maintainers -- they're always happy to help&nbsp;💛&nbsp;💙&nbsp;

Some of our code is old and does not (yet) conform to all these standards.  
_**We know it, and trust us, we are working on fixing it.**_ But if you see &nbsp;👀&nbsp; something, &nbsp;👄&nbsp; say something. It will motivate us to fix it! 🌈

 <br>

<img align="left" width="70" height="65" src="https://github.com/exercism/website-icons/blob/main/tracks/python.svg">
<p vertical-align="middle"><h2>Python Versions</h2></p>

<br>

This track officially supports Python = `3.8`  
The track `test runner`, `analyzer`, and `representer` run in docker on `python:3.9-slim`.

-  All exercises should be written for compatibility with Python = `3.8` or `3.9`.
-  Version backward _incompatibility_ (*e.g* an exercise using a `3.8` or `3.9` **only** feature)  should be clearly noted in any exercise hits, links, introductions or other notes.

-  Here is an example of how the Python documentation handles [version-tagged &nbsp;🏷&nbsp;][version-tagged-language-features] feature introduction.

- _Most_ exercises will work with Python `3.6+`, and _many_ are compatible with Python `2.7+`.
  - Please do not change existing exercises to add new language features without consulting with a maintainer first.
  - We &nbsp;💛&nbsp;💙&nbsp; modern Python, but we _also_ want to avoid student confusion when it comes to which Python versions support brand-new features.

- All test suites and example solutions must work in all Python versions that we currently support. When in doubt about a feature, please check with maintainers.

<br>

<br>

<img align="left" width="80" height="80" src="https://github.com/exercism/website-icons/blob/main/exercises/developer-privileges.svg">
<p vertical-align="middle"><h2>A Little More on Exercises</h2></p>

<br>

- Each exercise must be self-contained. Please do not use or reference files that reside outside the given exercise directory. "Outside" files will not be included if a student fetches the exercise via the Command line Interface.

- Each exercise/problem should include
  - a complete test suite,
  - an example/exemplar solution,
  - a stub file ready for student implementation.

- For specifications, refer to the links below, depending on which type of exercise you are contributing to.
  - [Concept Exercise Anatomy][concept-exercise-anatomy]
  - [Practice Exercise Anatomy][practice-exercise-anatomy]

- **Practice exercise**, descriptions and instructions come from a centralized, cross-track  [problem specifications][problem-specifications] repository.
  - Any updates or changes need to be proposed/approved in `problem-specifications` first.
  - If Python-specific changes become necessary, they  need to be appended to the canonical instructions by creating a `instructions.append.md` file in this (`exercism/Python`) repository.

- Practice Exercise **Test Suits** for many practice exercises are similarly [auto-generated](#auto-generated-files) from data in [problem specifications][problem-specifications].
  - Any changes to them need to be proposed/discussed in the `problem-specifications` repository and approved by **3 track maintainers**, since changes could potentially affect many (_or all_) exercism language tracks.
  - If Python-specific test changes become necessary, they can be appended to the exercise `tests.toml` file.
  - 📛&nbsp;[ **Please file an issue**][open-an-issue]&nbsp;📛 &nbsp;and check with maintainers before adding any Python-specific tests.

  <br>
  <br>
  <details>
    <summary>
     ✅&nbsp;&nbsp;&nbsp;Concept Exercise Checklist
   </summary>
   <br>

   - [ ] `.docs/hints.md`
   - [ ] `.docs/instructions.md`
   - [ ] `.docs/introduction.md`
   - [ ] `.meta/config.json`
   - [ ] `.meta/design.md`
   - [ ] `.meta/exemplar.py` (_exemplar solution_)
   - [ ] `<exercise-slug>_test.py` (_test file_)
   - [ ] `<exercise-slug>.py` (_stub file_)
   - [ ] `concepts/../introduction.md`
   - [ ] `concepts/../about.md`
   - [ ] `concepts/../links.json`
   - [ ] `concepts/../.meta/config.json`

  </details>

  <details>
   <summary>
    ✅&nbsp;&nbsp;&nbsp;Practice Exercise Checklist
   </summary>
   <br>

   - [ ] `.docs/instructions.md`(**required**)
   - [ ] `.docs/introduction.md`(_optional_)
   - [ ] `.docs/introduction.append.md`(_optional_)
   - [ ] `.docs/instructions.append.md` (_optional_)
   - [ ] `.docs/hints.md`(_optional_)
   - [ ] `.meta/config.json` (**required**)
   - [ ] `.meta/example.py` (**required**)
   - [ ] `.meta/design.md` (_optional_)
   - [ ] `.meta/template.j2` (_template for generating tests from canonical data_)
   - [ ] `.meta/tests.toml` (_tests configuration from canonical data_)
   - [ ] `<exercise-slug>_test.py` (_**auto-generated from canonical data**_)
   - [ ] `<exercise-slug>.py` (**required**)

  </details>


<br>


<br>
<img align="left" width="80" height="80" src="https://github.com/exercism/website-icons/blob/main/exercises/anagrams.svg">
<p vertical-align="middle"><h2>External Libraries and Dependencies</h2></p>

<br>

Our tooling (_runners, representers, and analyzers_) runs in isolated containers within the exercism website.  Because of this isolation, exercises cannot rely on third-party or external libraries.  Any library needed for an exercise or exercise tests must be incorporated as part of a tooling build, and noted for students who are using the CLI to solve problems locally.

If your exercise depends on a third-party library (_aka not part of standard Python_), please consult with maintainers about it.  We may or may not be able to accommodate the package.

<br>
<img id="auto-generated-files" align="left" width="85" height="80" src="https://github.com/exercism/website-icons/blob/main/exercises/forth.svg">
<p vertical-align="middle"><h2>Auto-Generated Test Files and Test Templates</h2></p>

<br>

[**Practice exercises**][practice-exercise-files] inherit their definitions from the [problem-specifications][problem-specifications] repository in the form of _description files_.  Exercise introductions, instructions and (_in the case of **many**, but not **all**_) test files are then machine-generated for each language track.

Changes to practice exercise _specifications_ should be raised/PR'd in  [problem-specifications][problem-specifications] and approved by **3 track maintainers**. After an exercise change has gone through that process , related documents and tests for the Python track will need to be [re-generated](#generating-practice-exercise-documents) via [configlet][configlet]. Configlet is also used as part of the track CI, essential track and exercise linting, and other verification tasks.

If a practice exercise has an auto-generated `<exercise_slug>_test.py` file, there will be a  `.meta/template.j2` and a `.meta/tests.toml` file  in the exercise directory. If an exercise implements  Python track-specific tests, there may be a `.meta/additional_tests.json` to define them. These `additional_tests.json` files will automatically be included in test generation.

_Exercise Structure with Auto-Generated Test Files_

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
<br>

Practice exercise `<exercise_slug>_test.py` files are  generated/regenerated via the [Python Track Test Generator][python-track-test-generator].  
Please reach out to a maintainer if you need any help with the process.

<br>
<img id="implementing-practice-exercise-tests" align="left" width="75" height="75" src="https://github.com/exercism/website-icons/blob/main/exercises/equilateral-triangle.svg">
<p vertical-align="middle"><h2>Implementing Practice Exercise Tests</h2></p>
<br>

If an unimplemented exercise has a `canonical-data.json` file in the [problem-specifications] repository, a generation template must be created. See the Python track [test generator documentation][python-track-test-generator] for more information.

If an unimplemented exercise does not have a `canonical-data.json` file, the test file must be written manually.

<br>
<img id="practice-exercise-example-solutions" align="left" width="75" height="75" src="https://github.com/exercism/website-icons/blob/main/exercises/character-study.svg">
<p vertical-align="middle"><h2>Implementing Practice Exercise Example Solutions</h2></p>
<br>

**Example solution files serve two purposes only:**
1. Verification of the tests
2. Example implementation for mentor/student reference

Unlike `concept` exercise, practice exercise `example.py` files are **NOT** intended as as a "best practice" or "standard".  
They are provided as proof that there is an acceptable and testable answer to the practice exercise.

<br>
<img id="implementing-track-specific-practice-exercises" align="left" width="75" height="75" src="https://github.com/exercism/website-icons/blob/main/exercises/darts.svg">
<p vertical-align="middle"><h2>Implementing Track-specific Practice Exercises</h2></p>
<br>

Implementing Track-specific Practice Exercises is similar to implementing a `canonical` exercise that has no `canonical-data.json`. But in addition to the tests, the exercise documents (_instructions, etc._) will also need to be written manually. Carefully follow the structure of generated exercise documents and the [exercism practice exercise specification][practice-exercises].

<br>

<p verticle-align="middle"><img id="generating-practice-exercise-documents" align="left" width="70" height="70" src="https://github.com/exercism/website-icons/blob/main/exercises/rest-api.svg"><h2>Generating Practice Exercise Documents</h2></p>
<br>
<b>You will need</b>

1.&nbsp;&nbsp;A local clone of the [problem-specifications] repository.  
2.&nbsp;&nbsp;[configlet]

<p><b>For Individual Exercises</b><p><img id="regenerating-individual-exercise-documents" align="left" width="45" height="45" src="https://github.com/exercism/website-icons/blob/main/exercises/doubly-linked-list.svg"></p>

```bash
configlet generate <path/to/track> --spec-path path/to/problem/specifications --only example-exercise
```
<p><b>For all Practice Exercises</b><p><img id="regenerating-all-practice-exercise-documents" align="left" width="45" height="45" src="https://github.com/exercism/website-icons/blob/main/exercises/doubly-linked-list.svg"></p>

```bash
configlet generate <path/to/track> --spec-path path/to/problem/specifications
```

<br>


[.flake8]: https://github.com/exercism/python/blob/main/.flake8
[.style.yapf]: https://github.com/exercism/python/blob/main/.style.yapf
[EOL]: https://en.wikipedia.org/wiki/Newline
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[american-english]: https://github.com/exercism/docs/blob/main/building/markdown/style-guide.md
[being-a-good-community-member]: https://github.com/exercism/docs/tree/main/community/good-member
[card-games-testfile]: https://github.com/exercism/python/blob/main/exercises/concept/card-games/lists_test.py
[cater-waiter]: https://github.com/exercism/python/tree/main/exercises/concept/cater-waiter
[concept-exercise-anatomy]: https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md
[concept-exercises]: https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md
[config-json]: https://github.com/exercism/javascript/blob/main/config.json
[configlet-lint]: https://github.com/exercism/configlet#configlet-lint
[configlet]: https://github.com/exercism/docs/blob/main/building/configlet/generating-documents.md
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
[flake8-noqa]: https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html#in-line-ignoring-errors
[flake8]: http://flake8.pycqa.org/
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
[pylint-disable-check]: https://pylint.pycqa.org/en/latest/user_guide/message-control.html#block-disables
[pylint]: https://pylint.pycqa.org/en/v2.11.1/user_guide/index.html
[pylintrc]: https://github.com/exercism/python/blob/main/pylintrc
[pytest]: https://docs.pytest.org/en/6.2.x/contents.html
[pytestmark]: https://docs.pytest.org/en/6.2.x/example/markers.html
[python-syllabus]: https://exercism.org/tracks/python/concepts
[python-track-test-generator]: https://github.com/exercism/python/blob/main/docs/GENERATOR.md
[subtest]: https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest
[the-words-that-we-use]: https://github.com/exercism/docs/blob/main/community/good-member/words.md
[unittest]: https://docs.python.org/3/library/unittest.html#unittest.TestCase
[version-tagged-language-features]: https://docs.python.org/3/library/stdtypes.html#dict.popitem
[website-contributing-section]: https://exercism.org/docs/building
[yapf]: https://github.com/google/yapf
