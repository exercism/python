# Instructions

Your acquaintance Erin needs to print thousands of handbills for multiple events and they need your help! They've asked you to create the layout for a leaflet containing a header, an optional date, and a list of artists -- each associated with a _unicode icon_. The goal is to `print` and distribute your cool new leaflet design - and you'll need all your Python string formatting skills to succeed.

## 1. Create the class with a capitalized header

The `capitalize_header` function should take in an event name and return the capitalized version of the event name.

```python
>>> capitalize_header("fan meetup")
"Fan meetup"
```

## 2. Format the date

Create a new method `format_date` which takes in a list which contains a date, month, and a year. It displays the formatted date with the format `<month_name> <date>, <year>`

```python
>>> convert_date([9, 4, 2020])
>>> leaflet.date
"April 9, 2020"
>>> leaflet.set_date([13, 5, 2030])
>>> leaflet.date
"May 13, 2030"
```

## 3. Render the unicode code points as icons

When the method `display_icons` is called, the list of unicode code points passed should be rendered and returned as a `list` of _icons_.

```python
>>> leaflet.display_icons(['\U00000040', '\U0001D70B'])
['@', '𝜋']
```

## 4. Display the finished leaflet

Now you will use all the functions above, and combine them in the `print_leaflet` function.
It should take an `event_name`, a list of `icons`, a list of `authors`, and an `event_date` list.

The poster should abide by the layout below.

The leaflet follows a specific layout in the shape of a rectangle:

- The first and last rows contain 20 asterisks. `"*"`
- Each section is separated by an empty row above and below it.
- An empty row contains only one asterisk at the beginning and one at the end.
- The first section is the header of the leaflet, this title is capitalized.
- The second section is the option date, if the date is not passed, this section should be an empty row.
- The third and last section is the list of the artists, each artist associated with the corresponding icon.

```python
********************
*                  *
*    'Concert'     *
*                  *
*  June 22, 2020   *
*                  *
* John         🎸  *
* Benjamin     🎤  *
* Max          🎹  *
*                  *
********************
```
