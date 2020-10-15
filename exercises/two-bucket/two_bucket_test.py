import unittest

from two_bucket import measure

# Tests adapted from `problem-specifications//canonical-data.json`


class TwoBucketTest(unittest.TestCase):
    def test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_one(
        self
    ):
        self.assertEqual(measure(3, 5, 1, "one"), (4, "one", 5))

    def test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_two(
        self
    ):
        self.assertEqual(measure(3, 5, 1, "two"), (8, "two", 3))

    def test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_one(
        self
    ):
        self.assertEqual(measure(7, 11, 2, "one"), (14, "one", 11))

    def test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_two(
        self
    ):
        self.assertEqual(measure(7, 11, 2, "two"), (18, "two", 7))

    def test_measure_one_step_using_bucket_one_of_size_1_and_bucket_two_of_size_3_start_with_bucket_two(
        self
    ):
        self.assertEqual(measure(1, 3, 3, "two"), (1, "two", 0))

    def test_measure_using_bucket_one_of_size_2_and_bucket_two_of_size_3_start_with_bucket_one_and_end_with_bucket_two(
        self
    ):
        self.assertEqual(measure(2, 3, 3, "one"), (2, "two", 2))


if __name__ == "__main__":
    unittest.main()
