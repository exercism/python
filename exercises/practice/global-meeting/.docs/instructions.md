# Instructions

Your task is to find out a time in which a set of your employees are working so that you can have an hour-long meeting.

Company policy allows employees to choose their own 9 hours of working time, inclusive of an hour of break, and you don't mind if people are eating during the meeting.


Take in a dictionary of employee IDs with their time zones and working hours, and return all possible meeting times in UTC.
Note that the meeting should start and end corresponding with a UTC hour - that is, a meeting can't start at say, 3:30 UTC.

Time zones are stored as a number which represents the difference from UTC.

All possible meeting start times must be reported.
```python
>>> meeting_time({
        110: [5.5, (9, 17)],
        111: [-10, (12, 21)],
        112: [3, (4, 13)],
        113: [-4, (15, 0)]
    })
[3]
```

## Errors
Admittedly, you're a little eccentric. 
You might provide working hours that are more or less than 9 - in which case you want the program to call out your error:
```
>>> meeting_time({
        201: [2, (5, 15)],
        202: [5, (13, 22)],
    })
ValueError: some employees are working for more or less than 9 hours 
```

If there's no possible meeting period, then you have to reshuffle teams.
Until then, your code should raise an error:
```
>>> meeting_time({
        201: [5, (5, 14)],
        202: [2, (13, 22)],
    })
ValueError: there's no possible meeting time for the provided employees
```
