import unittest

from two_bucket import TwoBucket


class TwoBucketTest(unittest.TestCase):

    def test_bucket_1_size_3_bucket_2_size_5_goal_1_start_bucket_1(self):
        two_bucket = TwoBucket(3, 5, 1, 'one')
        self.assertEqual(4, two_bucket.moves())
        self.assertEqual('one', two_bucket.goal_bucket)
        self.assertEqual(5, two_bucket.other_bucket)

    def test_bucket_1_size_3_bucket_2_size_5_goal_1_start_bucket_2(self):
        two_bucket = TwoBucket(3, 5, 1, 'two')
        self.assertEqual(8, two_bucket.moves())
        self.assertEqual('two', two_bucket.goal_bucket)
        self.assertEqual(3, two_bucket.other_bucket)

    def test_bucket_1_size_7_bucket_2_size_11_goal_2_start_bucket_1(self):
        two_bucket = TwoBucket(7, 11, 2, 'one')
        self.assertEqual(14, two_bucket.moves())
        self.assertEqual('one', two_bucket.goal_bucket)
        self.assertEqual(11, two_bucket.other_bucket)

    def test_bucket_1_size_7_bucket_2_size_11_goal_2_start_bucket_2(self):
        two_bucket = TwoBucket(7, 11, 2, 'two')
        self.assertEqual(18, two_bucket.moves())
        self.assertEqual('two', two_bucket.goal_bucket)
        self.assertEqual(7, two_bucket.other_bucket)

    def test_bucket_1_size_1_bucket_2_size_3_goal_3_start_bucket_2(self):
        two_bucket = TwoBucket(1, 3, 3, 'two')
        self.assertEqual(1, two_bucket.moves())
        self.assertEqual('two', two_bucket.goal_bucket)
        self.assertEqual(0, two_bucket.other_bucket)

    def test_bucket_1_size_2_bucket_2_size_3_goal_3_start_bucket_1(self):
        two_bucket = TwoBucket(2, 3, 3, 'one')
        self.assertEqual(4, two_bucket.moves())
        self.assertEqual('two', two_bucket.goal_bucket)
        self.assertEqual(1, two_bucket.other_bucket)


if __name__ == '__main__':
    unittest.main()
