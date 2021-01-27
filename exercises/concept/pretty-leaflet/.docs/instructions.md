Your acquaintance Erin needs to print thousands of handbills for multiple events and they need your help! They've asked you to create the layout for a leaflet containing a header, an optional date, and a list of artists -- each associated with a _unicode icon_. The goal is to `print` and distribute your cool new leaflet design - and you'll need all your Python string formatting skills to succeed.

## 1. Create the class with a capitalized header

The `Leaflet` class wraps all the instance variables and methods needed to create the leaflet. Implement that class, the header instance variable correspond to the first argument of the constructor.

The constructor should take three parameters: the header of type `str`, one `list` of artists and one `list` of unicode code points.

The header should be capitalized as illustrated in this example.

```python
>>> Leaflet("title", [], []).header
"Title"
```

## 2. Add an optional date

Implement a new method `set_date(day, month, year)` for your class with an _optional_ `Month, Day, Year` parameter. The values passed in as arguments should be formatted like this: **`December 6, 2021`**. If this method doesn't get called, the instance variable **`date`** should be an _empty string_.

```python
>>> leaflet = Leaflet("title", [], [])
>>> leaflet.date
""
>>> leaflet.set_date(21, 2, 2020)
>>> leaflet.date
"February 21, 2020"
>>> leaflet.set_date(30, 3)
>>> leaflet.date
"March 30, 2020"
```

## 3. Render the unicode code points as icons

When the method `get_icons` is called, the list of unicode code points passed as the third argument in the constructor should be rendered and returned as a `list` of _icons_.

```python
>>> leaflet = Leaflet("title", [], ['\U00000040', '\U0001D70B'])
>>> leaflet.get_icons()
['@', '𝜋']
```

## 4. Display the finished leaflet

The method `print_leaflet()` should return the finished leaflet, the poster should abide by the layout below.

The leaflet follows a specific layout in the shape of a rectangle:

- The first and last rows contain 20 asterisks. `"*"`
- Each section is separated by an empty row above and below it.
- An empty row contains only one asterisk at the beginning and one at the end.
- The first section is the header of the leaflet, this title is capitalized.
- The second section is the option date, if the date is not defined, this section should be an empty row.
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
