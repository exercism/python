def slices(series, length):
    if not series:
        raise ValueError('series cannot be empty')
    elif length == 0:
        raise ValueError('slice length cannot be zero')
    elif length < 0:
        raise ValueError('slice length cannot be negative')
    elif len(series) < length:
        raise ValueError('slice length cannot be greater than series length')

    return [series[idx:idx + length] for idx in range(len(series) - length + 1)]
