def transform(legacy_data):
    return_data = {}
    for score in legacy_data:
        letters = legacy_data[score]
        for letter in letters:
            uni_letter = letter.lower()
            return_data[uni_letter] = score

    return return_data
