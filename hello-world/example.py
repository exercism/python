def hello(name=''):
    if name:
        return u'Hello, {}!'.format(name)
    else:
        return 'Hello, World!'
