def verify(isbn):
    clear_isbn = remove_non_alphanumeric(isbn)
    if len(clear_isbn) != 10:
        return False

    isbn_main_part = get_isbn_main_part(clear_isbn)
    if not isbn_main_part.isdigit():
        return False

    check_digit = get_isbn_check_digit(clear_isbn)
    if not check_digit.isdigit() and check_digit.upper() != 'X':
        return False

    if calculate_isbn_check_digit(isbn_main_part) != check_digit:
        return False

    return True


def remove_non_alphanumeric(value):
    return ''.join([x for x in str(value) if x.isalnum()])


def get_isbn_main_part(isbn_value):
    return isbn_value[:-1]


def get_isbn_check_digit(isbn_value):
    return isbn_value[-1:]


def calculate_isbn_check_digit(isbn):
    check_digit = 11 - (int(isbn[0:1]) * 10 +
                        int(isbn[1:2]) * 9 +
                        int(isbn[2:3]) * 8 +
                        int(isbn[3:4]) * 7 +
                        int(isbn[4:5]) * 6 +
                        int(isbn[5:6]) * 5 +
                        int(isbn[6:7]) * 4 +
                        int(isbn[7:8]) * 3 +
                        int(isbn[8:9]) * 2) % 11

    if check_digit == 10:
        return 'X'

    return str(check_digit)
