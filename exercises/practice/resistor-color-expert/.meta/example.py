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

COLORS_TOLERANCE = {
    'brown': 1,
    'red': 2,
    'green': 0.5,
    'blue': 0.25,
    'violet': 0.1,
    'grey': 0.05,
    'gold': 5,
    'silver': 10
}


def resistor_label(colors):
    if len(colors) == 1:
        return f'0 ohms'
    elif len(colors) == 4:
        value = 10 * COLORS.index(colors[0]) + COLORS.index(colors[1])
        value *= 10 ** COLORS.index(colors[2])
        value, unit = color_code(value)
        value = int(value) if value.is_integer() else value
        return f'{value} {unit} ±{COLORS_TOLERANCE[colors[3]]}%'
    else:
        value = 100 * COLORS.index(colors[0]) + 10 * COLORS.index(colors[1]) + COLORS.index(colors[2])
        value *= 10 ** COLORS.index(colors[3])
        value, unit = color_code(value)
        value = int(value) if value.is_integer() else value
        return f'{value} {unit} ±{COLORS_TOLERANCE[colors[4]]}%'


def color_code(color):
    if color < 1000:
        return color / 1, 'ohms'
    elif color < 1000000:
        return color / 1000, 'kiloohms'
    else:
        return color / 1000000, 'megaohms'