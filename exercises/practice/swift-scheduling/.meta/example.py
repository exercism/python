from datetime import datetime, timedelta


def delivery_date(start, description):
    start_date = datetime.fromisoformat(start)


    if  description == 'NOW':
        due_date = start_date + timedelta(hours=2)

    if  description == 'ASAP':
        if str(start_date.time()) < '13:00:00':
            due_date = start_date.replace(hour=17, minute=0)
        else:
            due_date = (
                    start_date.replace(hour=13, minute=0) +
                    timedelta(days=1)
            )

    if description =='EOW':
        if start_date.isoweekday() < 4:
          due_date = (
              start_date.replace(hour=17, minute=0) +
              timedelta(days=5 - start_date.isoweekday())
          )
        else:
          due_date = (
              start_date.replace(hour=20, minute=0) +
              timedelta(days=7 - start_date.isoweekday())
          )

    if description.endswith('M'):
        month = int(description[:-1])
        target = datetime(start_date.year, month, 1, 8, 0, 0)

        if start_date.month >= target.month:
            target = target.replace(year=target.year + 1)
        if target.isoweekday() not in (6,7) and target.day in range(1, 8):
            due_date = target
        else:
            if target.isoweekday() == 6: due_date = target + timedelta(days = 2)
            if target.isoweekday() == 7: due_date = target + timedelta(days = 1)

    if description.startswith('Q'):
        target = int(description[1:])
        current  = ((start_date.month + 2) // 3)
        month =  {"Q1":4,"Q2": 7,"Q3": 10,"Q4": 1}[description]
        rollover = 1 if (current > target or target == 4) else 0

        due_date = start_date.replace(
            start_date.year + rollover, month, 1, 8, 0, 0
        ) - timedelta(days=1)

        if due_date.isoweekday() == 6: due_date -= timedelta(days=1)
        if due_date.isoweekday() == 7: due_date  -= timedelta(days=2)

    return due_date.isoformat()
