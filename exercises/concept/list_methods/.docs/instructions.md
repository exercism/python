You own a theme park. And for some reason, you own only one ride. The biggest roller coaster in the world. Although, you have only one ride, people stand in line for hours for the ride.

You do have 2 queues for this ride.

1. Normal Queue
2. Express Queue ( Also known as Fast-track Queue) - people pay extra to get faster access to the ride.

You are given a tasks to finish the following functions for the completion of this exercise.

## 1. Add Me to the queue

Define the `add_me_to_the_queue()` function that takes 4 parameters `express_queue, normal_queue, ticket_type, person_name` and returns the queue to which the person is added.

1. express queue is a list
2. normal queue is a list
3. ticket_type is a int in which 1 means he belongs to express queue, 0 means he belongs to normal queue.
4. person name is the name of the person to be added to the respective queue.

Once you have added the name to the respective queue, returned the added queue,

```python
add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich")
# => ["Tony", "Bruce", "RichieRich"]

add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye")
# => ["RobotGuy", "WW", "HawkEye"]
```

## 2. Where are my friends

One guy came late to the park and wants to join with his friends. He doesn't know where they are standing but wants to join with them.

Define the `find_his_friend()` function that takes 2 parameters `queue, friend_name`.

1. Queue is the list of people standing in the queue.
2. friend_name is the name of the friend who's index you need to find.

Indexing starts from 0.

```python
find_his_friend(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], friend_name="Steve")
# => 1
```

## 3. Can I please join with them?

Define the `add_person_with_his_friends()` function that takes 3 parameters `queue, index, person_name`.

1. Queue is the list of people standing in the queue.
2. index is the location the person has to be added
3. person_name is the name of the person to add at that index.

```python
add_person_with_his_friends(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], index=1, person_name="Bucky")
# => ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"]
```

## 4. Mean person in the queue

You just heard from the queue that there is a mean person in the queue and you need to throw him out.

Define the `remove_the_mean_person()` function that takes 2 parameters `queue, person_name`.

1. Queue is the list of people standing in the queue.
2. person_name is the name of the person whom we need to kick out.

```python
remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")
#=> ["Natasha", "Bucky", "Steve", "Wanda", "Rocket"]
```

# 5. DoppelGangers

You may not have seen 2 people look like the same person before but you sure would have seen people with the same name. It looks like today you are seeing the same scenario. You want to know how many times a name has occured in the queue.

Define the `how_many_dopplegangers()` function that takes 2 parameters `queue, person_name`.

1. Queue is the list of people standing in the queue.
2. person_name is the name of the person whom you think have been occuring more than once in the queue.

Return the number of occurances of the name, in `int` format.

```python
how_many_dopplegangers(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")
#=> 2
```

## 6. Remove the last guy

There is an overcrowd in the queue and you need to remove the last person out. You will have to define the function `remove_the_last_person()` that takes 1 parameter `queue` which will be called again and again till the queue count is back to normal. Queue is the list of people standing in the queue.

You should also return the name of the person who was removed.

```python
remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
#=> Rocket
```

## 7. Sort the Queue List

For Admin Purpose, you need the list of names in the queue in sorted order.

Define the `sorted_names()` function that takes 1 parameter `queue`. Queue is the list of people standing in the queue.

```python
sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
#=>['Natasha', 'Natasha', 'Rocket', 'Steve', 'Eltran']
```
