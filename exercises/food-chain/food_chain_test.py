import unittest

from food_chain import chain

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

song = """I know an old lady who swallowed a fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a spider.
It wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a bird.
How absurd to swallow a bird!
She swallowed the bird to catch the spider that wriggled
and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a cat.
Imagine that, to swallow a cat!
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled
and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a dog.
What a hog, to swallow a dog!
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled
and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a goat.
Just opened her throat and swallowed a goat!
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled
and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a cow.
I don't know how she swallowed a cow!
She swallowed the cow to catch the goat.
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled
and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a horse.
She's dead, of course!"""


def verses(letter):
    return letter.replace('die.', 'die.slice').split('slice')


original = [verse.replace("\n", "").replace(" ", "").lower()
            for verse in verses(song)]

generated = [verse.replace("\n", "").replace(" ", "").lower()
             for verse in verses(chain())]


class FoodChainTest(unittest.TestCase):

    def test_fly(self):
        self.assertEqual(original[0], generated[0])

    def test_spider(self):
        self.assertEqual(original[1], generated[1])

    def test_bird(self):
        self.assertEqual(original[2], generated[2])

    def test_cat(self):
        self.assertEqual(original[3], generated[3])

    def test_dog(self):
        self.assertEqual(original[4], generated[4])

    def test_goat(self):
        self.assertEqual(original[5], generated[5])

    def test_cow(self):
        self.assertEqual(original[6], generated[6])

    def test_horse(self):
        self.assertEqual(original[7], generated[7])

    def test_multiple_verses(self):
        self.assertEqual(original[0:3], generated[0:3])

    def test_full_song(self):
        self.assertEqual(original, generated)


if __name__ == '__main__':
    unittest.main()
