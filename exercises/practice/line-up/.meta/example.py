def line_up(name, number):
    suffix = get_suffix(number)
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"


def get_suffix(number):
    if 11 <= number % 100 <= 13:
        return "th"

    mod_10 = number % 10

    if mod_10 == 1:
        return "st"
    if mod_10 == 2:
        return "nd"
    if mod_10 == 3:
        return "rd"

    return "th"
