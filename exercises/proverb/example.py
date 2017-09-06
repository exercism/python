def proverb(items, qualifier=''):
    phrases = ['For want of a {0} the {1} was lost.'.format(el1, el2)
               for el1, el2 in zip(items, items[1:])]
    qualifier += ' ' if qualifier else ''
    phrases.append('And all for the want of a {0}{1}.'.format(qualifier,
                   items[0]))
    return '\n'.join(phrases)
