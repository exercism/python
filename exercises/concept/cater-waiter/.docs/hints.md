# Hints

## General

- [Sets][sets] are mutable, unordered collections with no duplicate elements.
- Sets can contain any data type, as long as all elements are [hashable][hashable].
- Sets are [iterable][iterable].
- Sets are most often used to quickly dedupe other collections or for membership testing.
- Sets also support mathematical operations like `union`, `intersection`, `difference`, and `symmetric difference`

## 1. Clean up Dish Ingredients

- The `set()` constructor can take any [iterable][iterable] as an argument. [concept: lists](/tracks/python/concepts/lists) are iterable.
- Remember: [concept: tuples](/tracks/python/concepts/tuples) can be formed using `(<element_1>, <element_2>)` or via the `tuple()` constructor.

## 2. Cocktails and Mocktails

- A `set` is _disjoint_ from another set if the two sets share no elements.
- The `set()` constructor can take any [iterable][iterable] as an argument. [concept: lists](/tracks/python/concepts/lists) are iterable.
- In Python, [concept: strings](/tracks/python/concepts/strings) can be concatenated with the `+` sign.

## 3. Categorize Dishes

- Using [concept: loops](/tracks/python/concepts/loops) to iterate through the available meal categories might be useful here.
- If all the elements of `<set_1>` are contained within `<set_2>`, then `<set_1> <= <set_2>`.
- The method equivalent of `<=` is `<set>.issubset(<iterable>)`
- [concept: tuples](/tracks/python/concepts/tuples) can contain any data type, including other tuples.  Tuples can be formed using `(<element_1>, <element_2>)` or via the `tuple()` constructor.
- Elements within [concept: tuples](/tracks/python/concepts/tuples) can be accessed from the left using a 0-based index number, or from the right using a -1-based index number.
- The `set()` constructor can take any [iterable][iterable] as an argument. [concept: lists](/tracks/python/concepts/lists) are iterable.
- [concept: strings](/tracks/python/concepts/strings) can be concatenated with the `+` sign.

## 4. Label Allergens and Restricted Foods

- A set _intersection_ are the elements shared between `<set_1>` and `<set_2>`.
- The set method equivalent of `&` is `<set>.intersection(<iterable>)`
- Elements within [concept: tuples](/tracks/python/concepts/tuples) can be accessed from the left using a 0-based index number, or from the right using a -1-based index number.
- The `set()` constructor can take any [iterable][iterable] as an argument.  [concept: lists](/tracks/python/concepts/lists) are iterable.
- [concept: tuples](/tracks/python/concepts/tuples) can be formed using `(<element_1>, <element_2>)` or via the `tuple()` constructor.

## 5. Compile a "Master List" of Ingredients

- A set _union_ is where `<set_1`> and `<set_2>`  are combined into a single `set`
- The set method equivalent of `|` is `<set>.union(<iterable>)`
- Using [concept: loops](/tracks/python/concepts/loops) to iterate through the various dishes might be useful here.

## 6. Pull out Appetizers for Passing on Trays

- A set _difference_ is where the elements of  `<set_2>`  are removed from `<set_1>`, e.g. `<set_1> - <set_2>`.
- The set method equivalent of `-` is `<set>.difference(<iterable>)`
- The `set()` constructor can take any [iterable][iterable] as an argument. [concept: lists](/tracks/python/concepts/lists) are iterable.
- The [concept: list](/tracks/python/concepts/lists) constructor can take any [iterable][iterable] as an argument. Sets are iterable.

## 7. Find Ingredients Used in Only One Recipe

- A set _symmetric difference_ is where  elements appear in `<set_1>` or `<set_2>`, but not **_both_** sets.
- A set _symmetric difference_ is the same as subtracting the `set` _intersection_ from the `set` _union_, e.g. `(<set_1> | <set_2>) - (<set_1> & <set_2>)`
- A _symmetric difference_ of more than two `sets` will include elements that are repeated more than two times across the input `sets`.  To remove these cross-set repeated elements, the _intersections_ between set pairs needs to be subtracted from the symmetric difference.
- Using [concept: loops](/tracks/python/concepts/loops) to iterate through the various dishes might be useful here.


[hashable]: https://docs.python.org/3.7/glossary.html#term-hashable
[iterable]: https://docs.python.org/3/glossary.html#term-iterable
[sets]: https://docs.python.org/3/tutorial/datastructures.html#sets