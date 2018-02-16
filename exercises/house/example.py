parts = [('lay in', 'the house that Jack built'),
         ('ate', 'the malt'),
         ('killed', 'the rat'),
         ('worried', 'the cat'),
         ('tossed', 'the dog'),
         ('milked', 'the cow with the crumpled horn'),
         ('kissed', 'the maiden all forlorn'),
         ('married', 'the man all tattered and torn'),
         ('woke', 'the priest all shaven and shorn'),
         ('kept', 'the rooster that crowed in the morn'),
         ('belonged to', 'the farmer sowing his corn'),
         ('', 'the horse and the hound and the horn')]


def _specified_verse(verse_num):
    v = ['This is {}'.format(parts[verse_num][1])]
    v.extend(['that {0} {1}'.format(parts[i][0], parts[i][1])
              for i in range(verse_num - 1, -1, -1)])
    v[-1] += '.'
    return '\n'.join(v)


def verse(start_verse, end_verse):
    if start_verse == end_verse:
        return _specified_verse(start_verse - 1)
    else:
        return "\n\n".join(
            _specified_verse(n)
            for n in range(start_verse-1, end_verse))
