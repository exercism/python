# Postfix Evaluation
## what is Postfix Evaluation?
_Postfix_ Expression _Evaluation_. A _postfix_ expression is a collection of operators and operands in which the operator is placed after the operands. That means, in a _postfix_ expression the operator follows the operands

## Interpreter Version
`Python 3.x` is used

## How to use
1. import _postfix_evaluation.py_ file
> `from postfix_evaluation import postfix_evaluation`

2. create an object of class _postfix_evaluation_ and pass string with integer value.
> number = "123+-"  
obj = postfix_evaluation(number)

3. call the `evaluate` method and print
> print(obj.evaluate())

## Limitations
+ This will not work on any **number greater than 9**
+ Floating number are not accepted
+ Invalid expression like `43+-` will raise an exception
## Contact Me
[**Email**](mailto:tbhaxor@gmail.com)
[**Github**](https://github.com/tbhaxor)
