"""
A test script for lab 23

Run this test script to make sure everything is working properly.

Author: Walker White (wmw2)
Date:   November 2, 2021
"""
import introcs
import funcs


def test_is_date():
    """
    Tests the is_date function
    """
    print('Testing the function is_date')

    introcs.assert_equals(True, funcs.is_date(2026, 11, 16))
    introcs.assert_equals(True, funcs.is_date(2026, 1, 31))
    introcs.assert_equals(False, funcs.is_date(2026, 4, 31)),
    introcs.assert_equals(False, funcs.is_date(2026, 1, 0))
    introcs.assert_equals(False, funcs.is_date(2026, 13, 1))
    introcs.assert_equals(False, funcs.is_date(0, 1, 1)),
    introcs.assert_equals(True, funcs.is_date(2024, 2, 29))
    introcs.assert_equals(False, funcs.is_date(2025, 2, 29)),
    introcs.assert_equals(False, funcs.is_date(1900, 2, 29)),
    introcs.assert_equals(True, funcs.is_date(2000, 2, 29))


def test_get_previous():
    """
    Tests the get_previous function
    """
    print('Testing the function get_previous')

    introcs.assert_equals(22,   funcs.get_previous('file_good.txt'))
    introcs.assert_equals('ABC',funcs.get_previous('file_bad.txt'))
    introcs.assert_equals(None, funcs.get_previous('file_huh.txt'))

    fail = False
    try:
        funcs.get_previous(12)
        fail = True
    except AssertionError:
        pass
    except:
        introcs.quit_with_error('Function get_previous is not enforcing preconditions.')

    if fail:
        introcs.quit_with_error('Function get_previous is not enforcing preconditions.')



def test_limited_error():
    """
    Tests the LimitedUnavailableError class
    """
    print('Testing the class LimitedUnavailableError')

    if not hasattr(funcs,'LimitedUnavailableError'):
        introcs.quit_with_error('funcs is missing the class LimitedUnavailableError.')

    if type(funcs.LimitedUnavailableError) != type:
        introcs.quit_with_error('LimitedUnavailableError is not a class.')

    introcs.assert_equals((1,), funcs.LimitedUnavailableError(1).args)
    introcs.assert_equals((1,2),funcs.LimitedUnavailableError(1,2).args)


def test_limited_class():
    """
    Tests the initializer of the class Limited
    """
    print('Testing the class Limited')

    introcs.assert_equals(1,funcs.Limited(1).x)
    introcs.assert_equals(3,funcs.Limited.AVAILABLE)
    introcs.assert_equals(2,funcs.Limited(2).x)
    introcs.assert_equals(2,funcs.Limited.AVAILABLE)
    introcs.assert_equals(3,funcs.Limited(3).x)
    introcs.assert_equals(1,funcs.Limited.AVAILABLE)
    introcs.assert_equals(4,funcs.Limited(4).x)
    introcs.assert_equals(0,funcs.Limited.AVAILABLE)

    fail = False
    try:
        funcs.Limited(1)
        fail = True
    except funcs.LimitedUnavailableError:
        pass
    except:
        introcs.quit_with_error('Limited raised an error other than LimitedUnavailableError')
    if fail:
        introcs.quit_with_error('Limited continued to create objects after the AVAILABLE is 0')

    fail = False
    try:
        funcs.Limited('a')
        fail = True
    except funcs.LimitedUnavailableError:
        introcs.quit_with_error('The initializer for Limited is not enforcing preconditions.')
    except AssertionError:
        pass
    if fail:
        introcs.quit_with_error('The initializer for Limited is not enforcing preconditions.')


def test_point2_equals():
    """
    Tests the equals1 method of class Point2.
    """
    print('Testing the method equals1 in Point2')

    class SubPoint(funcs.Point2):
        """Subclass to test"""
        pass

    p = funcs.Point2(1,2)
    introcs.assert_true(p == p)
    introcs.assert_true(p == funcs.Point2(1,2))
    introcs.assert_false(p == funcs.Point2(1,4))
    introcs.assert_false(p == funcs.Point2(3,2))
    introcs.assert_false(p == funcs.Point2(3,4))
    introcs.assert_false(p == 2)
    introcs.assert_true(p == SubPoint(1,2))


# Script code
if __name__ == '__main__':
    test_is_date()
    test_get_previous()
    test_limited_error()
    test_limited_class()
    test_point2_equals()

    print('The module funcs passed all tests')
