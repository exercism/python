def number(g):
    if g == [" _ ","| |","|_|","   "]:
        return '0'
    elif g == ["   ","  |","  |","   "]:
        return '1'
    else:
        return '?'

def grid(n):
    if n == '0':
        return [" _ ","| |","|_|","   "]
    elif n == '1':
        return ["   ","  |","  |","   "]
    raise ValueError('Unknown digit')