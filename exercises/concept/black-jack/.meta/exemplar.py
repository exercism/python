def value_of_card(card):
    """

    :param card: str - given card.
    :return: int - value of a given card (face card = 10, pip value otherwise).
    """

    if card in ['J', 'Q', 'K']:
        value = 10
    else:
        value = int(card)
    return value


def value_of_ace(hand_value):
    """

    :param hand_value: int - current hand value.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    if hand_value + 11 > 21:
        value = 1
    else:
        value = 11
    return value


def is_blackjack(hand):
    """

    :param hand: list - a pair of cards in hand.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    blackjack = False
    if 'A' in hand:
        if any(ten_card in hand for ten_card in ['10', 'J', 'Q', 'K']):
            blackjack = True
    return blackjack


def can_split_pairs(hand):
    """

    :param hand: list - a pair of cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    card_one, card_two = hand
    if 'A' in hand:
        split_pairs = card_one == card_two
    else:
        split_pairs = value_of_card(card_one) == value_of_card(card_two)
    return split_pairs


def can_double_down(hand):
    """

    :param hand: list - a pair of cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    hand_value = sum(1 if card == 'A' else value_of_card(card) for card in hand)
    return 9 <= hand_value <= 11
