import os
import unittest

from grep import grep


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

ILIADFILENAME = 'iliad.txt'
ILIADCONTENTS = '''Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men.
'''

MIDSUMMERNIGHTFILENAME = 'midsummer-night.txt'
MIDSUMMERNIGHTCONTENTS = '''I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius.
'''

PARADISELOSTFILENAME = 'paradise-lost.txt'
PARADISELOSTCONTENTS = '''Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed
'''


def remove_file(file_name):
    try:
        os.remove(file_name)
    except OSError:
        pass


def create_file(name, contents):
    with open(name, 'w') as f:
        f.write(contents)


class GrepTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        create_file(ILIADFILENAME, ILIADCONTENTS)
        create_file(MIDSUMMERNIGHTFILENAME, MIDSUMMERNIGHTCONTENTS)
        create_file(PARADISELOSTFILENAME, PARADISELOSTCONTENTS)

    @classmethod
    def tearDownClass(self):
        remove_file(ILIADFILENAME)
        remove_file(MIDSUMMERNIGHTFILENAME)
        remove_file(PARADISELOSTFILENAME)

    def test_one_file_one_match_no_flags(self):
        self.assertMultiLineEqual(
            grep("Agamemnon", [ILIADFILENAME]),
            "Of Atreus, Agamemnon, King of men.\n")

    def test_one_file_one_match_print_line_numbers_flag(self):
        self.assertMultiLineEqual(
            grep("Forbidden", [PARADISELOSTFILENAME], "-n"),
            "2:Of that Forbidden Tree, whose mortal tast\n")

    def test_one_file_one_match_case_insensitive_flag(self):
        self.assertMultiLineEqual(
            grep("FORBIDDEN", [PARADISELOSTFILENAME], "-i"),
            "Of that Forbidden Tree, whose mortal tast\n")

    def test_one_file_one_match_print_file_names_flag(self):
        self.assertMultiLineEqual(
            grep("Forbidden", [PARADISELOSTFILENAME], "-l"),
            PARADISELOSTFILENAME + '\n')

    def test_one_file_one_match_match_entire_lines_flag(self):
        self.assertMultiLineEqual(
            grep("With loss of Eden, till one greater Man",
                 [PARADISELOSTFILENAME], "-x"),
            "With loss of Eden, till one greater Man\n")

    def test_one_file_one_match_multiple_flags(self):
        self.assertMultiLineEqual(
            grep("OF ATREUS, Agamemnon, KIng of MEN.", [ILIADFILENAME],
                 "-n -i -x"), "9:Of Atreus, Agamemnon, King of men.\n")

    def test_one_file_several_matches_no_flags(self):
        self.assertMultiLineEqual(
            grep("may", [MIDSUMMERNIGHTFILENAME]),
            ("Nor how it may concern my modesty,\n"
             "But I beseech your grace that I may know\n"
             "The worst that may befall me in this case,\n"))

    def test_one_file_several_matches_print_line_numbers_flag(self):
        self.assertMultiLineEqual(
            grep("may", [MIDSUMMERNIGHTFILENAME], "-n"),
            ("3:Nor how it may concern my modesty,\n"
             "5:But I beseech your grace that I may know\n"
             "6:The worst that may befall me in this case,\n"))

    def test_one_file_several_matches_match_entire_lines_flag(self):
        self.assertMultiLineEqual(
            grep("may", [MIDSUMMERNIGHTFILENAME], "-x"), "")

    def test_one_file_several_matches_case_insensitive_flag(self):
        self.assertMultiLineEqual(
            grep("ACHILLES", [ILIADFILENAME], "-i"),
            ("Achilles sing, O Goddess! Peleus' son;\n"
             "The noble Chief Achilles from the son\n"))

    def test_one_file_several_matches_inverted_flag(self):
        self.assertMultiLineEqual(
            grep("Of", [PARADISELOSTFILENAME], "-v"),
            ("Brought Death into the World, and all our woe,\n"
             "With loss of Eden, till one greater Man\n"
             "Restore us, and regain the blissful Seat,\n"
             "Sing Heav'nly Muse, that on the secret top\n"
             "That Shepherd, who first taught the chosen Seed\n"))

    def test_one_file_no_matches_various_flags(self):
        self.assertMultiLineEqual(
            grep("Gandalf", [ILIADFILENAME], "-n -l -x -i"), "")

    def test_multiple_files_one_match_no_flags(self):
        self.assertMultiLineEqual(
            grep(
                "Agamemnon",
                [ILIADFILENAME, MIDSUMMERNIGHTFILENAME, PARADISELOSTFILENAME]),
            "iliad.txt:Of Atreus, Agamemnon, King of men.\n")

    def test_multiple_files_several_matches_no_flags(self):
        self.assertMultiLineEqual(
            grep("may",
                 ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"]),
            ("midsummer-night.txt:Nor how it may concern my modesty,\n"
             "midsummer-night.txt:But I beseech your grace that I may know\n"
             "midsummer-night.txt:The worst that may befall me in this case,\n"
             ))

    def test_multiple_files_several_matches_print_line_numbers_flag(self):
        self.assertMultiLineEqual(
            grep("that",
                 ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
                 "-n"),
            ("midsummer-night.txt:5:But I beseech your grace that I may know\n"
             "midsummer-night.txt:6:The worst that may befall me in this case,"
             "\nparadise-lost.txt:2:Of that Forbidden Tree, whose mortal tast"
             "\nparadise-lost.txt:6:Sing Heav'nly Muse, that on the secret top"
             "\n"))

    def test_multiple_files_one_match_print_file_names_flag(self):
        self.assertMultiLineEqual(
            grep("who",
                 ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
                 "-l"), ILIADFILENAME + '\n' + PARADISELOSTFILENAME + '\n')

    def test_multiple_files_several_matches_case_insensitive_flag(self):
        self.assertMultiLineEqual(
            grep("TO",
                 ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
                 "-i"),
            ("iliad.txt:Caused to Achaia's host, sent many a soul\n"
             "iliad.txt:Illustrious into Ades premature,\n"
             "iliad.txt:And Heroes gave (so stood the will of Jove)\n"
             "iliad.txt:To dogs and to all ravening fowls a prey,\n"
             "midsummer-night.txt:I do entreat your grace to pardon me.\n"
             "midsummer-night.txt:In such a presence here to plead my thoughts"
             ";\nmidsummer-night.txt:If I refuse to wed Demetrius.\n"
             "paradise-lost.txt:Brought Death into the World, and all our woe,"
             "\nparadise-lost.txt:Restore us, and regain the blissful Seat,\n"
             "paradise-lost.txt:Sing Heav'nly Muse, that on the secret top\n"))

    def test_multiple_files_several_matches_inverted_flag(self):
        self.assertMultiLineEqual(
            grep(
                "a", ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
                "-v"), ("iliad.txt:Achilles sing, O Goddess! Peleus' son;\n"
                        "iliad.txt:The noble Chief Achilles from the son\n"
                        "midsummer-night.txt:If I refuse to wed Demetrius.\n"))

    def test_multiple_files_one_match_match_entire_lines_flag(self):
        self.assertMultiLineEqual(
            grep("But I beseech your grace that I may know",
                 ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
                 "-x"),
            "midsummer-night.txt:But I beseech your grace that I may know\n")

    def test_multiple_files_one_match_multiple_flags(self):
        self.assertMultiLineEqual(
            grep("WITH LOSS OF EDEN, TILL ONE GREATER MAN",
                 ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
                 "-n -i -x"),
            "paradise-lost.txt:4:With loss of Eden, till one greater Man\n")

    def test_multiple_files_no_matches_various_flags(self):
        self.assertMultiLineEqual(
            grep("Frodo",
                 ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
                 "-n -l -x -i"), "")


if __name__ == '__main__':
    unittest.main()
