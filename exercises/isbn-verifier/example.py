def verify(isbn):
    clear_isbn = _remove_non_alphanumeric(isbn)
    if len(clear_isbn) != 10:
        return False

    isbn_main_part = _get_isbn_main_part(clear_isbn)
    if not isbn_main_part.isdigit():
        return False

    return _calculate_isbn_check_digit(isbn_main_part) == _get_isbn_check_digit(clear_isbn).upper()


def isbn_generator(isbn):
    clear_isbn = _remove_non_alphanumeric(isbn)
    if len(clear_isbn) < 9 or len(clear_isbn) > 10:
        raise ValueError()

    isbn_main_part = clear_isbn[:9]
    return _format_isbn(isbn_main_part + _calculate_isbn_check_digit(isbn_main_part))


def _remove_non_alphanumeric(value):
    return ''.join([x for x in str(value) if x.isalnum()])


def _get_isbn_main_part(isbn_value):
    return isbn_value[:-1]


def _get_isbn_check_digit(isbn_value):
    return isbn_value[-1:]


def _calculate_isbn_check_digit(isbn):
    isbn_sum = 11 - sum([int(x) * (10 - i) for i, x in enumerate(isbn)]) % 11
    return 'X' if isbn_sum == 10 else str(isbn_sum)


def _format_isbn(isbn):
    return '-'.join([isbn[:1], isbn[1:4], isbn[4:9], isbn[9:]])
