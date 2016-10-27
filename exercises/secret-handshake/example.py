gestures = ['wink', 'double blink', 'close your eyes', 'jump']


def handshake(s):
    s = list(sanitize(s))
    s.reverse()
    seq = []
    lim = len(s) if len(s) <= len(gestures) else len(gestures)
    for i1 in range(lim):
        if s[i1] == '1':
            seq.append(gestures[i1])
    if len(s) == 5:
        seq.reverse()
    return seq


def code(seq):
    if not seq or set(seq) - set(gestures):
        return '0'
    s = find_subseq(seq)
    if not s:
        s = ['1'] + find_subseq(reversed(seq))
    return "".join(s)


def sanitize(s):
    if not(isinstance(s, int) or isinstance(s, str)):
        raise TypeError('Unknown type')
    if isinstance(s, int):
        if s < 0:
            return ""
        s = bin(s)[2:]
    elif set(s) - set(['0', '1']):
        return ""
    if len(s) > 5:
        raise ValueError('Binary string too long')
    return "0" * (len(gestures) - len(s)) + s


def find_subseq(seq):
    idx = 0
    s = []
    for g in seq:
        if g not in gestures[idx:]:
            return []
        newidx = gestures.index(g, idx) + 1
        s.extend(['0'] * (newidx - idx - 1) + ['1'])
        idx = newidx
    s.reverse()
    return s
