from datetime import datetime, timedelta, timezone, time


def meeting_time(date_str, employees):
    meeting_times = {}

    meeting_date = datetime.strptime(date_str, "%m/%d/%Y")

    for hour in range(24):
        meeting_start_time = meeting_date.replace(
            hour=hour, minute=0, second=0, tzinfo=timezone.utc
        )
        meeting_end_time = meeting_start_time + timedelta(hours=1)

        employees_possible = {}
        for emp_id, (utc_offset, emp_start_str, emp_end_str) in employees.items():
            emp_timezone = timezone(timedelta(hours=utc_offset))

            start_datetime = datetime.combine(
                meeting_date,
                datetime.strptime(emp_start_str, "%I:%M %p").time(),
                tzinfo=emp_timezone,
            ).astimezone(timezone.utc)
            end_datetime = datetime.combine(
                meeting_date,
                datetime.strptime(emp_end_str, "%I:%M %p").time(),
                tzinfo=emp_timezone,
            ).astimezone(timezone.utc)

            if end_datetime < start_datetime:
                end_datetime = end_datetime + timedelta(days=1)
            for i in range(-1, 2):
                modified_start = start_datetime + timedelta(days=i)
                modified_end = end_datetime + timedelta(days=i)
                if (
                    modified_start <= meeting_start_time
                    and modified_end >= meeting_end_time
                ):
                    employees_possible[emp_id] = meeting_start_time.astimezone(
                        emp_timezone
                    ).strftime("%m/%d/%Y %I:%M %p")

        if len(employees_possible) == 4:
            meeting_times[time(hour=hour).strftime("%I:%M %p")] = employees_possible

    return meeting_times
