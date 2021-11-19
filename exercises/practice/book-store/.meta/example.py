from collections import Counter

PER_BOOK = 800.00
PER_GROUP = {
    1: 1 * PER_BOOK * 1.00,
    2: 2 * PER_BOOK * 0.95,
    3: 3 * PER_BOOK * 0.90,
    4: 4 * PER_BOOK * 0.80,
    5: 5 * PER_BOOK * 0.75,
}


def _total(basket):
    volumes = Counter(basket)
    price = len(basket) * PER_BOOK
    for size in range(len(volumes), 1, -1):
        group = volumes - Counter(k for k, _ in volumes.most_common(size))
        group_books = sorted(group.elements())
        price = min(price, PER_GROUP[size] + _total(group_books))
    return price


def total(basket):
    if not basket:
        return 0
    return _total(sorted(basket))
