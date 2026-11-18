# Instructions

Your classmate Thallia has just won an internship with the city's premier tram company.
Her goal for the term of the internship is to improve communications with the ridership and promote special services.
She's decided to focus on writing several apps that can run on station platforms, the tram website, and rider's phones.
Since writing all these apps is a big task, she's asked that the tram company recruit you to help with the project.

1. Schedules by Weekday Number

First on the agenda is an app that can help commuters navigate the various schedules so they can more easily get to and from work.
Thallia's got the lines and locations mostly figured out, but would like you to write a function that will filter the timetable sequence for a given weekday, so riders can clearly see all the departure times.
The aim will be to return tram departure times from the timetable based on a weekday number (_0 being Monday, 6 being Sunday_).
Write the `time_table_for_a_weekday` function that takes a nested sequence of timetables and weekday number.
It should return the schedule sequence corresponding to the weekday number.

```python
>>> time_table_for_a_weekday([["8:00", "17:00"], ("9:00", "16:00"), ("8:30", "15:00"), ["10:00", "19:00", "21:00"], ["12:00", "20:00"], ("9:00", "19:00"), ("9:30", "15:00", "20:00")], 3)
["10:00", "19:00", "21:00"]
```

2. Departures by Commute Window

Now that you have the weekday filtering figured out, Thallia has asked you to drill down into specific commute times.
This part of the app is designed to allow a commuter to input their commute day plus a "commute window" and receive a sequence of departure times.
With the `time_table_for_a_specific_range` function that takes a sequence of daily timetables, a weekday number, and `start`/`stop` indexes for the "commute window".
It should return a sequence of departure times for the commuter that fits their travel day and "commute window".

```python
>>> time_table_for_a_specific_range([["8:00", "17:00"], ("9:00", "16:00"), ("8:30", "15:00"), ["10:00", "19:00", "21:00"], ["12:00", "20:00"], ("9:00", "19:00"), ("9:30", "15:00", "20:00", "21:00")], 6, 1, 3)
("15:00", "20:00")
```

3. Calculate Route with Fewest Transfers

The tram system has many routes and many different ways for commuters to reach their destinations.
However, transferring adds time and complexity to the process.
Thallia is trying to tackle this in-app by asking you to add a feature that will calculate routes with the fewest transfers.

4. Calculate Fastest Route

To up the tram company's visibility, Thallia has decided to add functionality similar to Googles "plan a trip" functionality.
But instead of providing all routes and times, she'd like you to provide commuters only with the fastest available routes listed in the timetables.

5. Update Station Status Displays

Having built up commuter features, Thallia now wants to focus a bit on weekend "family activity" services.
She'd like to update the station display software to better promote different activities (concerts, museums, amusement parks, zoos, sports matches, theater) that can be reached via different tram lines.
She's asked you to write a function that will insert a short blurb about an activity into the arrival and departure displays.

6. Update Weekend Schedule Information

Thallia would also like to update the app so that weekend riders can know when an event is scheduled and what train departures will get them to the activities on time.
She'd like you to write a function that will insert an activity description and start time into a given schedule display, so that riders are reminded that they can take the tram to the activity.
