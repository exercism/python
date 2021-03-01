# Python reference

_Python is an interpreted, dynamically (but strongly) typed, and garbage-collected general programming language that has become extremely popular due to its readability, low barrier for entry, and exceptionally deep ecosystem of libraries and tools. Python is object-based, but is inherently multi-paradigm and has drawn together influences from a wide range of programming languages, including ABC, Haskell, Lisp, and Modula-3. It is ideal for prototyping and ad-hoc tasks, but also sees wide use in scientific computing, web development, and automation._

Below are concepts that were extracted/identified in Python based on Exercism's V2 exercises.
Resources used include:

- [Python 3 Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python Library Reference](https://docs.python.org/3/library/index.html)

<br>

## Unique to Python

<details>
    <summary> "Pythonic"/Python Community
      <br>
    </summary>

- [ ] [The Zen of Python][zen-of-python]
- [ ] [Pythonic][pythonic]
- [ ] [Python Enhancement Proposals][python-enhancement-proposals]
- [ ] [PEP 8][pep-8-style-guide]
- [ ] [Dunder Methods][dunder-methods]

</details>
<br>

## Baseline

<details>
    <summary> Concepts Introduced in the "Basics" Exercise (_Guido's Gorgeous Lasagna_):
      <br>
    </summary>

- [ ] [Arithmetic][arithmetic-general]
- [ ] [Assignment][assignment]
- [ ] [Comments][comments-general]

  - [ ] TODO: Explain # syntax in Python

- [ ] [Constants][constants]
- [ ] [Docstrings][docstrings]
- [ ] [Expressions][expressions]
- [ ] [Functions][functions-general]

  - [ ] [Function Definition][function-definition]
    - [ ] [`def`][keyword-def]
    - [ ] [`pass`][keyword-pass]
    - [ ] [`None`][keyword-none]
    - [ ] [Return Values][return-value]
      - [ ] [`return`][keyword-return]

- [ ] Statements

  - [ ] TODO: Explain the importance of statements in Python

- [ ] [Variables][variables]

</details>
<br>

## General

_Concepts needed for a good working understanding of the language_

<details>
    <summary> Current "Core" Concepts:
      <br>
    </summary>

- [ ] [Argument unpacking][argument-unpacking]
- [ ] [Arithmetic][arithmetic-general]

  - [ ] [Modular Division][modular-division]
  - [ ] [Arithmetic Operators][arithmetic-operators]

- [ ] [Bitwise manipulation][bitwise-manipulation-general]

  - [ ] [Binary numbers][binary-numbers]
  - [ ] [Bitflags][bitflags]
  - [ ] [Bitwise operators][bitwise-operators]
  - [ ] [Powers of Two][powers-of-two]

- [ ] [Boolean logic][boolean-logic-general]

  - [ ] [Boolean values][boolean-values]

    - [ ] [Booleans are integers][booleans-are-integers]
    - [ ] [`True`][keyword-true]
    - [ ] [`False`][keyword-false]

  - [ ] [Boolean operators][boolean-operators]
    - [ ] [`not`][keyword-not]
    - [ ] [Short-circuiting][short-circuiting]
      - [ ] [`and`][keyword-and]
      - [ ] [`or`][keyword-or]

- [ ] [Comparisons][comparisons-general]

  - [ ] [Comparison operators][comparison-operators]
  - [ ] [Integer comparison][integer-comparison]
  - [ ] [Rich comparison methods][rich-comparison-methods]
  - [ ] [Equality operator][equality-operator]
  - [ ] [Equivalence][equivalence]
  - [ ] [Inequality][inequality]

- [ ] [Conditionals][conditionals-general]

  - [ ] [Conditionals structures][conditional-structures]
    - [ ] [`if`][keyword-if]
    - [ ] [`elif`][keyword-elif]
    - [ ] [`else`][keyword-else]

- [ ] [`dict`][builtin-types-dict]

- [ ] [Enumeration][enumeration]

  - [ ] [Enumerated values][enumerated-values]
  - [ ] [`enumerate()`][builtin-functions-enumerate]

- [ ] [Functions][functions-general]

  - [ ] [Function Definition][function-definition]

    - [ ] [`def`][keyword-def]
    - [ ] [Function signature][function-signature]
      - [ ] [Arguments & parameters][arguments-and-parameters]
      - [ ] [Positional parameters][positional-parameters]
      - [ ] [Positional-only parameters][positional-only-parameters]
      - [ ] [Keyword parameters][keyword-parameters]
      - [ ] [Keyword-only parameters][keyword-only-parameters]
      - [ ] [Default arguments][default-arguments]
      - [ ] [`\*args`][star-args]
      - [ ] [`\*\*kwargs`][star-star-kwargs]
      - [ ] [Return Values][return-value]
        - [ ] [`return`][keyword-return]
        - [ ] [`none`][keyword-none]

  - [ ] [Nested functions][nested-functions]

  - [ ] [Type hinting][type-hinting]
  - [ ] [Call semantics][call-semantics]

- [ ] [Identity testing][identity-testing]

  - [ ] [`is`][keyword-is]

- [ ] [Importing][importing]

  - [ ] [relative imports][relative-imports]
  - [ ] [`import`][keyword-import]
  - [ ] [`from`][keyword-from]
  - [ ] [`as`][keyword-as]

- [ ] [Iteration][iteration]

  - [ ] [Iterables][iterables]
  - [ ] [Iterators][iterators]

  - [ ] [Loops][loops-general]

    - [ ] [`while` loops][while-loops]

      - [ ] [`while`][keyword-while]

    - [ ] [`for` loops][for-loops]

      - [ ] [`for`][keyword-for]
      - [ ] [`range`][builtin-types-range]

    - [ ] [Exiting loops][exiting-loops]
      - [ ] [`break`][keyword-break]
      - [ ] [`continue`][keyword-continue]
      - [ ] [`else` in a `loop` context][keyword-else-in-loops]

- [ ] [Membership testing][membership-testing]

  - [ ] [`in`][keyword-in]

- [ ] Numbers

  - [ ] [`int`][builtin-types-int]
  - [ ] [`float`][builtin-types-float]
  - [ ] [`complex`][builtin-types-complex]

    - [ ] [cmath][library-cmath]

  - [ ] [`fractions`][library-fractions]
  - [ ] [`decimal`][library-decimal]
  - [ ] [math][library-math]

- [ ] [Operators][operators]

  - [ ] [Operator overloading][operator-overloading]
  - [ ] [Operator precedence][operator-precedence]

- [ ] [REPL][repl]

  - [ ] TODO: Discuss the interactive Python interpreter

- [ ] [sequences][builtin-types-sequence]

  - [ ] [common sequence operations][common-sequence-operations]

    - [ ] [bracket notation][bracket-notation]
      - [ ] [Indexing][indexing]
      - [ ] [Slicing][slicing]
      - [ ] Slice assignment

  - [ ] [`list`][builtin-types-list]

    - [ ] [List Methods][list-methods]

  - [ ] [`range`][builtin-types-range]
  - [ ] [`str`][builtin-types-str]

    - [ ] [str-methods][string-methods]
    - [ ] [String formatting][string-formatting]
    - [ ] [str-splitting][string-splitting]
    - [ ] [str-translation][string-translation]

  - [ ] [`tuple`][builtin-types-tuple]

- [ ] [Scope][scope]

  - [ ] [`del`][keyword-del]

  - [ ] [Namespaces][namespaces]
    - [ ] [`global`][keyword-global]
    - [ ] [`nonlocal`][keyword-nonlocal]

- [ ] [`set`][builtin-types-set]

  - [ ] [`frozenset`][builtin-types-frozenset]

- [ ] [Type conversion][type-conversion]
      TODO: Casting between types in Python can be a bit unclear; this will need expansion

  - [ ] [Type conversion][type-conversion]

- [ ] [Variables][variables]
  - [ ] [Assignment][assignment]
    - [ ] [Multiple assignment][multiple-assignment]
    - [ ] [Tuple unpacking][tuple-unpacking]
    - [ ] [Constants][constants]

</details>
<br>

## Detailed

_Concepts needed for a deeper understanding/fluency_

<details>
    <summary> "Intermediate" Concepts
      <br>
    </summary>

- [ ] Aliasing

  - [ ] [`as`][keyword-as]
  - [ ] [`import`][keyword-import]

- [ ] [Anonymous functions][anonymous-functions-general]

  - [ ] [`lambda`][keyword-lambda]

- [ ] [`bytes`][builtin-types-bytes]

  - [ ] [`bytearray`][builtin-types-bytearray]

- [ ] [Comprehension Syntax][comprehension-syntax]

  - [ ] [List comprehension][list-comprehension]
  - [ ] [Dict comprehension][dict-comprehension]
  - [ ] [Set comprehension][set-comprehension]
  - [ ] [Generator comprehension][generator-comprehension]

- [ ] Context managers

  - [ ] [`with`][keyword-with]

- [ ] [Decorators][decorators]

- [ ] [Docstrings][docstrings]

- [ ] [Exceptions][exceptions-general]

  - [ ] [Exception handling][exception-handling]
  - [ ] [Exception catching][exception-catching]

    - [ ] [`try`][keyword-try]
    - [ ] [`except`][keyword-except]
    - [ ] [`else`][keyword-else]
    - [ ] [`finally`][keyword-finally]

  - [ ] [Exception hierarchy][exception-hierarchy]
  - [ ] [Raise][raise]
    - [ ] [Exception message][exception-message]
    - [ ] [`raise`][keyword-raise]
    - [ ] [`from`][keyword-from]
    - [ ] [raise from][exception-chaining]
    - [ ] [`assert`][keyword-assert]

- [ ] [Generators][generators]

  - [ ] [`yield`][keyword-yield]

- [ ] [Higher-order functions][higher-order-functions]

  - [ ] [Decorators as higher-order functions][decorators-as-higher-order-functions]
  - [ ] [`map`][builtin-functions-map]
  - [ ] [`filter`][builtin-functions-filter]

- [ ] [Partial application][partial-application]

  - [ ] TODO: `functools.partial`

- [ ] [Recursion][recursion]

  - [ ] TODO: explain limitations of recursion in Python, ie `RecursionLimit`

- [ ] [Regular Expressions][regular-expressions]

</details>
<br>

## Object-Oriented Specific

<details>
    <summary> OOP-Specific/Class Oriented Concepts
      <br>
    </summary>

- [ ] [Objects][objects-general]

  - [ ] [Everything is an object][everything-is-an-object]
    - [ ] [`type`][builtin-types-type]
    - [ ] [`object`][builtin-types-object]
    - [ ] [`property`][builtin-types-property]

- [ ] [Classes][classes-general]

  - [ ] [Custom classes][custom-classes]
    - [ ] [`class`][keyword-class]
  - [ ] [Class members][class-members]
    - [ ] Behavior
      - [ ] [Methods][methods-general]
        - [ ] [Instance Methods][instance-methods]
          - [ ] [Implicit self][implicit-self]
          - [ ] [Initialization][initialization]
          - [ ] [Instantiation][instantiation]
        - [ ] [Class methods][class-methods]
          - [ ] [Constructor][constructor]
        - [ ] [Static Methods][static-methods]
    - [ ] [State][state]
      - [ ] [Instance Attributes][instance-attributes]
      - [ ] [Instance Properties][instance-properties]
        - [ ] [Property Decorator][property-decorator]

- [ ] [Inheritance][inheritance-general]

  - [ ] [Class inheritance][class-inheritance]

- [ ] [Composition][composition-general]

  - [ ] [Class composition][class-composition]

- [ ] [Encapsulation][encapsulation-general]

  - [ ] [Non-Public Methods][non-public-methods]

- [ ] [Interfaces][interfaces-general]

  - [ ] [Meta Classes][metaclasses]
    - [ ] [Virtual Base Classes]
    - [ ] [Abstract Base Classes]
    - [ ] [`.__subclasshook__() `]
    - [ ] [`.register()`]
  - [ ] [Duck Typing][duck-typing]

- [ ] [Mutation][mutation-general]

  - [ ] [Immutability in Python][immutability]
  - [ ] [Mutability in Python][mutability]

- [ ] [Polymorphism][polymorphism-general]
  - [ ] [Dynamic typing][dynamic-typing]
  - [ ] [Duck Typing][duck-typing]
  - [ ] [Gradual Typing][gradual-typing]
    - [ ] [Type Hinting][type-hinting]
    - [ ] [`typing`][typing-module]

</details>
<br>

## Specialized

_(These are probably outside scope of an Exercism Concept exercise, but might make good longer/practice exercises that recieve mentoring)_

<details>
    <summary> Advanced/Specialized Concepts
      <br>
    </summary>

- [ ] Asynchronous operatons
  - [ ] [`async`][keyword-async]
  - [ ] [`await`][keyword-await]

_These datatypes will very rarely be encountered in the wild, the first because it's more of an internal implementation detail and the second because it's hyper-specific_:

- [ ] [`slice`][builtin-types-slice]
- [ ] [`memoryview`][builtin-types-memoryview]

</details>

[anonymous-functions-general]: ../../../reference/concepts/anonymous_functions.md
[argument-unpacking]: ./concepts/argument_unpacking.md
[arguments-and-parameters]: ./concepts/arguments_and_parameters.md
[arithmetic-general]: ../../../reference/concepts/arithmetic.md
[arithmetic-operators]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
[assignment]: ./concepts/assignment.md
[binary-numbers]: ./concepts/binary_numbers.md
[bitflags]: ./concepts/bitflags.md
[bitwise-manipulation-general]: ../../../reference/concepts/bitwise_manipulation.md
[bitwise-operators]: ./concepts/bitwise_operators.md
[boolean-logic-general]: ../../../reference/concepts/boolean_logic.md
[boolean-operators]: ./concepts/boolean_operators.md
[boolean-values]: ./concepts/boolean_values.md
[booleans-are-integers]: ./concepts/booleans_are_integers.md
[bracket-notation]: ./concepts/bracket_notation.md
[builtin-functions-__import__]: ./concepts/builtin_functions/__import__.md
[builtin-functions-abs]: ./concepts/builtin_functions/abs.md
[builtin-functions-all]: ./concepts/builtin_functions/all.md
[builtin-functions-any]: ./concepts/builtin_functions/any.md
[builtin-functions-ascii]: ./concepts/builtin_functions/ascii.md
[builtin-functions-bin]: ./concepts/builtin_functions/bin.md
[builtin-functions-breakpoint]: ./concepts/builtin_functions/breakpoint.md
[builtin-functions-callable]: ./concepts/builtin_functions/callable.md
[builtin-functions-chr]: ./concepts/builtin_functions/chr.md
[builtin-functions-classmethod]: ./concepts/builtin_functions/classmethod.md
[builtin-functions-compile]: ./concepts/builtin_functions/compile.md
[builtin-functions-delattr]: ./concepts/builtin_functions/delattr.md
[builtin-functions-dir]: ./concepts/builtin_functions/dir.md
[builtin-functions-divmod]: ./concepts/builtin_functions/divmod.md
[builtin-functions-enumerate]: ./concepts/builtin_functions/enumerate.md
[builtin-functions-eval]: ./concepts/builtin_functions/eval.md
[builtin-functions-exec]: ./concepts/builtin_functions/exec.md
[builtin-functions-filter]: ./concepts/builtin_functions/filter.md
[builtin-functions-format]: ./concepts/builtin_functions/format.md
[builtin-functions-getattr]: ./concepts/builtin_functions/getattr.md
[builtin-functions-globals]: ./concepts/builtin_functions/globals.md
[builtin-functions-hasattr]: ./concepts/builtin_functions/hasattr.md
[builtin-functions-hash]: ./concepts/builtin_functions/hash.md
[builtin-functions-help]: ./concepts/builtin_functions/help.md
[builtin-functions-hex]: ./concepts/builtin_functions/hex.md
[builtin-functions-id]: ./concepts/builtin_functions/id.md
[builtin-functions-input]: ./concepts/builtin_functions/input.md
[builtin-functions-isinstance]: ./concepts/builtin_functions/isinstance.md
[builtin-functions-issubclass]: ./concepts/builtin_functions/issubclass.md
[builtin-functions-iter]: ./concepts/builtin_functions/iter.md
[builtin-functions-len]: ./concepts/builtin_functions/len.md
[builtin-functions-locals]: ./concepts/builtin_functions/locals.md
[builtin-functions-map]: ./concepts/builtin_functions/map.md
[builtin-functions-max]: ./concepts/builtin_functions/max.md
[builtin-functions-min]: ./concepts/builtin_functions/min.md
[builtin-functions-next]: ./concepts/builtin_functions/next.md
[builtin-functions-oct]: ./concepts/builtin_functions/oct.md
[builtin-functions-open]: ./concepts/builtin_functions/open.md
[builtin-functions-ord]: ./concepts/builtin_functions/ord.md
[builtin-functions-pow]: ./concepts/builtin_functions/pow.md
[builtin-functions-print]: ./concepts/builtin_functions/print.md
[builtin-functions-repr]: ./concepts/builtin_functions/repr.md
[builtin-functions-reversed]: ./concepts/builtin_functions/reversed.md
[builtin-functions-round]: ./concepts/builtin_functions/round.md
[builtin-functions-setattr]: ./concepts/builtin_functions/setattr.md
[builtin-functions-sorted]: ./concepts/builtin_functions/sorted.md
[builtin-functions-staticmethod]: ./concepts/builtin_functions/staticmethod.md
[builtin-functions-sum]: ./concepts/builtin_functions/sum.md
[builtin-functions-super]: ./concepts/builtin_functions/super.md
[builtin-functions-vars]: ./concepts/builtin_functions/vars.md
[builtin-functions-zip]: ./concepts/builtin_functions/zip.md
[builtin-functions]: ./concepts/builtin_functions/README.md
[builtin-types-bool]: ./concepts/builtin_types/bool.md
[builtin-types-bytearray]: ./concepts/builtin_types/bytearray.md
[builtin-types-bytes]: ./concepts/builtin_types/bytes.md
[builtin-types-complex]: ./concepts/builtin_types/complex.md
[builtin-types-dict]: ./concepts/builtin_types/dict.md
[builtin-types-float]: ./concepts/builtin_types/float.md
[builtin-types-frozenset]: ./concepts/builtin_types/frozenset.md
[builtin-types-int]: ./concepts/builtin_types/int.md
[builtin-types-list]: ./concepts/builtin_types/list.md
[builtin-types-memoryview]: ./concepts/builtin_types/memoryview.md
[builtin-types-object]: ./concepts/builtin_types/object.md
[builtin-types-property]: ./concepts/builtin_types/property.md
[builtin-types-range]: ./concepts/builtin_types/range.md
[builtin-types-sequence]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[builtin-types-set]: ./concepts/builtin_types/set.md
[builtin-types-slice]: ./concepts/builtin_types/slice.md
[builtin-types-str]: ./concepts/builtin_types/str.md
[builtin-types-tuple]: ./concepts/builtin_types/tuple.md
[builtin-types-type]: ./concepts/builtin_types/type.md
[builtin-types]: ./concepts/builtin_types/README.md
[call-semantics]: ./concepts/call_semantics.md
[class-composition]: ./concepts/class_composition.md
[class-inheritance]: ./concepts/class_inheritance.md
[class-members]: ./concepts/class_members.md
[class-methods]: ./concepts/class_methods.md
[classes-general]: ../../../reference/concepts/classes.md
[comments-general]: ../../../reference/concepts/comments.md
[common-sequence-operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[comparison-operators]: ./concepts/comparison_operators.md
[comparisons-general]: ../../../reference/concepts/comparisons.md
[composition-general]: ../../../reference/concepts/composition.md
[comprehension-syntax]: ./concepts/comprehension_syntax.md
[conditional-structures]: ./concepts/conditional_structures.md
[conditionals-general]: ../../../reference/concepts/conditionals.md
[constants]: ./concepts/constants.md
[constructor]: ./concepts/constructor.md
[custom-classes]: ./concepts/custom_classes.md
[data-structures]: ./concepts/data_structures.md
[decorators-as-higher-order-functions]: ./concepts/decorators_as_higher_order_functions.md
[decorators]: ./concepts/decorators.md
[default-arguments]: ./concepts/default_arguments.md
[dict-comprehension]: ./concepts/dict_comprehension.md
[docstrings]: ./concepts/docstrings.md
[duck-typing]: ./concepts/duck_typing.md
[dunder-methods]: ./concepts/dunder_methods.md
[dynamic-typing]: ./concepts/dynamic_typing.md
[encapsulation-general]: ../../../reference/concepts/encapsulation.md
[enumerated-values]: ./concepts/enumerated_values.md
[enumeration]: ../../../reference/concepts/enumeration.md
[equality-operator]: ./concepts/equality_operator.md
[equivalence]: ./concepts/equivalence.md
[everything-is-an-object]: ./concepts/everything_is_an_object.md
[exception-catching]: ./concepts/exception_catching.md
[exception-chaining]: https://docs.python.org/3/tutorial/errors.html#exception-chaining
[exception-handling]: ./concepts/exception_handling.md
[exception-hierarchy]: ./concepts/exception_hierarchy.md
[exception-message]: ./concepts/exception_message.md
[exceptions-general]: ./concepts/exceptions.md
[exiting-loops]: ./concepts/exiting_loops.md
[expressions]: ./concepts/expressions.md
[for-loops]: ./concepts/for_loops.md
[function-definition]: ./concepts/function_definition.md
[function-signature]: ./concepts/function_signature.md
[functions-general]: ../../../reference/concepts/functions.md
[generator-comprehension]: ./concepts/generator_comprehension.md
[generators]: ./concepts/generators.md
[gradual-typing]: https://en.wikipedia.org/wiki/Gradual_typing
[higher-order-functions]: ../../../reference/concepts/higher_order_functions.md
[identity-testing]: ./concepts/identity_testing.md
[immutability]: ../../../reference/concepts/immutability.md
[implicit-self]: ./concepts/implicit_self.md
[importing]: ./concepts/importing.md
[indexing]: ./concepts/indexing.md
[inequality]: ./concepts/inequality.md
[inheritance-general]: ../../../reference/concepts/inheritance.md
[initialization]: ./concepts/initialization.md
[instance-attributes]: ./concepts/instance_attributes.md
[instance-methods]: ./concepts/instance_methods.md
[instance-properties]: ./concepts/instance_properties.md
[instantiation]: ./concepts/instantiation.md
[integer-comparison]: ./concepts/integer_comparison.md
[interfaces-general]: ../../../reference/concepts/interfaces.md
[iterables]: ./concepts/iterables.md
[iteration]: ./concepts/iteration.md
[iterators]: ./concepts/iterators.md
[keyword-and]: ./concepts/keywords/and.md
[keyword-as]: ./concepts/keywords/as.md
[keyword-assert]: ./concepts/keywords/assert.md
[keyword-async]: ./concepts/keywords/async.md
[keyword-await]: ./concepts/keywords/await.md
[keyword-break]: ./concepts/keywords/break.md
[keyword-class]: ./concepts/keywords/class.md
[keyword-continue]: ./concepts/keywords/continue.md
[keyword-def]: ./concepts/keywords/def.md
[keyword-del]: ./concepts/keywords/del.md
[keyword-elif]: ./concepts/keywords/elif.md
[keyword-else]: ./concepts/keywords/else.md
[keyword-else-in-loops]: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
[keyword-except]: ./concepts/keywords/except.md
[keyword-false]: ./concepts/keywords/false.md
[keyword-finally]: ./concepts/keywords/finally.md
[keyword-for]: ./concepts/keywords/for.md
[keyword-from]: ./concepts/keywords/from.md
[keyword-global]: ./concepts/keywords/global.md
[keyword-if]: ./concepts/keywords/if.md
[keyword-import]: ./concepts/keywords/import.md
[keyword-in]: ./concepts/keywords/in.md
[keyword-is]: ./concepts/keywords/is.md
[keyword-lambda]: ./concepts/keywords/lambda.md
[keyword-none]: ./concepts/keywords/none.md
[keyword-nonlocal]: ./concepts/keywords/nonlocal.md
[keyword-not]: ./concepts/keywords/not.md
[keyword-only-parameters]: ./concepts/keyword_only_parameters.md
[keyword-or]: ./concepts/keywords/or.md
[keyword-parameters]: ./concepts/keyword_parameters.md
[keyword-pass]: ./concepts/keywords/pass.md
[keyword-raise]: ./concepts/keywords/raise.md
[keyword-return]: ./concepts/keywords/return.md
[keyword-true]: ./concepts/keywords/true.md
[keyword-try]: ./concepts/keywords/try.md
[keyword-while]: ./concepts/keywords/while.md
[keyword-with]: ./concepts/keywords/with.md
[keyword-yield]: ./concepts/keywords/yield.md
[keywords]: ./concepts/keywords/README.md
[library-decimal]: https://docs.python.org/3/library/decimal.html#module-decimal
[library-fractions]: https://docs.python.org/3/library/fractions.html
[library-math]: https://docs.python.org/3/library/math.html
[library-cmath]: https://docs.python.org/3/library/cmath.html#module-cmath
[list-comprehension]: ./concepts/list_comprehension.md
[list-methods]: ./concepts/list_methods.md
[lookup-efficiency]: ./concepts/lookup_efficiency.md
[loops-general]: ../../../reference/concepts/loops.md
[membership-testing]: ./concepts/membership_testing.md
[method-overloading]: ./concepts/method_overloading.md
[metaclasses]: https://docs.python.org/3/library/abc.html#abc.ABCMeta
[methods-general]: ../../../reference/concepts/methods.md
[modular-division]: ./concepts/modular_division.md
[multiple-assignment]: ./concepts/multiple_assignment.md
[multiple-inheritance]: https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
[mutability]: ./concepts/mutability.md
[mutation-general]: ../../../reference/concepts/mutation.md
[namespaces]: ./concepts/namespaces.md
[nested-functions]: ../../../reference/concepts/nested_functions.md
[non-public-methods]: ./concepts/non_public_methods.md
[objects-general]: ../../../reference/concepts/objects.md
[operator-overloading]: ./concepts/operator_overloading.md
[operator-precedence]: https://docs.python.org/3/reference/expressions.html#operator-summary
[operators]: ./concepts/operators.md
[order-of-evaluation]: ./concepts/order_of_evaluation.md
[partial-application]: ../../../reference/concepts/partial_application.md
[pep-8-style-guide]: ./concepts/pep_8_style_guide.md
[polymorphism-general]: ../../../reference/concepts/polymorphism.md
[positional-only-parameters]: ./concepts/positional_only_parameters.md
[positional-parameters]: ./concepts/positional_parameters.md
[powers-of-two]: ./concepts/powers_of_two.md
[property-decorator]: ./concepts/property_decorator.md
[python-enhancement-proposals]: ./concepts/python_enhancement_proposals.md
[python-exercises]: https://github.com/exercism/v3/tree/master/languages/python/exercises
[pythonic]: ./concepts/pythonic.md
[raise]: ./concepts/raise.md
[recursion]: ../../../reference/concepts/recursion.md
[recursive-data-structures]: ./concepts/recursive_data_structures.md
[regular-expressions]: ./concepts/regular_expressions.md
[relative-imports]: https://docs.python.org/3/reference/import.html#package-relative-imports
[repl]: ../../../reference/concepts/repl.md
[return-value]: ./concepts/return_value.md
[rich-comparison-methods]: ./concepts/rich_comparison_methods.md
[scope]: ../../../reference/concepts/scope.md
[set-comprehension]: ./concepts/set_comprehension.md
[short-circuiting]: ./concepts/short_circuiting.md
[slicing]: ./concepts/slicing.md
[standard-library]: ./concepts/standard_library.md
[star-args]: ./concepts/star_args.md
[star-star-kwargs]: ./concepts/star_star_kwargs.md
[state]: ../../../reference/concepts/state.md
[static-methods]: ./concepts/static_methods.md
[string-formatting]: ./concepts/string_formatting.md
[string-methods]: ./concepts/string_methods.md
[string-splitting]: ./concepts/string_splitting.md
[string-translation]: ./concepts/string_translation.md
[tuple-unpacking]: ./concepts/tuple_unpacking.md
[type-conversion]: ./concepts/type_conversion.md
[type-hinting]: ./concepts/type_hinting.md
[typing-module]: https://docs.python.org/3/library/typing.html
[variables]: ../../../reference/concepts/variables.md
[while-loops]: ./concepts/while_loops.md
[zen-of-python]: ./concepts/zen_of_python.md

<br>

## Implementations in Progress

Expect this table to be updated as larger concepts are broken down or additional concepts/exercises are identified.
<br>
See the [**Python Exercises Table**][python-exercises] (_`exercices/README.md`_) for committed "live" on website concept exercises.

#### Below are currently identified concepts needing:

1.  Issues logged (_Blank issue entry_)
2.  PRs written (_An issue's been logged but there is no PR/exercise_)
3.  Possible Imrovements (_PRs as noted /the exercise has been completed, but could be iterated on_)

<br>

|  Concept Group                            	|  Topics Included                                                                                                                                                                                                                                                                                                                                                                                                                                         	|  Issue Link                                                                                                      	|  PR Link                                	|  Exercise Name                                                                                                                 	|
|-------------------------------------------	|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------	|-----------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------	|
|  aliasing                                 	|  - [as][keyword-as]                                                                                                                                                                                                                                                                                                                                                                                                                                        	|  [ ]()                                                                                                           	|                                         	|                                                                                                                                	|
|  anonymous-functions (lambda)             	|  - [Anonymous functions][anonymous-functions-general]<br>- [lambda][keyword-lambda]                                                                                                                                                                                                                                                                                                                                                                            	|  [#2357](https://github.com/exercism/python/issues/2357)                                                         	|                                         	|                                                                                                                                	|
|  basics                                   	|   - [Assignment][assignment]<br>- [Variables][variables]<br>- [Constants][constants]<br>- [Objects][objects-general]<br>- [Functions][functions-general]<br>- [Function Definition][function-definition]<br>- [Arguments & Parameters][arguments-and-parameters]<br>- [def][keyword-def]<br>- [return][keyword-return]<br>- [Return Values][return-value]<br>- [Docstrings][docstrings]<br>- [Comments][comments-general]                                                                  	| Completed                                                                                                        	| Completed                               	|  [Guidos Gorgeous Lasagna](https://github.com/exercism/python/tree/main/tree/main/exercises/concept/guidos-gorgeous-lasagna)   	|
|  binary data                              	|                                                                                                                                                                                                                                                                                                                                                                                                                                                          	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  bitflags                                 	|  - [bitflags][bitflags]                                                                                                                                                                                                                                                                                                                                                                                                                                    	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  bitwise and bitwise operators            	|  - [Bitwise manipulation][bitwise-manipulation-general]                                                                                                                                                                                                                                                                                                                                                                                                    	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  bools & boolean-logic                    	|  - [**bool**l][builtin-types-bool]<br>- [Boolean operators][boolean-operators]<br>-  [Boolean values][boolean-values]<br>- [False][keyword-false]<br>- [True][keyword-true]<br>- [and][keyword-and]<br>- [or][keyword-or]<br>- [Short circuiting][short-circuiting]<br>- [Boolean logic][boolean-logic-general]<br>- [Booleans are integers][booleans-are-integers]                                                                                                              	| Completed                                                                                                        	| Completed                               	|  [ghost-gobble-arcade-game](https://github.com/exercism/python/tree/main/tree/main/exercises/concept/ghost-gobble-arcade-game) 	|
|  bytes                                    	|  - [bytes][builtin-types-bytes]<br>- [bytearray][builtin-types-bytearray]                                                                                                                                                                                                                                                                                                                                                                                     	|  []()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  class-composition                        	|  - [Class Composition][class-composition]<br>- dependancy injuection/inverse of control                                                                                                                                                                                                                                                                                                                                                                     	| [#2352](https://github.com/exercism/python/issues/2352)                                                                                                                	|                                         	|                                                                                                                                	|
|  class-customization                      	|  - [Custom Classes][custom-classes]<br>- [Property Decorator][property-decorator] (`@property`)<br>- [Class methods][class-methods] (`@classmethod`)<br>- [Static Methods][static-methods] (`@staticmethod`)<br>- [Non-Public Methods][non-public-methods]  (getters, setters)<br>-  class members                                                                                                                                                                      	|  [ #2350](https://github.com/exercism/python/issues/2350)                                                        	|  [ ]()                                  	|                                                                                                                                	|
|  class-inheritance                        	|  - [Inheritance][inheritance-general]<br>- [Class Inheritance][class-inheritance]<br>- [Multiple Inheritance][mulitple-inheritance]<br>- `__super__()`<br>- `minxins`<br>- MRO                                                                                                                                                                                                                                                                                          	|  [#2351](https://github.com/exercism/python/issues/2351)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  class-interfaces                         	|  - Multiple Inheritance<br>- MRO<br>- Abstract Base Clases                                                                                                                                                                                                                                                                                                                                                                                                         	|  []()                                                                                                            	|                                         	|                                                                                                                                	|
|  classes                                  	|  - [Classes][classes-general]<br>- [class][keyword-class]<br>- [Constructor][constructor] (`self`, `__init__()`)<br>- [property][builtin-types-property]<br>- [Instance Attributes][instance-attributes]<br>- [Instance Methods][instance-methods]<br>- [Instance Properties][instance-properties]<br>- [Instantiation][instantiation]<br>- [Initialization][initialization]<br>- [pass][keyword-pass]<br>- [opbject][builtin-types-object]                                            	|  [ #2349](https://github.com/exercism/python/issues/2349)                                                        	|  [ ]()                                  	|                                                                                                                                	|
|  collections                              	|  - namedtuple()<br>- Counter<br>- dequeue<br>- defaultdict<br>- OrderedDict<br>- ChainMap                                                                                                                                                                                                                                                                                                                                                                               	|  []()                                                                                                            	|                                         	|                                                                                                                                	|
|  comparisons                              	|  - [Comparisons][comparisons-general]<br>- [Comparison operators][comparison-operators]<br>- [Equivalence][equivalence]<br>- [Equality operator][equality-operator]<br>- [Inequality][inequality]                                                                                                                                                                                                                                                                    	|  [#2039](https://github.com/exercism/python/issues/2288)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  complex-numbers                          	|  - [complex][builtin-types-complex]<br>- [cmath][library-cmath]<br>- [decimal][library-decimal]<br>- [fractions][library-fractions]                                                                                                                                                                                                                                                                                                                               	|  [#2208](https://github.com/exercism/v3/issues/2208) note: same issue as float/int, but will be its own exercise 	|  [ ]()                                  	|                                                                                                                                	|
|  conditionals                             	|  - Conditionals][conditionals-general]<br>- [Conditional structures][conditional-structures]<br>- [if][keyword-if]<br>- [elif][keyword-elif]<br>- [else][keyword-else]<br>- [else][keyword-else]                                                                                                                                                                                                                                                                        	|  Completed                                                                                                       	|  Merged.  Draft.  Needs Additional Work 	|                                                                                                                                	|
|  context-manager customization            	|  - [with][keyword-with]<br>- `contextlib`<br>- @contextlib.contextmanager<br>- contextlib.closing()<br>- contextlib.nullcontext()<br>- contextlib.suppress<br>- conextlib.redirect_stdout()<br>- contextlib.redirect_stderr()<br>- class contextlib.ContextDecorator<br>- `context-handling`<br>- `context-managers`<br>- `context-manager` types                                                                                                             	|  [#2370](https://github.com/exercism/python/issues/2370)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  dataclasses and namedtuples              	|  - `dataclasses`<br>- `@dataclass`<br>- `collections.namedtuple()` - `decorators`                                                                                                                                                                                                                                                                                                                                                                              	|  [ #2361](https://github.com/exercism/python/issues/2361)                                                        	|  [ ]()                                  	|                                                                                                                                	|
|  decorators                               	|  - [decorators][decorators]<br>- [Decorators as higher-order functions][decorators-as-higher-order-functions]<br>-  nested functions<br>- functions-as-arguments<br>- functions-as-returns<br>- `functools.wraps()`<br>- `@` symbol for decorators                                                                                                                                                                                                                         	|  [ #2356](https://github.com/exercism/python/issues/2356)                                                        	|  [ ]()                                  	|                                                                                                                                	|
|  descriptors                              	|  - descrptor protocol<br>- descriptors<br>- private variables<br>- name mangling<br>- data descriptors<br>- non-data descriptors<br>- class attributes<br>- class members                                                                                                                                                                                                                                                                                                     	|  [#2365](https://github.com/exercism/python/issues/2365)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  dict-methods                             	|  - [dict][builtin-types-dict]                                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ #2348](https://github.com/exercism/python/issues/2348)                                                        	|                                         	|                                                                                                                                	|
|  dicts                                    	|  - [dict][builtin-types-dict]                                                                                                                                                                                                                                                                                                                                                                                                                              	|  Completed                                                                                                       	|  Completed                              	|  [inventory-management](https://github.com/exercism/python/tree/main/exercises/concept/inventory-management)                   	|
|  enums                                    	|  - enums                                                                                                                                                                                                                                                                                                                                                                                                                                                   	|  Completed                                                                                                       	|  Completed                              	|  [log-levels](https://github.com/exercism/python/tree/main/exercises/concept/log-levels)                                       	|
|  function-arguments                       	|  - [Arguments & Parameters][arguments-and-parameters]<br>- [Keyword parameters][keyword-parameters]<br>- [Positional parameters][positional-parameters]<br>- [Default arguments][default-arguments]<br>- [Positional-only parameters][positional-only-parameters]<br>- [Keyword-only parameters][keyword-only-parameters]<br>- [`*args`][star-args]<br>- [`**kwargs`][star-star-kwargs]<br>- [None][keyword-none]<br>- `/*` for requiring parameter types                           	|  [#2364](https://github.com/exercism/python/issues/2354)                                                         	|                                         	|                                                                                                                                	|
|  functional tools                         	| - [map][builtin-functions-map]<br>- [filter][builtin-functions-filter]<br>- `functools.reduce`                                                                                                                                                                                                                                                                                                                                                                 	|  [#2359](https://github.com/exercism/python/issues/2359)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  functions                                	|  - [Call semantics][call-semantics]<br>- [Namespaces][namespaces]<br>- callable objects<br>- scope<br>- nested functions<br>- `closures`<br>- `return`<br>- `global`<br>- `nonlocal`<br>- "first class" functions<br>- function attributes                                                                                                                                                                                                                                             	|  [ #2353](https://github.com/exercism/python/issues/2353)                                                        	|  [ ]()                                  	|                                                                                                                                	|
|  functools                                	|  - [Partial application][partial-application]<br>- single dispatch<br>- higher-order functions<br>- functools.partial()<br>- partial.func<br>- partial.args<br>- partial.keywords<br>- functools.update_wrapper()<br>- funtools.cache()<br>- @functools.cached_property()<br>- @functools.lru_cache()<br>- @functools.total_ordering<br>- @functools.singledispatch<br>- @<function>.register()<br>- @functools.wraps()<br>- class functools.partialmethod()<br>- class functools.singledispatchmethod() 	|  [#2366](https://github.com/exercism/python/issues/2366)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  generator expressions                    	|  - [Generator expression][generator-comprehension]                                                                                                                                                                                                                                                                                                                                                                                                         	|  [#1384](https://github.com/exercism/python/issues/2292)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  generators                               	|  - [Generators][generators]<br>- [yield][keyword-yield]                                                                                                                                                                                                                                                                                                                                                                                                     	|  [#2293](https://github.com/exercism/python/issues/2293)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  higher-order-functions                   	|  - [Function Signature][function-signature]<br>- [pass][keyword-pass]<br>- [Higher-order functions]<br>- [higher-order-functions]<br>- [Nested functions][nested-functions]<br>- [global][keyword-global]<br>- [nonlocal][keyword-nonlocal]<br>- `closures`<br>- `recursion`<br>- `functions as arguments`<br>- `functions as returns`                                                                                                                                                  	|  [#2355](https://github.com/exercism/python/issues/2355)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  import                                   	|  - [import][keyword-import]<br>- [importing][importing]<br>- relative imports<br>- [from][keyword-from]<br>- [as][keyword-as]                                                                                                                                                                                                                                                                                                                                              	|  ON HOLD                                                                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  iteration                                	|  - [Enumerated values][enumerated-values]<br>- [Enumerate][builtin-functions-enumerate]                                                                                                                                                                                                                                                                                                                                                                        	|  [ ]()                                                                                                           	|                                         	|                                                                                                                                	|
|  iterators                                	|  - [Iterators][iterators]<br>- iterator protocol<br>-  `__next_()`<br>- `__stopiteration__()`<br>-  `__iter__()`<br>-  `iter()`<br>- `__getitem__()`                                                                                                                                                                                                                                                                                                                       	|  [#2367](https://github.com/exercism/python/issues/2367)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  itertools                                	|  - `itertools`<br>- count()<br>- cycle()<br>- repeat()<br>- accumulate()<br>- product()<br>- chain() & chain.from_iterable()<br>- groupby()<br>- islice()<br>- zip_longest() and the zip() built-in<br>- permutations()<br>- combinations()                                                                                                                                                                                                                                               	|  [#2368](https://github.com/exercism/python/issues/2368)                                                         	|                                         	|                                                                                                                                	|
|  list-comprehensions                      	|  - [Comprehension Syntax][comprehension-syntax]<br>- [list comprehension][list-comprehension]<br>- comprehensions are optimized loops                                                                                                                                                                                                                                                                                                                              	|  [#1361](https://github.com/exercism/python/issues/2295)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  list-methods                             	|  - [list methods][list-methods]                                                                                                                                                                                                                                                                                                                                                                                                                            	|  Completed                                                                                                       	|  Completed                              	|  [Chaitanas Colossal Coaster](https://github.com/exercism/python/tree/main/exercises/concept/chaitanas-colossal-coaster)       	|
|  lists                                    	|  - [list][builtin-types-list]                                                                                                                                                                                                                                                                                                                                                                                                                              	|  Completed                                                                                                       	|  Completed                              	|  [Elyses Enchantments](https://github.com/exercism/python/tree/main/exercises/concept/elyses-enchantments)                     	|
|  loops                                    	|  - [Loops][loops-general]<br>- [for loops][for-loops]<br>- [while loops][while-loops]<br>- [while][keyword-while]<br>- [for][keyword-for]<br>- [range][builtin-types-range]<br>- [Exiting loops][exiting-loops]<br>- [break][keyword-break]<br>- [continue][keyword-continue]<br>- [else][keyword-else]                                                                                                                                                                             	|  Completed                                                                                                       	|  Completed                              	|  [Making the Grade](https://github.com/exercism/python/tree/main/exercises/concept/making-the-grade)                           	|
|  memoryview                               	|  - [memoryview][builtin-types-memoryview]                                                                                                                                                                                                                                                                                                                                                                                                                  	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  no stand-alone (multiple concepts)       	|  - [Membership testing][membership-testing]<br>- [in][keyword-in]<br>- [is][keyword-is]<br>- [not][keyword-not]                                                                                                                                                                                                                                                                                                                                                          	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  none                                     	|  - [None][keyword-none]                                                                                                                                                                                                                                                                                                                                                                                                                                    	|  Completed                                                                                                       	|  Completed                              	|  [Restaurant Rozalynn](https://github.com/exercism/python/tree/main/exercises/concept/restaurant-rozalynn)                     	|
|  number-variations                        	|  - [Binary numbers][binary-numbers]<br>- [Octal numbers][octal-numbers]<br>- [Hexidecimal numbers][hex-numbers]<br>- [Powers of Two][powers-of-two]<br>- decimals<br>- fractions                                                                                                                                                                                                                                                                                        	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  numbers                                  	|  - numbers<br>- [int][builtin-types-int]<br>- [float][builtin-types-float]<br>- [Arithmetic][arithmetic-general]<br>- [Integer comparison][integer-comparison]<br>- [Modular Division][modular-division]<br>- % operator                                                                                                                                                                                                                                                   	|  Completed                                                                                                       	|  Completed                              	|  [Currency Exchange](https://github.com/exercism/python/tree/main/exercises/concept/currency-exchange)                         	|
|  operator-overloading                     	|  - [Operator overloading][operator-overloading]                                                                                                                                                                                                                                                                                                                                                                                                            	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  other-comprehensions                     	|  - [Set comprehension][set-comprehension]<br>- [Dict comprehension][dict-comprehension]                                                                                                                                                                                                                                                                                                                                                                         	|  [#2294 ](https://github.com/exercism/python/issues/2294)                                                        	|  [ ]()                                  	|                                                                                                                                	|
|  raising and handling errors              	|  - [Exceptions][exceptions-general]<br>- [Exception catching][exception-catching]<br>- [Exception handling][exception-handling]<br>- [Exception message][exception-message]<br>- [raise][raise]<br>- [try][keyword-try]<br>- [except][keyword-except]<br>- [finally][keyword-finally]                                                                                                                                                                                        	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  regular-expressions                      	|  - [Regular Expressions][regular-expressions]<br>- `re`<br>- `re.find`<br>- `re.sub`<br>- `re.search`<br>- re.compile`                                                                                                                                                                                                                                                                                                                                                    	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  rich-comparisons                         	|  - [Rich comparison methods][rich-comparison-methods]<br>- `operator-overloading`                                                                                                                                                                                                                                                                                                                                                                           	|  [#2171](https://github.com/exercism/python/issues/2287)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  sequences and common sequence operations 	|  - [Bracket notation][bracket-notation]<br>- [Indexing][indexing]<br>- [slice][builtin-types-slice]<br>- [Slicing][slicing]<br>- slice assignment                                                                                                                                                                                                                                                                                                                          	|  [#2290](https://github.com/exercism/v3/#2290)                                                                   	|  [ ]()                                  	|                                                                                                                                	|
|  sets                                     	|  - [set][builtin-types-set]<br>- [frozenset][builtin-types-frozenset]<br>- set operations<br>- set operators<br>- set methods                                                                                                                                                                                                                                                                                                                                        	|  [#2296 ](https://github.com/exercism/python/issues/2296)                                                        	|  [ ]()                                  	|                                                                                                                                	|
|  string-formatting                        	|  - [String formatting][string-formatting]                                                                                                                                                                                                                                                                                                                                                                                                                  	|                                                                                                                  	|  Completed                              	|  [pretty-leaflet](https://github.com/exercism/python/tree/main/exercises/concept/pretty-leaflet)                               	|
|  string-methods                           	|  - [String methods][string-methods]                                                                                                                                                                                                                                                                                                                                                                                                                        	|  Completed                                                                                                       	|  Completed                              	|  [Litte Sister's Essay](https://github.com/exercism/python/tree/main/exercises/concept/little-sisters-essay)                   	|
|  string-methods-splitting                 	|  - [String splitting][string-splitting]                                                                                                                                                                                                                                                                                                                                                                                                                    	|                                                                                                                  	|  [ ]()                                  	|                                                                                                                                	|
|  strings                                  	|  - [str][builtin-types-str]                                                                                                                                                                                                                                                                                                                                                                                                                                	|  N/A                                                                                                             	|  Completed                              	|  [Processing Logs](https://github.com/exercism/python/tree/main/exercises/concept/processing-logs)                             	|
|  testing                                  	|  - [assert][keyword-assert]<br>- `unittest`<br>- `doctest`                                                                                                                                                                                                                                                                                                                                                                                                     	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  text-processing                          	|                                                                                                                                                                                                                                                                                                                                                                                                                                                          	|  [ ]()                                                                                                           	|                                         	|                                                                                                                                	|
|  tuples                                   	|  - [tuple][builtin-types-tuple]                                                                                                                                                                                                                                                                                                                                                                                                                            	|  Completed                                                                                                       	|  Completed                              	|  [Tisbury Treasure Hunt](https://github.com/exercism/python/tree/main/exercises/concept/tisbury-treasure-hunt)                 	|
|  type-hinting                             	|  - [Type hinting][type-hinting]                                                                                                                                                                                                                                                                                                                                                                                                                            	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  unicode regular expressions     |  - regular expressions<br>- unicode<br>- `                                                                                                                                                                                                                                                                                                                                                                                                                            	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  unpacking and multiple assignment        	|  - [Argument unpacking][argument-unpacking]<br>- splat or astrix operator<br>- [Multiple assignment][multiple-assignment]<br>- [Tuple unpacking][tuple-unpacking]                                                                                                                                                                                                                                                                                                       	|  [#2360](https://github.com/exercism/python/issues/2360)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  user-defined errors                      	|  - [Exception hierarchy][exception-hierarchy]<br>- Custom Exceptions<br>- subclassing Exception<br>- custom error messages                                                                                                                                                                                                                                                                                                                                        	|  [ ]()                                                                                                           	|                                         	|                                                                                                                                	|
|  walrus operator                          	|  - assignment expression, `:=`                                                                                                                                                                                                                                                                                                                                                                                                                             	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  `with` statement (_context-managers_)    	|  - [with][keyword-with]<br>- `context-handling`<br>- `context-managers`<br>- [finally][keyword-finally]<br>- file handling                                                                                                                                                                                                                                                                                                                                           	|  [#2369](https://github.com/exercism/python/issues/2369)                                                         	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Composition][composition-general]                                                                                                                                                                                                                                                                                                                                                                                                                      	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Data Structures][data-structures]                                                                                                                                                                                                                                                                                                                                                                                                                      	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Encapsulation][encapsulation-general]                                                                                                                                                                                                                                                                                                                                                                                                                  	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Interfaces][interfaces-general]                                                                                                                                                                                                                                                                                                                                                                                                                        	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Lookup efficiency][lookup-efficiency]                                                                                                                                                                                                                                                                                                                                                                                                                  	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Mutation][mutation-general]                                                                                                                                                                                                                                                                                                                                                                                                                            	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Mutability in Python][mutability]                                                                                                                                                                                                                                                                                                                                                                                                                      	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Polymorphism][polymorphism-general]                                                                                                                                                                                                                                                                                                                                                                                                                    	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Recursive data structures][recursive-data-structures]                                                                                                                                                                                                                                                                                                                                                                                                  	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Scope][scope]                                                                                                                                                                                                                                                                                                                                                                                                                                          	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [Standard Library][standard-library]                                                                                                                                                                                                                                                                                                                                                                                                                    	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*general                                	|  - [State][state]                                                                                                                                                                                                                                                                                                                                                                                                                                          	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Duck Typing][duck-typing]                                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Dynamic Typing][dynamic-typing]                                                                                                                                                                                                                                                                                                                                                                                                                        	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [del][keyword-del]                                                                                                                                                                                                                                                                                                                                                                                                                                      	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Expressions][expressions]                                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Identity testing][identity-testing]                                                                                                                                                                                                                                                                                                                                                                                                                    	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Operators][operators]                                                                                                                                                                                                                                                                                                                                                                                                                                  	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Operator precedence][operator-precedence]                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Order of Evaluation][order-of-evaluation]                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [type][builtin-types-type]                                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [type conversion][type-conversion]                                                                                                                                                                                                                                                                                                                                                                                                                      	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Immutability in Python][immutability]                                                                                                                                                                                                                                                                                                                                                                                                                  	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Operators][operators]                                                                                                                                                                                                                                                                                                                                                                                                                                  	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [Order of Evaluation][order-of-evaluation]                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [type][builtin-types-type]                                                                                                                                                                                                                                                                                                                                                                                                                              	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
|  \*no stand-alone                         	|  - [type conversion][type-conversion]                                                                                                                                                                                                                                                                                                                                                                                                                      	|  [ ]()                                                                                                           	|  [ ]()                                  	|                                                                                                                                	|
_Concepts flagged as **general** are broad enough that we are questioning if they need a specific concept exercise._
<br>
_Concepts flagged **no stand alone** are explained/utilized across multiple concept exercises._
