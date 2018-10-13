def sum_of_multiples(limit, multiples):
    if 0 in multiples:
        return 0
    else:
        return sum(value for value in range(limit)
               if any(value % multiple == 0
                      for multiple in multiples))
