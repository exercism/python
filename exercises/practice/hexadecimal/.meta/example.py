from functools import reduce


def hexa(hex_str):
    hex_str = hex_str.lower()
    if set(hex_str) - set('0123456789abcdef'):
        raise ValueError('Invalid hexadecimal string')
    digits = [ord(c) - ord('a') + 10 if c in 'abcdef' else ord(c) - ord('0')
              for c in hex_str]
    return reduce(lambda x, y: x * 16 + y, digits, 0)
