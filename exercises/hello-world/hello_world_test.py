import unittest

import hello_world


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class HelloWorldTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world.hello(), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
