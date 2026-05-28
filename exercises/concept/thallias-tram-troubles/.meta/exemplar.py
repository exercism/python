def time_table_for_a_weekday(table_of_time, week_day):
    """Get the time table for a weekday.

    :parm table_of_time: sequence[sequence] - sequence of time tables.
    :parm week_day: integer - the number of the weekday.
    :return: sequence - sequence of timetables within a weekday .
    """
    return table_of_time[week_day]


def time_table_for_a_specific_range(table_of_time, week_day, start, stop):
    """Get the a slice of time table for a weekday.

    :parm table_of_time: sequence[sequence] - sequence of time tables.
    :parm week_day: integer - the number of the weekday.
    :parm start: integer - the start of the slice.
    :parm stop: integer - the end of the slice.
    :return: sequence - slice of timetables within a weekday .
    """
    return table_of_time[week_day][start:stop]

