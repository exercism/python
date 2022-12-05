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


def label(colors):
    value = 10 * COLORS.index(colors[0]) + COLORS.index(colors[1])
    value *= 10 ** COLORS.index(colors[2])
    return str(value) + ' ohms' if value < 1000 else str(value // 1000) + ' kiloohms'
