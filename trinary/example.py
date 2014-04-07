def trinary(s):
    if set(s) - set('012'):
        return 0
    return reduce(lambda x,y:x*3 + int(y), s, 0)

if __name__ == '__main__':
    print trinary('102101')
    print trinary('22222')
    print trinary('10000')
