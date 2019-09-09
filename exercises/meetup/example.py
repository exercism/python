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

    day = -1 if (week == 'last') else (int(week[0]) - 1)

    def _func(dates):
        if day < len(dates):
            return dates[day]
        raise MeetupDayException('day does not exist')
    return _func


class MeetupDayException(Exception):
    pass
