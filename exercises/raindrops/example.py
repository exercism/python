DROPS = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))


def convert(number):
    """
    Converts a number to a string according to the raindrop sounds.
    """

    return "".join(sound for factor, sound
                   in DROPS if number % factor == 0) or str(number)
