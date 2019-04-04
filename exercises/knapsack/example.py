def solve_knapsack(max_weight, items):
    t = [[0 for _ in range(len(items) + 1)] for _ in range(max_weight + 1)]
    for weight in range(1, max_weight + 1):
        for i, item in enumerate(items, 1):
            if item["weight"] <= weight:
                value = item["value"] + t[weight - item["weight"]][i - 1]
                value_without_item = t[weight][i - 1]
                t[weight][i] = max(value, value_without_item)
            else:
                t[weight][i] = t[weight][i - 1]
    return t[max_weight][len(items)]
