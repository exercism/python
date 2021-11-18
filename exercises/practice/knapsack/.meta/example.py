def maximum_value(maximum_weight, items):
    totals = [[0 for _ in range(len(items) + 1)]
              for _ in range(maximum_weight + 1)]

    for weight in range(1, maximum_weight + 1):
        for index, item in enumerate(items, 1):
            if item['weight'] <= weight:
                value = item['value'] + \
                        totals[weight - item['weight']][index - 1]

                value_without_item = totals[weight][index - 1]
                totals[weight][index] = max(value, value_without_item)
            else:
                totals[weight][index] = totals[weight][index - 1]
    return totals[maximum_weight][len(items)]
