def proverb(rhyme_items):
    if not rhyme_items:
        return ""
    phrases = ['For want of a {0} the {1} was lost.'.format(el1, el2)
               for el1, el2 in zip(rhyme_items, rhyme_items[1:])]
    phrases.append('And all for the want of a {0}.'.format(rhyme_items[0]))
    return '\n'.join(phrases)
