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
    label = str(value)

    if len(label) < 4 :
        unit = 'ohms'
    elif len(label) < 7:
        label = str(value//1000)
        unit = 'kiloohms'
    elif len(label) <= 8 :
        label = str(value//1000000)
        unit = 'megaohms'
    elif len(label) >= 9:
        label = str(value//1000000000)
        unit = 'gigaohms'

    return f'{value if value < 1000 else label} {unit}'
