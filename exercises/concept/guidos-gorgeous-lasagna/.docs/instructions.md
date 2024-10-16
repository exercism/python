# Instructions

You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

You have five tasks, all related to cooking your recipe.

<br>

~~~~exercism/note
We have started the first function definition for you in the stub file, but you will need to write the remaining function definitions yourself.
You will also need to define any constants yourself.
Read the #TODO comment lines in the stub file carefully.
Once you are done with a task, remove the TODO comment.
~~~~

<br>

## 1. Define expected bake time in minutes as a constant

Define the `EXPECTED_BAKE_TIME` [constant][constants] that represents how many minutes the lasagna should bake in the oven.
According to your cookbook, the Lasagna should be in the oven for 40 minutes:

```python
>>> print(EXPECTED_BAKE_TIME)
40
```

## 2. Calculate remaining bake time in minutes

Complete the `bake_time_remaining()` function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the `EXPECTED_BAKE_TIME` constant.

```python
>>> bake_time_remaining(30)
10
```


## 3. Calculate preparation time in minutes

Define the `preparation_time_in_minutes()` [function][functions] that takes the `number_of_layers` you want to add to the lasagna as an argument and returns how many minutes you would spend making them.
Assume each layer takes 2 minutes to prepare.

```python
>>> def preparation_time_in_minutes(number_of_layers):
        ...
        ...
        
>>> preparation_time_in_minutes(2)
4
```


## 4. Calculate total elapsed cooking time (prep + bake) in minutes

Define the `elapsed_time_in_minutes()` function that takes two parameters as arguments: `number_of_layers` (_the number of layers added to the lasagna_) and `elapsed_bake_time` (_the number of minutes the lasagna has been baking in the oven_).
This function should return the total number of minutes you have been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

```python
>>> def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
        ...
        ...
        
>>> elapsed_time_in_minutes(3, 20)
26
```


## 5. Update the recipe with notes

Go back through the recipe, adding "notes" in the form of [function docstrings][function-docstrings].

```python
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
```

[constants]: https://stackoverflow.com/a/2682752
[functions]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[function-docstrings]: https://docs.python.org/3/tutorial/controlflow.html#documentation-strings
