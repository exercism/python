# `list`

Lists are dynamic arrays that can be resized by Python at runtime. They are homogenous, meaning they are able to hold any data type, including other lists, and can even contain themselves (recursive data structures are relatively simple in Python).

Simple flat lists are used extensively in [variable-length-quantity][variable-length-quantity], [markdown][markdown], and [robot-simulator][robot-simulator].

A multi-dimensional list-with-a-list is used as a simple (but not very efficient) matrix type in [matrix][matrix].

TODO: ADD MORE DETAIL

See the Python documentation entries for the [mutable][mutation] [`list` type][docs-list-type] and it's [constructor][list-as-function]. This is Python's most commonly used [sequential collection][docs-sequence-types], and as it allows _heterogenous data_ it's quite different from the [fixed array][general-concept-array] and [singly-linked list][general-concept-list] types you may have encountered in other, less flexible, languages.

[variable-length-quantity]: ../../exercise-concepts/variable-length-quantity.md
[markdown]: ../../exercise-concepts/markdown.md
[robot-simulator]: ../../exercise-concepts/robot-simulator.md
[matrix]: ../../exercise-concepts/matrix.md
[mutation]: ../../../../../reference/concepts/mutation.md
[general-concept-array]: ../../../../../reference/types/array.md
[general-concept-list]: ../../../../../reference/types/list.md
[docs-list-type]: https://docs.python.org/3/library/stdtypes.html#typesseq-list
[docs-list-as-function]: https://docs.python.org/3/library/stdtypes.html#list
[docs-sequence-types]: https://docs.python.org/3/library/stdtypes.html#typesseq
