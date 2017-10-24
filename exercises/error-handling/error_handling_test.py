import unittest

import error_handling as er


class FileLike(object):
    def __init__(self):
        self.is_open = False
        self.was_open = False
        self.did_something = False

    def open(self):
        self.was_open = False
        self.is_open = True

    def close(self):
        self.is_open = False
        self.was_open = True

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def do_something(self):
        self.did_something = True
        raise Exception()


class ErrorHandlingTest(unittest.TestCase):
    def test_throw_exception(self):
        with self.assertRaises(Exception):
            er.handle_error_by_throwing_exception()

    def test_return_none(self):
        self.assertEqual(1, er.handle_error_by_returning_none('1'),
                         'Result of valid input should not be None')
        self.assertIsNone(er.handle_error_by_returning_none('a'),
                          'Result of invalid input should be None')

    def test_return_tuple(self):
        successful_result, result = er.handle_error_by_returning_tuple('1')
        self.assertIs(True, successful_result,
                      'Valid input should be successful')
        self.assertEqual(1, result, 'Result of valid input should not be None')

        failure_result, result = er.handle_error_by_returning_tuple('a')
        self.assertIs(False, failure_result,
                      'Invalid input should not be successful')

    def test_filelike_objects_are_closed_on_exception(self):
        filelike_object = FileLike()
        with self.assertRaises(Exception):
            er.filelike_objects_are_closed_on_exception(filelike_object)
        self.assertIs(False, filelike_object.is_open,
                      'filelike_object should be closed')
        self.assertIs(True, filelike_object.was_open,
                      'filelike_object should have been opened')
        self.assertIs(True, filelike_object.did_something,
                      'filelike_object should call do_something()')


if __name__ == '__main__':
    unittest.main()
