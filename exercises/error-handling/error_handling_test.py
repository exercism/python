import unittest

import error_handling as er


class FileLike:
    def __init__(self, fail_something=True):
        self.is_open = False
        self.was_open = False
        self.did_something = False
        self.fail_something = fail_something

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
        if self.fail_something:
            raise Exception("Failed while doing something")


class ErrorHandlingTest(unittest.TestCase):
    def test_throw_exception(self):
        with self.assertRaisesWithMessage(Exception):
            er.handle_error_by_throwing_exception()

    def test_return_none(self):
        self.assertEqual(er.handle_error_by_returning_none('1'), 1,
                         'Result of valid input should not be None')
        self.assertIsNone(er.handle_error_by_returning_none('a'),
                          'Result of invalid input should be None')

    def test_return_tuple(self):
        successful_result, result = er.handle_error_by_returning_tuple('1')
        self.assertIs(successful_result, True,
                      'Valid input should be successful')
        self.assertEqual(result, 1, 'Result of valid input should not be None')

        failure_result, result = er.handle_error_by_returning_tuple('a')
        self.assertIs(failure_result, False,
                      'Invalid input should not be successful')

    def test_filelike_objects_are_closed_on_exception(self):
        filelike_object = FileLike(fail_something=True)
        with self.assertRaisesWithMessage(Exception):
            er.filelike_objects_are_closed_on_exception(filelike_object)
        self.assertIs(filelike_object.is_open, False,
                      'filelike_object should be closed')
        self.assertIs(filelike_object.was_open, True,
                      'filelike_object should have been opened')
        self.assertIs(filelike_object.did_something, True,
                      'filelike_object should call do_something()')

    def test_filelike_objects_are_closed_without_exception(self):
        filelike_object = FileLike(fail_something=False)
        er.filelike_objects_are_closed_on_exception(filelike_object)
        self.assertIs(filelike_object.is_open, False,
                      'filelike_object should be closed')
        self.assertIs(filelike_object.was_open, True,
                      'filelike_object should have been opened')
        self.assertIs(filelike_object.did_something, True,
                      'filelike_object should call do_something()')

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
