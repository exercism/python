def verify(isbn):
    clear_isbn = _remove_non_alphanumeric(isbn)
    if len(clear_isbn) != 10:
        return False

    isbn_main_part = clear_isbn[:-1]
    if not isbn_main_part.isdigit():
        return False

    calculated_digit = _calculate_isbn10_check_digit(isbn_main_part)
    check_digit = clear_isbn[-1:].upper()

    return calculated_digit == check_digit


def isbn_generator(isbn):
    clear_isbn = _remove_non_alphanumeric(isbn)
    if len(clear_isbn) < 9 or len(clear_isbn) > 10:
        raise ValueError()

    isbn_main_part = clear_isbn[:9]
    isbn = isbn_main_part + _calculate_isbn10_check_digit(isbn_main_part)
    return '-'.join([isbn[:1], isbn[1:4], isbn[4:9], isbn[9:]])


def isbn13_generator_from_isbn10(isbn10):
    clear_isbn = _remove_non_alphanumeric(isbn10)
    if len(clear_isbn) != 10:
        raise ValueError()

    isbn_main_part = '978' + clear_isbn[:9]
    isbn = isbn_main_part + _calculate_isbn13_check_digit(isbn_main_part)
    return '-'.join([isbn[:3], isbn[3:4], isbn[4:6], isbn[6:12], isbn[12:13]])


def _remove_non_alphanumeric(value):
    return ''.join([x for x in str(value) if x.isalnum()])


def _calculate_isbn10_check_digit(isbn):
    isbn_sum = sum([int(x) * (i + 1) for i, x in enumerate(isbn)]) % 11
    return 'X' if isbn_sum == 10 else str(isbn_sum)


def _calculate_isbn13_check_digit(isbn):
    isbn_sum = sum([int(x) * (3 if i % 2 == 1 else 1)
                    for i, x in enumerate(isbn)]) % 10
    return str(isbn_sum) if isbn_sum == 0 else str(10 - isbn_sum)
