# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import hello_world


class HelloWorldTests(unittest.TestCase):

    def test_hello_without_name(self):
        self.assertEqual(
            'Hello, World!',
            hello_world.hello()
        )

    def test_hello_with_sample_name(self):
        self.assertEqual(
            'Hello, Alice!',
            hello_world.hello('Alice')
        )

    def test_hello_with_other_sample_name(self):
        self.assertEqual(
            'Hello, Bob!',
            hello_world.hello('Bob')
        )

    def test_hello_with_umlaut_name(self):
        self.assertEqual(
            'Hello, Jürgen!',
            hello_world.hello('Jürgen')
        )

    def test_hello_with_blank_name(self):
        self.assertEqual(
            'Hello, World!',
            hello_world.hello('')
        )

    def test_hello_with_none_name(self):
        self.assertEqual(
            'Hello, World!',
            hello_world.hello(None)
        )


if __name__ == '__main__':
    unittest.main()
