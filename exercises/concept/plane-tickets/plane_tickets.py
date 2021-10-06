def value_of_card(card):
    """

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, numerical value otherwise).
    """

    pass


def value_of_ace(hand_value):
    """

    :param hand_value: int - current hand value.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    pass


def is_blackjack(card_one, card_two):
    """

    :param card_one: str - first card in hand.
    :param card_two: str - second card in hand.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    pass


def can_split_pairs(card_one, card_two):
    """

    :param card_one: str - first card in hand.
    :param card_two: str - second card in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    pass


def can_double_down(card_one, card_two):
    """

    :param card_one: str - first card in hand.
    :param card_two: str - second card in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    pass
