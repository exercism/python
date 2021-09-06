def number_of_card(card):
    if card == 'A':
        return "ace"
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    else:
        return card


def number_of_ace(hand):
    if hand + 11 <= 21:
        return 11
    else:
        return 1


def blackjack(hand):
    if 'A' not in hand:
        return False
    elif 'J' in hand or 'Q' in hand or 'K' in hand or 10 in hand:
        return True
    else:
        False
