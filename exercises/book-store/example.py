BOOK_PRICE = 8


def _group_price(size):
    discounts = [0, .05, .1, .2, .25]
    if not (0 < size <= 5):
        raise ValueError('size must be in 1..' + len(discounts))
    return 8 * size * (1 - discounts[size - 1])


def calculate_total(books, price_so_far=0.):
    if not books:
        return price_so_far

    groups = list(set(books))
    min_price = float('inf')

    for i in range(len(groups)):

        remaining_books = books[:]

        for v in groups[:i + 1]:
            remaining_books.remove(v)

        price = calculate_total(remaining_books,
                                price_so_far + _group_price(i + 1))
        min_price = min(min_price, price)

    return min_price
