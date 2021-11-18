def get_song():

    animals = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']

    phrases = [' wriggled and jiggled and tickled inside her.',
               'How absurd to swallow a bird!',
               'Imagine that, to swallow a cat!',
               'What a hog, to swallow a dog!',
               'Just opened her throat and swallowed a goat!',
               "I don't know how she swallowed a cow!",
               "She's dead, of course!"]

    old_lady = 'I know an old lady who swallowed a '
    swallowed = 'She swallowed the <animal> to catch the '
    die = "I don't know why she swallowed the fly. Perhaps she'll die."

    song = ''
    verse = ''
    chain = ''

    for number, animal in enumerate(animals):
        verse = old_lady + animal + '.\n'

        if number == 7:
            verse += phrases[6]
        else:
            if number == 0:
                chain = swallowed + animal + '.\n'
            elif number == 1:
                verse += 'It' + phrases[0] + '\n'
                chain = chain.replace('<animal>', animal)
                verse += chain
                chain = swallowed + animal + ' that' + phrases[0] + '\n' + chain
            else:
                verse += phrases[number-1] + '\n'
                chain = chain.replace('<animal>', animal)
                verse += chain
                chain = swallowed + animal + '.\n' + chain

            verse += die + '\n'

        verse += '\n'
        song += verse

    return song


def verses(letter):
    return letter.replace('die.', 'die.slice').split('slice')


def recite(start_verse, end_verse):
    generated = [verse.strip().split('\n') for verse in verses(get_song())]
    if start_verse == end_verse:
        return generated[start_verse - 1]
    else:
        result = []
        for idx in range(start_verse - 1, end_verse):
            result += generated[idx] + ['']

        # Pop out the last empty string
        result.pop()
        return result
