from calendar import Calendar


def meetup(year, month, week, day_of_week):
    candidates = [date
                  for date in Calendar().itermonthdates(year, month)
                  if date.month == month
                  if date.strftime('%A') == day_of_week]
    return _choice(week)(candidates)


def _choice(week):
    if week == 'teenth':
        return lambda dates: next(date for date in dates if
                                  13 <= date.day <= 19)

    ordinals = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth')
    day = -1 if (week == 'last') else (ordinals.index(week))

    def _func(dates):
        if day < len(dates):
            return dates[day]
        raise MeetupDayException('That day does not exist.')
    return _func


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
