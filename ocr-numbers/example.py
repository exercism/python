def number(g):
    if not g or len(g) < 4 or any(len(r)!=len(g[0]) for r in g):
        raise ValueError('Ill-formed grid')
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