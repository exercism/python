# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import hello_world


class BobTests(unittest.TestCase):

    def test_hello_without_name(self):
        self.assertEqual(
            'Hello, World!',
            hello_world.hello()
        )

    def test_hello_with_name(self):
        self.assertEqual(
            'Hello, Jane!',
            hello_world.hello('Jane')
        )

    def test_hello_with_umlaut_name(self):
        self.assertEqual(
            'Hello, Jürgen!',
            hello_world.hello('Jürgen')
        )

if __name__ == '__main__':
    unittest.main()
