from math import ceil, floor

def meeting_time(employee_info):
    employee_times = []
    for _, (time_zone, (start_time, end_time)) in employee_info.items():
        if (end_time if end_time >= start_time else end_time + 24) - start_time != 9:
            raise ValueError("some employees are working for more or less than 9 hours")
        start_time_utc = (start_time - time_zone) % 24
        end_time_utc = (end_time - time_zone) % 24

        employee_times.append((start_time_utc, end_time_utc))


    employee_times_set = []
    for start_time, end_time in employee_times:
        if end_time > start_time:
            employee_times_set.append(set(range(ceil(start_time), floor(end_time))))
        else:
            employee_times_set.append({*range(ceil(start_time), 24), *range(0, floor(end_time))})


    possible_times = list(set.intersection(*employee_times_set))

    if not possible_times:
        raise ValueError("there's no possible meeting time for the provided employees")
    return possible_times