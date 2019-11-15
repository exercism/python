gestures = ['wink', 'double blink', 'close your eyes', 'jump']


def commands(number):
    actions = [gestures[i] for i in range(len(gestures))
               if (number >> i) % 2 == 1]
    return actions if number < 16 else list(reversed(actions))
