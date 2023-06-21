# Instruction append
Here's an example of what's expected:
```python
>>> meeting_time("06/21/2023", {
        110: (5.5, "08:00 AM", "05:00 PM"),
        111: (-10, "12:00 PM", "09:00 PM"),
        112: (3, "04:00 AM", "01:00 PM"),
        113: (-4, "04:00 PM", "01:00 AM")
    })
{
    "03:00 AM": {
        110: "06/21/2023 08:30 AM",
        111: "06/20/2023 05:00 PM",
        112: "06/21/2023 06:00 AM",
        113: "06/20/2023 11:00 PM",
    },
    "4:00 AM": {
        110: "06/21/2023 09:30 AM",
        111: "06/20/2023 06:00 PM",
        112: "06/21/2023 07:00 AM",
        113: "06/21/2023 12:00 AM",
    },
}
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