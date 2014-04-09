def hexa(s):
    s = s.lower()
    if set(s) - set('0123456789abcdef'):
        raise ValueError('Invalid hexadecimal string')
    l = [ord(c) - ord('a') + 10 if c in 'abcdef' else ord(c) - ord('0')
            for c in s]
    return reduce(lambda x,y:x*16 + y, l, 0)

if __name__ == '__main__':
    print hexa('19ACE')
    print hexa('100')
    print hexa('dead')