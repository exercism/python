GESTURES = ['jump', 'close your eyes', 'double blink', 'wink']


def commands(binary_str):
    reverse, *bits = [digit == '1' for digit in binary_str]
    actions = [gesture for gesture, bit in zip(GESTURES, bits) if bit]
    return actions if reverse else actions[::-1]
