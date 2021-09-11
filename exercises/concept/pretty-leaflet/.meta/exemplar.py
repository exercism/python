import calendar
from typing import List, Optional


CENTER_FORMAT = "*{: ^18}*"
FULL_ROW = "*" * 20
EMPTY_ROW = CENTER_FORMAT.format("")

def capitalize_header(event_name: str) -> str:
    return event_name.capitalize()

def format_date(event_date: List[int]) -> str:
    date, month, year = event_date
    month_name = calendar.month_name[month]
    return "{} {}, {}".format(month_name, date, year)

def display_icons(icons: List[str]) -> List[str]:
    displayed = []
    for icon in icons:
        displayed.append(u"{}".format(icon))
    return displayed

def print_leaflet(event_name: str, icons: List[str], authors, event_date: Optional[List[int]]=None):
    event_name = capitalize_header(event_name)
    date_string = format_date(event_date)
    icons = display_icons(icons)

    poster = []
    poster.append(FULL_ROW)
    poster.append(EMPTY_ROW)
    poster.append(CENTER_FORMAT.format("'" + event_name + "'"))
    poster.append(EMPTY_ROW)
    poster.append(CENTER_FORMAT.format(date_string))
    poster.append(EMPTY_ROW)
    for i, author in enumerate(authors):
        current_icon = icons[i] if i < len(icons) else " "
        space_width = 17 - len(current_icon) - len(author)
        poster.append(CENTER_FORMAT.format(" {}{: ^{width}}{}  ".format(author, "", current_icon, width=space_width)))
    poster.append(EMPTY_ROW)
    poster.append(FULL_ROW)
