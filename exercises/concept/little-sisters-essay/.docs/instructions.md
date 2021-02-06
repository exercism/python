In this exercise, you are helping your younger sister edit her paper for school. The teacher is looking for correct punctuation, grammar, and excellent choice of words.

You have four tasks to clean up and modify strings.

## 1. Capitalize the title of the paper

Any good paper needs a properly formatted title. Implement the function `capitalize_title()` which takes `title` as parameter and capitalizes the first letter of each word of the title. This function will return a `str`.

```python
>>> capitalize_title("my hobbies")
"My Hobbies"
```

## 2. Check if each sentence ends with a period

You want to make sure that the punctuation in the paper is perfect. Implement the function `check_sentence_ending()` that takes `sentence` as a parameter. This function should return a `bool`.

```python
>>> check_sentence_ending("I like to hike, bake, and read.")
True
```

## 3. Clean up spacing

For the paper to look professional, you need to remove unnecessary spacing. Implement the function `remove_extra_spaces()` which takes `sentence` as a parameter and removes any extra whitespace at the beginning and the end of the sentence. This function should return a `str`.

```python
>>> remove_extra_spaces(" I like to go on hikes with my dog.  ")
"I like to go on hikes with my dog."
```

## 4. Replace words with a synonym

To make the paper even better, you can replace some of the adjectives with synonyms. Write a function `replace_word_choice()` that takes `sentence`, `old_word`, and `new_word` as parameters. This function should replace all instances of the `old_word` with the `new_word` and return the updated sentence. The function should return a `str`.

```python
>>> replace_word_choice("I bake good cakes.", "good", "amazing")
"I bake amazing cakes."
```
