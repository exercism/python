#  Contributing

Hi. &nbsp;👋🏽 &nbsp;👋 &nbsp; 

Thank you so much for your interest in contributing to the Python track!  **We are happy you are here.** 🌟 &nbsp; 🎉


`exercsim/Python` is  one of the many tracks on [exercism][exercism-website]. This repo holds all the instructions, tests, code, & support files for Python *exercises* currently under development or implemented & available for students.

Exercises are grouped into **concept** exercises which teach the [Python syllabus][python-syllabus], and **practice** exercises, which are unlocked by progressing in the syllabus tree. Concept exercises are constrained to a small set of language or syntax features. Practice exercises are open-ended, and can be used to practice concepts learned, try out new techniques, and _play_.  These two exercise groupings can be found in the track [config.json][config-json], and under the `python/exercises` directory.

<br>

## 🐛 **Did you find a bug?**

It's not uncommon that people discover typos, confusing directions, or incorrect implementations of  certain tests or code examples.  Or you might have a great suggestion for a hint to aid students (💙 &nbsp;) ,  see optimizations for exemplar or test code, find missing test cases to add, or want to correct factual and/or logical errors.  Or maybe you have a great idea for an exercise or feature (&nbsp;❗&nbsp;).

_Our track is always a work in progress!_ 🌟🌟   
Please  📛 &nbsp;[Open an issue][open-an-issue]&nbsp;📛 , and let us know what you have found or suggest.

<br>

## 🚧  **Did you write a patch that fixes a bug?**

 💛 💙&nbsp; **We Warmly Welcome Pull Requests that are:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1️⃣  &nbsp;&nbsp;&nbsp; Small, contained fixes for typos/grammar/punctuation/code syntax on [one] exercise,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2️⃣&nbsp;&nbsp;&nbsp;&nbsp; Medium changes that have been agreed/discussed via a filed issue,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3️⃣ &nbsp;&nbsp;&nbsp;&nbsp;Contributions from our [help wanted][help-wanted] issue list,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4️⃣ &nbsp;&nbsp;&nbsp;&nbsp;Larger (_and previously agreed-upon_) contributions from recent & regular (_within the last 6 months_) contributors.

When in doubt, 📛 &nbsp;[Open an issue][open-an-issue]&nbsp;📛. We will happily discuss your proposed change. 🐍

But let's talk before you take a whole lot of time or energy implementing anything.

<br>

## :books:  **Want to jump directly into Exercism specifications & detail?**

✨&nbsp;🦄&nbsp; Here is the good stuff:

[Track Structure][exercism-track-structure] **|** [Tasks][exercism-tasks] **|** [Concepts][exercism-concepts] **|** [Concept Exercises][concept-exercises] **|** [Practice Exercises][practice-exercises]  **|** [Presentation][exercise-presentation] **|** [Writing Style Guide][exercism-writing-style] **|** [Markdown Specification][exercism-markdown-specification]

Web-formatted &nbsp;🕸️ &nbsp; versions are available in the [contributing section][website-contributing-section] of exercsim.org.

<br>

## 🌍 &nbsp; The Exercism Community &nbsp; 🌏

<br>

🌟🌟&nbsp; If you have not already done so, please take a moment to read our [Code of Conduct][exercism-code-of-conduct] & [Being a Good Community Member][being-a-good-community-member] documents.
It might also be helpful to take a look at [The words that we use][the-words-that-we-use].


Some defined roles in our community:  [Community Member][being-a-good-community-member] **|**  [Contributors][exercism-contributors] **|** [Mentors][exercism-mentors] **|** [Maintainers][exercism-track-maintainers]  **|** [Admins][exercism-admins]

<br>

## In General

<br>

- Maintainers are happy to review your work and help you.&nbsp;💛&nbsp;💙&nbsp;
  - They may be in a different timezone&nbsp;⌚&nbsp;, or tied up &nbsp;🧶&nbsp; with other tasks. They will review your request as soon as they are able to.
  - **Please wait at least 72 hours before pinging.**
- If you'd like in-progress feedback or discussion, please mark your Pull Request as a `[draft]`
- Pull requests should be focused on a single exercise, issue, or change.
- Pull Request titles and descriptions should make clear **what** has changed and **why**.
  - Please link &nbsp;🔗&nbsp; to any related issues the PR addresses.
- 📛&nbsp;[Open an issue][open-an-issue]&nbsp;📛&nbsp;&nbsp; and discussed  _**before**_ creating a Pull Request making significant or breaking changes to an existing exercise.
  - The same rule holds true for changes across multiple exercises.
  - It is best to discuss changes with &nbsp;🧰 &nbsp;maintainers before doing a lot of work.
- Follow coding standards found in [PEP8][PEP8] (["For Humans" version here][pep8-for-humans]).
  - We do have some more specific requirements.  More on that a little later.
- All files should have a proper [EOL][EOL] at the end. This means one carriage return at the end of the final line of text in files.
- Otherwise, watch out &nbsp;⚠️&nbsp; for trailing spaces, extra blank lines, extra spaces, and spaces in blank lines.
- The CI is going to run **a lot** of checks on your PR. Pay attention to the failures, try to understand and fix them.
  - If you need help, comment in the PR or issue.&nbsp; 🙋🏽‍♀️ &nbsp;  The maintainers are happy to help troubleshoot.


&nbsp;⚠️&nbsp;&nbsp;**Before committing**&nbsp;⚠️&nbsp;

- Run `configlet fmt` and `configlet lint` if the track [config.json](config-json) has been modified.
- Run [Prettier][prettier] on all markdown files.
- Run [flake8][flake8] to ensure all Python code files conform to general code style standards.
- Run [???] to help format your code
- Run `test/check-exercises.py [EXERCISE]` to check if your test changes function correctly.
- Run the `example.py` or `exemplar.py` file against the test file to ensure that it passes without error.
- If you modified or created a `hints.md` file for a practice exercise, [regenerate](#generating-exercise-readmes) it.

<br>

## 📄 A Little More on Prose Writing Style and Standards

<br>

Non-code content (_exercise introductions & instructions, hints, concept write-ups, documentation etc._) should be written in [American English][american-english]. We strive to watch [the words we use][the-words-that-we-use].

When a word or phrase usage is contested | ambiguous, we default to what is best understood by our international community of learners, even if it "sounds a little weird"  to a "native" American English speaker.

Our documents use [Markdown][markdown-language], with certain [alterations][exercism-markdown-widgets] & [additions][exercism-internal-linking]. Here is our full [Markdown Specification][exercism-markdown-specification]. &nbsp;📐 We format/lint our Markdown with [Prettier][prettier].&nbsp;✨


<br>

##  Little More on Coding Standards
<br>


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
  - If Python-specific test changes become necessary, they can be appended to the exercise `tests.toml` file.   📛&nbsp;[**Please file an issue**][open-an-issue]&nbsp;📛 &nbsp; and check with maintainers before adding any Python-specific tests.


<br>


<br>

## Python Versions

<br>

This track officially supports Python >= `3.8`  The track `test runner`, `analyzer`, and `representer` run in docker on `python:3.9-slim`.

Although the majority of test cases are written using `unittest.TestCase`,

*  All exercises should be written for compatibility with Python >= `3.8`,.
*  Version backward _incompatibility_ (*e.g* an exercise using a `3.8` or `3.9` **only** feature)  should be clearly noted in any exercise introduction or notes.

* _Most_ exercises will work with Python `3.6+`, and _many_ are compatible with Python 2.7+.   Please do not change existing exercises to add new `3.6`+ features without consulting with a maintainer first.

- All test suites and example solutions must work in all Python versions that we currently support. When in doubt about a feature, please check with maintainers.

<br>

## External Libraries and Dependencies

<br>
<br>



## Auto-Generated Test Files and Test Templates

<br>

Practice exericses  inherit their definitions from the [problem-specifications][problem-specifications] repository in the form of _description files_.  Exercise introductions, instructions and (_in the case of **many**, but not **all**_) test files are machine-generated .

Changes to practice exercise _specifications_ should be raised/PR'd in  [problem-specifications][problem-specifications] and approved by **3 track maintainers**. After an exercise change has gone through that process , related documents and tests for the Python track will need to be re-generated via [configlet][configlet]. Configlet is also used as part of the track CI, essential track and exercise linting, and other verification tasks.

If a practice exercise has an auto-generated `<exercise>_test.py` file, there will be a  `.meta/template.j2` and a `.meta/tests.toml` file  in the exercise directory. If an exercise implements  Python track-specific tests, there may be a `.meta/additional_tests.json` to define them. These `additional_tests.json` files will automatically be included in test generation.

Practice exercise  `<exercise>_test.py` files are  generated/regenerated via the [Python Track Test Generator][python-track-test-generator]. Please reach out to a maintainer if you need any help with the process.

<br>

## Tools and Tooling


##################################


## Architecture

Exercism tracks inherit exercise definitions from the [problem-specifications] repository in the form of description files
(from which exercise READMEs are [generated](#generating-exercise-readmes))


## Implementing an exercise

### Exercise structure

```Bash
exercises/[EXERCISE]/
├── [EXERCISE].py
├── [EXERCISE]_test.py
├── example.py
├── .meta
│   ├── template.j2
│   ├── additional_tests.json
│   └── hints.md
└── README.md
```

Files:

| File | Description | Source |
|:--- |:--- |:--- |
| [[EXERCISE].py](exercises/two-fer/two_fer.py) | Solution stub  | Manually created by the implementer |
| [[EXERCISE]_test.py](exercises/two-fer/two_fer_test.py) | Exercise test suite | Automatically generated if `.meta/template.j2` is present, otherwise manually created by the implementer |
| [example.py](exercises/two-fer/example.py) | Example solution used to automatically verify the `[EXERCISE]_test.py` suite | Manually created by the implementer |
| [.meta/template.j2](exercises/two-fer/.meta/template.j2) | Test generation template; if present used to automatically generate `[EXERCISE]_test.py` (See [generator documentation](docs/GENERATOR.md)) | Manually created by implementer |
| [.meta/additional_tests.json](exercises/word-count/.meta/additional_tests.json) | Defines additional track-specific test cases; if `.meta/template.j2` is also present these test will be incorporated into the automatically generated `[EXERCISE]_test.py` | Manually created by the implementer |
| [.meta/hints.md](exercises/high-scores/.meta/hints.md) | Contains track-specific hints that are automatically included in the generated `README.md` file | Manually created by the implementer |
| [README.md](exercises/two-fer/README.md) | Exercise README | [Generated by `configlet` tool](#generating-exercise-readmes) |

### Generating Exercise READMEs

#### Requirements
- A local clone of the [problem-specifications] repository.
- [configlet]: may be obtained either by
  - (**Recommended**) Following installation instructions at the above link
  - Running `bin/fetch-configlet` (`configlet` binary will be downloaded to the repository `bin/`)

#### Generating all READMEs

```
configlet generate <path/to/track> --spec-path path/to/problem/specifications
```

#### Generating a single README

```
configlet generate <path/to/track> --spec-path path/to/problem/specifications --only example-exercise
```

### Implementing tests

If an unimplemented exercise has a `canonical-data.json` file in the [problem-specifications] repository, a generation template must be created. See the [test generator documentation](docs/GENERATOR.md) for more information.

If an unimplemented exercise does not have a `canonical-data.json` file, the test file must be written manually (use existing test files for examples).

### Example solutions

Example solution files serve two purposes:

1. Verification of the tests
2. Example implementation for mentor/student reference

### config.json

[`config.json`](config.json) is used by the website to determine which exercises to load an in what order. It also contains some exercise metadata, such as difficulty, labels, and if the exercise is a core exercise. New entries should be places just before the first exercise that is marked `"deprecated": true`:

```JSON
    {
      "slug": "current-exercise",
      "uuid": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "core": false,
      "unlocked_by": null,
      "difficulty": 1,
      "topics": [
          "strings"
      ]
    },
    <<< HERE
    {
      "slug": "old-exercise",
      "uuid": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "core": false,
      "unlocked_by": null,
      "difficulty": 2,
      "topics": null,
      "status": "deprecated"
    },
```

Fields
<table>
<tr>
    <td>slug</td>
    <td>Hyphenated lowercase exercise name</td>
</tr>
<tr>
    <td>uuid</td>
    <td>Generate using <code>configlet uuid</code></td>
</tr>
<tr>
    <td>core</td>
    <td>Set to <code>false</code>; core exercises are decided by track maintainers</td>
</tr>
<tr>
    <td>unlocked_by</td>
    <td>Slug for the core exercise that unlocks the new one</td>
</tr>
<tr>
    <td>difficulty</td>
    <td><code>1</code> through <code>10</code>. Discuss with reviewer if uncertain.</td>
</tr>
<tr>
    <td>topics</td>
    <td>Array of relevant topics from the <a href="https://github.com/exercism/problem-specifications/blob/master/TOPICS.txt">topics list</a> </td>
</tr>
</table>


## Implementing Track-specific Exercises

Similar to implementing a canonical exercise that has no `canonical-data.json`, but the exercise README will also need to be written manually. Carefully follow the structure of generated exercise READMEs.



[EOL]: https://en.wikipedia.org/wiki/Newline
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[american-english]: https://github.com/exercism/docs/blob/main/building/markdown/style-guide.md
[being-a-good-community-member]: https://github.com/exercism/docs/tree/main/community/good-member
[concept-exercise-anatomy]: https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md
[concept-exercises]: https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md
[config-json]: https://github.com/exercism/javascript/blob/main/config.json
[configlet-general]: https://github.com/exercism/configlet
[configlet]: https://github.com/exercism/docs/blob/main/building/configlet/generating-documents.md
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
[help-wanted]: https://github.com/exercism/python/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22
[markdown-language]: https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
[open-an-issue]: https://github.com/exercism/python/issues/new/choose
[pep8-for-humans]: https://pep8.org/
[practice-exercise-anatomy]: https://github.com/exercism/docs/blob/main/building/tracks/practice-exercises.md
[practice-exercises]: https://github.com/exercism/docs/blob/main/building/tracks/practice-exercises.md
[prettier]: https://prettier.io/
[problem-specifications]: https://github.com/exercism/problem-specifications
[python-syllabus]: https://exercism.org/tracks/python/concepts
[python-track-test-generator]: https://github.com/exercism/python/blob/main/docs/GENERATOR.md
[the-words-that-we-use]: https://github.com/exercism/docs/blob/main/community/good-member/words.md
[website-contributing-section]: https://exercism.org/docs/building
