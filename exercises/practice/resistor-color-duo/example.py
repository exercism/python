COLORS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]


def value(colors):
    return 10 * COLORS.index(colors[0]) + COLORS.index(colors[1])
