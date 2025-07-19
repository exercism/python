def recite(start_verse, end_verse):
    gifts = (
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    )
    ordinals = (
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    )
    
    def build_verse(n):
        day = n - 1
        verse = f"On the {ordinals[day]} day of Christmas my true love gave to me: "
        verse_gifts = [f"and {gifts[0]}" if i == 0 and day > 0 else gifts[i] for i in range(day, -1, -1)]
        verse += ", ".join(verse_gifts) + "."
        return verse
    
    return [build_verse(n) for n in range(start_verse, end_verse + 1)]