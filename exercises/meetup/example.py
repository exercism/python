from calendar import Calendar


def meetup_day(year, month, day_of_the_week, which):
    candidates = [date
                  for date in Calendar().itermonthdates(year, month)
                  if date.month == month
                  if date.strftime('%A') == day_of_the_week]
    return _choice(which)(candidates)


def _choice(which):
    if which == 'teenth':
        return lambda dates: next(d for d in dates if 13 <= d.day <= 19)

    ix = -1 if (which == 'last') else (int(which[0]) - 1)

    def _func(dates):
        if ix < len(dates):
            return dates[ix]
        raise MeetupDayException('day does not exist')
    return _func


class MeetupDayException(Exception):
    pass
