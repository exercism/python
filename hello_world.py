def hello(name=''):
    if name != '':
        print('Hello, %s!' % name)
    else:
        print('Hello, World!')

print('Hi! you are in Exercism Python\n')

name = input('What is your name?:')
#assert type( name ) is str,'input must be a name!'

try:
    name = str(name)
except ValueError as msg:
    pass
    print('input must be a name')
    #raise ValueError('input must be a name!)
hello(name)

