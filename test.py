import pytest
from potter import price

def assert_equal(num, result):
    assert num == result

def testBasics():
    assert_equal(0, price([]))
    assert_equal(8, price([1]))
    assert_equal(8, price([2]))
    assert_equal(8, price([3]))
    assert_equal(8, price([4]))
    assert_equal(8 * 3, price([1, 1, 1]))

def testSimpleDiscounts():
    assert_equal(8 * 2 * 0.95, price([0, 1]))
    assert_equal(8 * 3 * 0.9, price([0, 2, 4]))
    assert_equal(8 * 4 * 0.8, price([0, 1, 2, 4]))
    assert_equal(8 * 5 * 0.75, price([0, 1, 2, 3, 4]))


def testSeveralDiscounts():
    assert_equal(8 + (8 * 2 * 0.95), price([0, 0, 1]))
    assert_equal(2 * (8 * 2 * 0.95), price([0, 0, 1, 1]))
    assert_equal((8 * 4 * 0.8) + (8 * 2 * 0.95), price([0, 0, 1, 2, 2, 3]))
    assert_equal(8 + (8 * 5 * 0.75), price([0, 1, 1, 2, 3, 4]))


def testEdgeCases():
    assert_equal(2 * (8 * 4 * 0.8), price([0, 0, 1, 1, 2, 2, 3, 4]))
    assert_equal(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8),
                 price([0, 0, 0, 0, 0,
                        1, 1, 1, 1, 1,
                        2, 2, 2, 2,
                        3, 3, 3, 3, 3,
                        4, 4, 4, 4]))
