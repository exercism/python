# Instructions

You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

You have five tasks, all related to cooking your recipe.

## 1. Define expected bake time in minutes

Define an `EXPECTED_BAKE_TIME` constant that returns how many minutes the lasagna should bake in the oven.
According to your cookbook, the Lasagna should be in the oven for 40 minutes:

```python
>>> import lasagna
>>> lasagna.EXPECTED_BAKE_TIME
40
```

## 2. Calculate remaining bake time in minutes

Implement the `bake_time_remaining()` function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the `EXPECTED_BAKE_TIME`.

```python
>>> from lasagna import bake_time_remaining
>>> bake_time_remaining(30)
10
```

## 3. Calculate preparation time in minutes

Implement the `preparation_time_in_minutes()` function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them.
Assume each layer takes 2 minutes to prepare.

```python
>>> from lasagna import preparation_time_in_minutes
>>> preparation_time_in_minutes(2)
4
```

## 4. Calculate total elapsed cooking time (prep + bake) in minutes

Implement the `elapsed_time_in_minutes()` function that has two parameters: `number_of_layers` (_the number of layers added to the lasagna_) and `elapsed_bake_time` (_the number of minutes the lasagna has been baking in the oven_).
This function should return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

```python
>>> from lasagna import elapsed_time_in_minutes
>>> elapsed_time_in_minutes(3, 20)
26
```

## 5. Update the recipe with notes

Go back through the recipe, adding notes and documentation.

```python
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
```
