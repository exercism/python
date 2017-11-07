gestures = ['wink', 'double blink', 'close your eyes', 'jump']


def handshake(code):
    actions = [gestures[i] for i in range(len(gestures))
               if (code >> i) % 2 == 1]
    return actions if code < 16 else list(reversed(actions))


def secret_code(actions):
    actions = [a for a in actions if a in gestures]
    result = sum(1 << i for i, action in enumerate(gestures)
                 if action in actions)
    if len(actions) > 1 and (gestures.index(actions[0]) >
                             gestures.index(actions[1])):
        result += 16
    return result
