# Instructions

Chaitana owns a very popular theme park. She only has one ride in the very center of beautifully landscaped grounds: The Biggest Roller Coaster in the World(TM). Although there is only this one attraction, people travel from all over the world and stand in line for hours for the opportunity to ride Chaitana's hypercoaster.

There are two queues for this ride, represented as `list`s:

1. Normal Queue
2. Express Queue (Also known as the Fast-track) - where people pay extra for priority access.

You've been asked to write some code to better manage the guests at the park. You need to implement the following functions as soon as possible before the guests (and your boss, Chaitana!) get cranky.

## 1. Add me to the queue

Define the `add_me_to_the_queue()` function that takes 4 parameters `express_queue, normal_queue, ticket_type, person_name` and returns the queue with the person's name added.


1. ticket_type is an `int` with 1 == express_queue and 0 == normal_queue.
2. person_name is the name (as a `str`) of the person to be added to the respective queue.

Once you have added the name to the appropriate queue, return the queue that includes the new person.

```python
>>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich")
["Tony", "Bruce", "RichieRich"]

>>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye")
["RobotGuy", "WW", "HawkEye"]
```

## 2. Where are my friends

One person arrived late at the park but wants to join the queue with his friends. He has no idea where they're standing, and he can't get any reception to call them.

Define the `find_my_friend()` function that takes 2 parameters `queue, friend_name`.

1. queue is the list of people standing in the queue.
2. friend_name is the name of the friend whose index you need to find.

Indexing starts at 0.

```python
>>> find_my_friend(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], friend_name="Steve")
1
```

## 3. Can I please join them?

Define the `add_me_with_my_friends()` function that takes 3 parameters `queue, index, person_name`.

1. queue is the list of people standing in the queue.
2. index is the position at which the person should be added.
3. person_name is the name of the person to add at this position.

```python
>>> add_me_with_my_friends(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], index=1, person_name="Bucky")
["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"]
```

## 4. Mean person in the queue

You just heard from the queue that there is a really mean person shoving, shouting, and making trouble. You need to throw that miscreant out for bad behavior.

Define the `remove_the_mean_person()` function that takes 2 parameters `queue, person_name`.

1. queue is the list of people standing in the queue.
2. person_name is the name of the person whom we need to kick out.

```python
>>> remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")
["Natasha", "Steve", "Wanda", "Rocket"]
```

# 5. Namefellows

You may not have seen two unrelated people who look exactly the same, but you've _definitely_ seen unrelated people with the same exact name (_namefellows or doppelgängers_)! It looks like today there are a lot of them. You want to know how many times a particular name occurs in the queue.

Define the `how_many_namefellows()` function that takes 2 parameters `queue, person_name`.

1. queue is the list of people standing in the queue.
2. person_name is the name you think might occur more than once in the queue.

Return the number of occurrences of person_name, as an `int`.

```python
>>> how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")
2
```

## 6. Remove the last person

Sadly, it's overcrowded in the queue today and you need to remove the last person in line (_you'll give them a voucher to come back in the fast track another time_). You'll have to define the function `remove_the_last_person()` that takes 1 parameter `queue`, which is the list of people standing in the queue.

You should also return the name of the person who was removed, so you can write them a voucher.

```python
>>> remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
'Rocket'
```

## 7. Sort the Queue List

For administrative purposes, you need to get the names in alphabetical order.

Define the `sorted_names()` function that takes 1 argument: `queue`, which is the list of people standing in the queue, and returns a sorted copy of the list.

```python
>>> sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
['Eltran', 'Natasha', 'Natasha', 'Rocket', 'Steve']
```
