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

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). 
When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. 
This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.




Admittedly, you're a little eccentric. 
You might provide working hours that are more or less than 9 - in which case you want the program to call out your error:

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:
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