def slices(series, length):
    if not 1 <= length <= len(series):
        raise ValueError("Invalid slice length for this series: " + str(
            length))
    return [series[i:i + length] for i in range(len(series) - length + 1)]
