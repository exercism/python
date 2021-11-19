PARTS = [('lay in', 'the house that Jack built.'),
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


def verse(verse_num):
    verse = [f'This is {PARTS[verse_num][1]}']
    verse.extend(['that {0} {1}'.format(*PARTS[idx])
              for idx in range(verse_num - 1, -1, -1)])
    return ' '.join(verse)


def recite(start_verse, end_verse):
    return [verse(verse_num) for verse_num in range(start_verse-1, end_verse)]
