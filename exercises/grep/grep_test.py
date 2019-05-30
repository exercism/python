import unittest
try:
    import builtins
except ImportError:
    import __builtin__ as builtins

from grep import grep


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

ILIADFILENAME = 'iliad.txt'
ILIADCONTENTS = '''Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men.'''

MIDSUMMERNIGHTFILENAME = 'midsummer-night.txt'
MIDSUMMERNIGHTCONTENTS = '''I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius.'''

PARADISELOSTFILENAME = 'paradise-lost.txt'
PARADISELOSTCONTENTS = '''Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed'''
FILENAMES = [
    ILIADFILENAME,
    MIDSUMMERNIGHTFILENAME,
    PARADISELOSTFILENAME,
]
FILES = {}


class File(object):
    def __init__(self, name=''):
        self.name = name
        self.contents = ''

    def read(self):
        return self.contents

    def readlines(self):
        return [line + '\n' for line in self.read().split('\n') if line]

    def write(self, data):
        self.contents += data

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


# Store builtin definition of open()
builtins.oldopen = builtins.open


def open(name, mode='r', *args, **kwargs):
    # if name is a mocked file name, lookup corresponding mocked file
    if name in FILENAMES:
        if mode == 'w' or name not in FILES:
            FILES[name] = File(name)
        return FILES[name]
    # else call builtin open()
    else:
        return builtins.oldopen(name, mode, *args, **kwargs)


builtins.open = open


# remove mocked file contents
def remove_file(file_name):
    del FILES[file_name]


def create_file(name, contents):
    with open(name, 'w') as f:
        f.write(contents)


class GrepTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Override builtin open() with mock-file-enabled one
        builtins.open = open
        create_file(ILIADFILENAME, ILIADCONTENTS)
        create_file(MIDSUMMERNIGHTFILENAME, MIDSUMMERNIGHTCONTENTS)
        create_file(PARADISELOSTFILENAME, PARADISELOSTCONTENTS)
        self.maxDiff = None

    @classmethod
    def tearDownClass(self):
        remove_file(ILIADFILENAME)
        remove_file(MIDSUMMERNIGHTFILENAME)
        remove_file(PARADISELOSTFILENAME)
        # Restore builtin open()
        builtins.open = builtins.oldopen

    def test_one_file_one_match_no_flags(self):
        self.assertMultiLineEqual(
            grep("Agamemnon", "", [ILIADFILENAME]),
            "Of Atreus, Agamemnon, King of men.\n"
        )

    def test_one_file_one_match_print_line_numbers_flag(self):
        self.assertMultiLineEqual(
            grep("Forbidden", "-n", [PARADISELOSTFILENAME]),
            "2:Of that Forbidden Tree, whose mortal tast\n"
        )

    def test_one_file_one_match_case_insensitive_flag(self):
        self.assertMultiLineEqual(
            grep("FORBIDDEN", "-i", [PARADISELOSTFILENAME]),
            "Of that Forbidden Tree, whose mortal tast\n"
        )

    def test_one_file_one_match_print_file_names_flag(self):
        self.assertMultiLineEqual(
            grep("Forbidden", "-l", [PARADISELOSTFILENAME]),
            PARADISELOSTFILENAME + '\n')

    def test_one_file_one_match_match_entire_lines_flag(self):
        self.assertMultiLineEqual(
            grep("With loss of Eden, till one greater Man",
                 "-x", [PARADISELOSTFILENAME]),
            "With loss of Eden, till one greater Man\n")

    def test_one_file_one_match_multiple_flags(self):
        self.assertMultiLineEqual(
            grep("OF ATREUS, Agamemnon, KIng of MEN.",
                 "-n -i -x", [ILIADFILENAME]),
            "9:Of Atreus, Agamemnon, King of men.\n")

    def test_one_file_several_matches_no_flags(self):
        self.assertMultiLineEqual(
            grep("may", "", [MIDSUMMERNIGHTFILENAME]),
            "Nor how it may concern my modesty,\n"
            "But I beseech your grace that I may know\n"
            "The worst that may befall me in this case,\n")

    def test_one_file_several_matches_print_line_numbers_flag(self):
        self.assertMultiLineEqual(
            grep("may", "-n", [MIDSUMMERNIGHTFILENAME]),
            "3:Nor how it may concern my modesty,\n"
            "5:But I beseech your grace that I may know\n"
            "6:The worst that may befall me in this case,\n")

    def test_one_file_several_matches_match_entire_lines_flag(self):
        self.assertMultiLineEqual(
            grep("may", "-x", [MIDSUMMERNIGHTFILENAME]),
            "")

    def test_one_file_several_matches_case_insensitive_flag(self):
        self.assertMultiLineEqual(
            grep("ACHILLES", "-i", [ILIADFILENAME]),
            "Achilles sing, O Goddess! Peleus' son;\n"
            "The noble Chief Achilles from the son\n")

    def test_one_file_several_matches_inverted_flag(self):
        self.assertMultiLineEqual(
            grep("Of", "-v", [PARADISELOSTFILENAME]),
            "Brought Death into the World, and all our woe,\n"
            "With loss of Eden, till one greater Man\n"
            "Restore us, and regain the blissful Seat,\n"
            "Sing Heav'nly Muse, that on the secret top\n"
            "That Shepherd, who first taught the chosen Seed\n")

    def test_one_file_one_match_file_flag_takes_precedence_over_line(self):
        self.assertMultiLineEqual(
            grep("ten",  "-n -l", [ILIADFILENAME]),
            ILIADFILENAME + '\n')

    def test_one_file_no_matches_various_flags(self):
        self.assertMultiLineEqual(
            grep("Gandalf", "-n -l -x -i", [ILIADFILENAME]),
            "")

    def test_multiple_files_one_match_no_flags(self):
        self.assertMultiLineEqual(
            grep("Agamemnon", "", FILENAMES),
            "iliad.txt:Of Atreus, Agamemnon, King of men.\n")

    def test_multiple_files_several_matches_no_flags(self):
        self.assertMultiLineEqual(
            grep("may", "", FILENAMES),
            "midsummer-night.txt:Nor how it may concern my modesty,\n"
            "midsummer-night.txt:But I beseech your grace that I may know\n"
            "midsummer-night.txt:The worst that may befall me in this case,\n")

    def test_multiple_files_several_matches_print_line_numbers_flag(self):
        expected = (
            "midsummer-night.txt:5:But I beseech your grace that I may know\n"
            "midsummer-night.txt:6:The worst that may befall me in this case,"
            "\nparadise-lost.txt:2:Of that Forbidden Tree, whose mortal tast\n"
            "paradise-lost.txt:6:Sing Heav'nly Muse, that on the secret top\n")
        self.assertMultiLineEqual(grep("that", "-n", FILENAMES), expected)

    def test_multiple_files_one_match_print_file_names_flag(self):
        self.assertMultiLineEqual(
            grep("who", "-l", FILENAMES),
            ILIADFILENAME + '\n' + PARADISELOSTFILENAME + '\n')

    def test_multiple_files_several_matches_case_insensitive_flag(self):
        expected = (
            "iliad.txt:Caused to Achaia's host, sent many a soul\n"
            "iliad.txt:Illustrious into Ades premature,\n"
            "iliad.txt:And Heroes gave (so stood the will of Jove)\n"
            "iliad.txt:To dogs and to all ravening fowls a prey,\n"
            "midsummer-night.txt:I do entreat your grace to pardon me.\n"
            "midsummer-night.txt:In such a presence here to plead my thoughts;"
            "\nmidsummer-night.txt:If I refuse to wed Demetrius.\n"
            "paradise-lost.txt:Brought Death into the World, and all our woe,"
            "\nparadise-lost.txt:Restore us, and regain the blissful Seat,\n"
            "paradise-lost.txt:Sing Heav'nly Muse, that on the secret top\n")
        self.assertMultiLineEqual(grep("TO", "-i", FILENAMES), expected)

    def test_multiple_files_several_matches_inverted_flag(self):
        self.assertMultiLineEqual(
            grep("a", "-v", FILENAMES),
            "iliad.txt:Achilles sing, O Goddess! Peleus' son;\n"
            "iliad.txt:The noble Chief Achilles from the son\n"
            "midsummer-night.txt:If I refuse to wed Demetrius.\n"
        )

    def test_multiple_files_one_match_match_entire_lines_flag(self):
        self.assertMultiLineEqual(
            grep("But I beseech your grace that I may know", "-x", FILENAMES),
            "midsummer-night.txt:But I beseech your grace that I may know\n")

    def test_multiple_files_one_match_multiple_flags(self):
        self.assertMultiLineEqual(
            grep("WITH LOSS OF EDEN, TILL ONE GREATER MAN",  "-n -i -x",
                 FILENAMES),
            "paradise-lost.txt:4:With loss of Eden, till one greater Man\n")

    def test_multiple_files_no_matches_various_flags(self):
        self.assertMultiLineEqual(
            grep("Frodo", "-n -l -x -i", FILENAMES),
            ""
        )

    def test_multiple_files_several_matches_file_flag_takes_precedence(self):
        self.assertMultiLineEqual(
            grep("who", "-n -l", FILENAMES),
            ILIADFILENAME + '\n' + PARADISELOSTFILENAME + '\n')

    def test_multiple_files_several_matches_inverted_match_entire_lines(self):
        expected = (
            "iliad.txt:Achilles sing, O Goddess! Peleus' son;\n"
            "iliad.txt:His wrath pernicious, who ten thousand woes\n"
            "iliad.txt:Caused to Achaia's host, sent many a soul\n"
            "iliad.txt:And Heroes gave (so stood the will of Jove)\n"
            "iliad.txt:To dogs and to all ravening fowls a prey,\n"
            "iliad.txt:When fierce dispute had separated once\n"
            "iliad.txt:The noble Chief Achilles from the son\n"
            "iliad.txt:Of Atreus, Agamemnon, King of men.\n"
            "midsummer-night.txt:I do entreat your grace to pardon me.\n"
            "midsummer-night.txt:I know not by what power I am made bold,\n"
            "midsummer-night.txt:Nor how it may concern my modesty,\n"
            "midsummer-night.txt:In such a presence here to plead my thoughts;"
            "\nmidsummer-night.txt:But I beseech your grace that I may know\n"
            "midsummer-night.txt:The worst that may befall me in this case,\n"
            "midsummer-night.txt:If I refuse to wed Demetrius.\n"
            "paradise-lost.txt:Of Mans First Disobedience, and the Fruit\n"
            "paradise-lost.txt:Of that Forbidden Tree, whose mortal tast\n"
            "paradise-lost.txt:Brought Death into the World, and all our woe,"
            "\nparadise-lost.txt:With loss of Eden, till one greater Man\n"
            "paradise-lost.txt:Restore us, and regain the blissful Seat,\n"
            "paradise-lost.txt:Sing Heav'nly Muse, that on the secret top\n"
            "paradise-lost.txt:Of Oreb, or of Sinai, didst inspire\n"
            "paradise-lost.txt:That Shepherd, who first taught the chosen Seed"
            "\n"
        )
        self.assertMultiLineEqual(
            grep("Illustrious into Ades premature,", "-x -v", FILENAMES),
            expected
        )


if __name__ == '__main__':
    unittest.main()
