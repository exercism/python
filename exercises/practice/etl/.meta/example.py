def transform(legacy_data):
    return {
        letter.lower(): points
        for points, letters in legacy_data.items()
        for letter in letters
    }
