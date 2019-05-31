old_sum = sum


def sum(factors, limit):
    return old_sum(value for value in range(limit)
                   if any(value % multiple == 0
                          for multiple in factors
                          if multiple > 0))
