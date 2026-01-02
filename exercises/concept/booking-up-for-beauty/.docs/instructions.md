# Instructions

In this exercise you'll be working on an appointment scheduler for a beauty salon in New York that opened on September 15th in 2012.

You have six tasks, which will all involve appointment dates.

## 1. Parse all-number appointment date

Implement the `schedule_numeric()` function to parse a textual representation of an appointment date into the corresponding `datetime.datetime` format.

Note that the input is in U.S.-style month/day/year order and numbers are zero-padded (so July is 07, not 7).

```python
schedule_numeric("07/25/2023 13:45:00")
// => datetime.datetime(2023, 7, 25, 13, 45, 0)
```

## 2. Parse mixed-format appointment date

Implement the `schedule_mixed()` function to parse a textual representation of an appointment date into the corresponding `datetime.datetime` format:

```python
schedule_mixed("Thursday, July 25, 2023 13:45:00")
// => datetime.datetime(2023, 7, 25, 13, 45, 0)
```

## 3. Check if an appointment has already passed

Implement the `has_passed()` function that takes an appointment date and checks if the appointment was somewhere in the past:

```python
has_passed(datetime.datetime(1999, 12, 31, 9, 0, 0))
// => True
```

## 4. Check if appointment is in the afternoon

Implement the `is_afternoon_appointment()` function that takes an appointment date and checks if the appointment is in the afternoon (>= 12:00 and < 18:00):

```python
is_afternoon_appointment(datetime.datetime(2023, 3, 29, 15, 0, 0))
// => True
```

## 5. Describe the time and date of the appointment

Implement the `description()` function that takes an appointment date and returns a description of that date and time:

```python
description(datetime.datetime(2023, 3, 29, 15, 0, 0))
// => "You have an appointment on 03/29/2023 03:00:00 PM."
```

## 6. Return the anniversary date

Implement the `anniversary_date()` function that returns this year's anniversary date, which is September 15th:

```python
anniversary_date()
// => datetime.date(2023, 9, 15)
```