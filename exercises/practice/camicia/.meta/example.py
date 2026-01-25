def simulate_game(player_a, player_b):
    hand_a = list(map(get_value, player_a))
    hand_b = list(map(get_value, player_b))
    turn = "A"
    pile = []
    seen = set()
    total_tricks = 0
    cards_played = 0
    current_debt = 0

    while True:
        if not pile:
            state = (tuple(hand_a), tuple(hand_b), turn)
            if state in seen:
                return {
                    "status": "loop", 
                    "tricks": total_tricks, 
                    "cards": cards_played
                }
            seen.add(state)

        active_hand = hand_a if turn == "A" else hand_b
        other_hand = hand_b if turn == "A" else hand_a

        if not active_hand:
            extra_trick = 0 if not pile else 1
            return {
                "status": "finished",
                "tricks": total_tricks + extra_trick,
                "cards": cards_played,
            }

        card_val = active_hand.pop(0)
        pile.append(card_val)
        cards_played += 1

        if card_val > 0:
            current_debt = card_val
            turn = "B" if turn == "A" else "A"
        else:
            if current_debt > 0:
                current_debt -= 1
                if not current_debt:
                    other_hand.extend(pile)
                    pile = []
                    total_tricks += 1
                    current_debt = 0

                    if not hand_a or not hand_b:
                        return {
                            "status": "finished", 
                            "tricks": total_tricks, 
                            "cards": cards_played
                        }

                    turn = "B" if turn == "A" else "A"
            else:
                turn = "B" if turn == "A" else "A"


def get_value(card):
    if card == "J":
        return 1
    if card == "Q":
        return 2
    if card == "K":
        return 3
    if card == "A":
        return 4
    return 0
