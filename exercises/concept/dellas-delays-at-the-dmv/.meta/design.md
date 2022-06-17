## 🎯 Goal

This `functions` concept exercise is meant to teach a deeper understanding and use of `functions`  in Python. It should also explain how Python treats/views functions (_as callable objects_), and dig into some of the features that make Python `functions` unique.


<br>

## 💡Learning objectives

- Understand more about  Python `scopes` and `namespaces`
  - understand the difference between the `global` and `nonlocal` keywords and when to use them
- Get familiar with the [special attributes](https://docs.python.org/3/reference/datamodel.html#types) of Python functions
- Get familiar with best practices when using `return`, and the difference between _explicit_ and _implicit_ `return`
   - functions without an explicit return will return the singleton object `None`
- Understand what is meant by _"functions are first class **objects** in Python"_.
  - understand that `functions` **are** `objects` in Python, and that they have `types`
  - understand that `functions` can be assigned to variables, used in expressions,  and stored in various data structures such as `dicts` or `lists`
  - create `functons` that are assigned to variables, used in expressions, and stored in different data structures.
  - understand and create` functions` that are/can be nested inside one another
- Understand that Python considers a function a form of  `callable object`. 
- Understand that a user-defined `function object` is created by a `function definition`.

<br>

## 🤔 Concepts

- `callable objects`
- `first-class functions`
- `global`
- `nested functions`
- `nonlocal`
- `return`, `implicit return`, `explicit return`
- `scope`
-  special `function attributes`

<br>

## 🚫 Topics that are Out of scope


<br>
<details>
<summary><b>Concepts & Subjects that are Out of Scope</b> (<em>click to expand</em>)</summary>
<br>

- `named parameters` (_these can be touched on if needed_)
-  `default parameters` (_these can be touched on, if needed_)
- `arbitrary parameters`
- `*args & **kwargs`
- `keyword-only arguments`
- `/` and `*` for requiring parameter types
-  `functions-as-arguments` (_this can be mentioned, but shouldn't be required for the exercise_)
- `functions-as-returns`(_this can be mentioned, but will be covered in-depth in `higher-order functions`)
- `closures` (_these will be covered in a different exercise_)
- `decorators` (_these will be covered in a different exercise_)
-  `functools.wraps` (_this is used mostly for decorators_)
-  `functools` (_this will get its own exercise_)
- `comprehensions`
- `generators`
- `lambda`, `anonymous functions` (_these will be covered in a different exercise_)
- `recursion`

</details>
<br>


## ↩️  Prerequisites

_These are the concepts/concept exercises the student needs to complete/understand before solving this concept exercise.  Since `functions` is a "meta" topic,  these will probably need to be adjusted to fit the parameters of the exercise._ 

<details>
<summary>Prereqs  (<em>click to expand</em>)</summary>
<br>

- `basics`
- `bools`
- `comparisons`
- `lists`
- `list-methods`
- `loops`
- `numbers`
- `strings`
- `string-methods`

</details>

<br>

##  📚 Resources for Writing and Reference

<details>
<summary><b>Resources</b> (<em>click to expand</em>)</summary>
<br>

- [Python Docs: Naming and Binding](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding)
- [Python Docs: Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Function definitions (Python Library Reference)](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [Dan Bader:  Python s Functions are First-Class](https://dbader.org/blog/python-first-class-functions)
- [Real Python:  Python Scope & the LEGB Rule](https://realpython.com/python-scope-legb-rule/)
- [Stack Overflow: Short Description of Python's Scoping Rules?](https://stackoverflow.com/questions/291978/short-description-of-the-scoping-rules)
- [Real Python: Python Inner Functions: What are they Good For?](https://realpython.com/inner-functions-what-are-they-good-for/)
- [Stack Abuse: How to Use global and nonlocal variables in Python](https://stackabuse.com/how-to-use-global-and-nonlocal-variables-in-python/)
- [The `nonlocal` Statement (Python Docs)](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
- [The `global` Statement (Python Docs)](https://docs.python.org/3/reference/simple_stmts.html#global)
- [Real Python: The Python return Statement: Usage and Best Practices](https://stackabuse.com/how-to-use-global-and-nonlocal-variables-in-python/)
- [Calls (Python Library Reference)](https://docs.python.org/3/reference/expressions.html#calls)
- [Is it a Class or a Function?  It's a Callable! (Trey Hunner)](https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/)
- [Callables in Python (Vimal A.R Blog)](https://arvimal.blog/2017/08/09/callables-in-python/)
- [Functions as Objects in Python](https://medium.com/python-pandemonium/function-as-objects-in-python-d5215e6d1b0d) -- _this is a subscription-based medium blog, so not good for hints or links_
- [Python Datamodel: Types](https://docs.python.org/3/reference/datamodel.html#types)

</details>
