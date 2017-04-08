import unittest
from transpose import transpose


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class TransposeTests(unittest.TestCase):
    def test_empty_string(self):
        input_line = ""
        expected = ""
        self.assertEqual(
            transpose(input_line),
            expected
        )

    def test_two_characters_in_a_row(self):
        self.assertEqual(
            transpose("A1"),
            "\n".join(["A", "1"])
        )

    def test_two_characters_in_a_column(self):
        self.assertEqual(
            transpose("\n".join(["A", "1"])),
            "A1"
        )

    def test_simple(self):
        input_line = [
            "ABC",
            "123"
        ]
        expected = [
            "A1",
            "B2",
            "C3"
        ]

        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_single_line(self):
        input_line = ["Single line."]
        expected = [
            "S",
            "i",
            "n",
            "g",
            "l",
            "e",
            " ",
            "l",
            "i",
            "n",
            "e",
            "."
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_first_line_longer_than_second_line(self):
        input_line = [
            "The fourth line.",
            "The fifth line."
        ]
        expected = [
            "TT",
            "hh",
            "ee",
            "  ",
            "ff",
            "oi",
            "uf",
            "rt",
            "th",
            "h ",
            " l",
            "li",
            "in",
            "ne",
            "e.",
            "."
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_second_line_longer_than_first_line(self):
        input_line = [
            "The first line.",
            "The second line."
        ]
        expected = [
            "TT",
            "hh",
            "ee",
            "  ",
            "fs",
            "ie",
            "rc",
            "so",
            "tn",
            " d",
            "l ",
            "il",
            "ni",
            "en",
            ".e",
            " ."
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_square(self):
        input_line = [
            "HEART",
            "EMBER",
            "ABUSE",
            "RESIN",
            "TREND"
        ]
        expected = [
            "HEART",
            "EMBER",
            "ABUSE",
            "RESIN",
            "TREND"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_rectangle(self):
        input_line = [
            "FRACTURE",
            "OUTLINED",
            "BLOOMING",
            "SEPTETTE"
        ]
        expected = [
            "FOBS",
            "RULE",
            "ATOP",
            "CLOT",
            "TIME",
            "UNIT",
            "RENT",
            "EDGE"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_triangle(self):
        input_line = [
            "T",
            "EE",
            "AAA",
            "SSSS",
            "EEEEE",
            "RRRRRR"
        ]
        expected = [
            "TEASER",
            " EASER",
            "  ASER",
            "   SER",
            "    ER",
            "     R"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_many_lines(self):
        input_line = [
            "Chor. Two households, both alike in dignity,",
            "In fair Verona, where we lay our scene,",
            "From ancient grudge break to new mutiny,",
            "Where civil blood makes civil hands unclean.",
            "From forth the fatal loins of these two foes",
            "A pair of star-cross'd lovers take their life;",
            "Whose misadventur'd piteous overthrows",
            "Doth with their death bury their parents' strife.",
            "The fearful passage of their death-mark'd love,",
            "And the continuance of their parents' rage,",
            "Which, but their children's end, naught could remove,",
            "Is now the two hours' traffic of our stage;",
            "The which if you with patient ears attend,",
            "What here shall miss, our toil shall strive to mend."
        ]
        expected = [
            "CIFWFAWDTAWITW",
            "hnrhr hohnhshh",
            "o oeopotedi ea",
            "rfmrmash  cn t",
            ".a e ie fthow ",
            " ia fr weh,whh",
            "Trnco miae  ie",
            "w ciroitr btcr",
            "oVivtfshfcuhhe",
            " eeih a uote  ",
            "hrnl sdtln  is",
            "oot ttvh tttfh",
            "un bhaeepihw a",
            "saglernianeoyl",
            "e,ro -trsui ol",
            "h uofcu sarhu ",
            "owddarrdan o m",
            "lhg to'egccuwi",
            "deemasdaeehris",
            "sr als t  ists",
            ",ebk 'phool'h,",
            "  reldi ffd   ",
            "bweso tb  rtpo",
            "oea ileutterau",
            "t kcnoorhhnatr",
            "hl isvuyee'fi ",
            " atv es iisfet",
            "ayoior trr ino",
            "l  lfsoh  ecti",
            "ion   vedpn  l",
            "kuehtteieadoe ",
            "erwaharrar,fas",
            "   nekt te  rh",
            "ismdsehphnnosa",
            "ncuse ra-tau l",
            " et  tormsural",
            "dniuthwea'g t ",
            "iennwesnr hsts",
            "g,ycoi tkrttet",
            "n ,l r s'a anr",
            "i  ef  'dgcgdi",
            "t  aol   eoe,v",
            "y  nei sl,u; e",
            ",  .sf to l   ",
            "     e rv d  t",
            "     ; ie    o",
            "       f, r   ",
            "       e  e  m",
            "       .  m  e",
            "          o  n",
            "          v  d",
            "          e  .",
            "          ,"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )


if __name__ == '__main__':
    unittest.main()
