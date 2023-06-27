# Instructions

Your task is to find out a time in which a set of your employees are working so that you can have an hour-long meeting.

Company policy allows employees to choose their own 9 hours of working time, inclusive of an hour break.
This is an important meeting, so if people need to attend during their break, the company will let them take an extra break/hour on another day within the month.


Given a collection of employee IDs with their time zones and working hours, return a collection of all possible meeting times, each of which should contain the local time and date for all employees listed.
Note that meetings should start "on the hour" in UTC - in other words, a meeting can't start at, 3:30, 12:10, or 17:45 UTC.
Local times, of course may vary.

Local time zones are represented as [UTC offsets][UTC offset].

All possible meeting start times should be reported.

[UTC offset]: https://en.wikipedia.org/wiki/UTC_offset
