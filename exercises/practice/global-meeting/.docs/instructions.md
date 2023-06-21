# Instructions

Your task is to find out a time in which a set of your employees are working so that you can have an hour-long meeting.

Company policy allows employees to choose their own 9 hours of working time, inclusive of an hour of break, and you don't mind if people are eating during the meeting.


Take in a collection of employee IDs with their time zones and working hours, and return a collection of all possible meeting times, each of which should contain the local time and date for all employees.
Note that the meeting should start and end corresponding with a UTC hour - that is, a meeting can't start at say, 3:30 UTC.

Time zones are represented as UTC offsets.

All possible meeting start times must be reported.
