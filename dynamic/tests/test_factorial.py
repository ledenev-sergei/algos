import pytest

import timeit
import logging as log

from dynamic import factorial


"""
Factorial function is defined recurcivly for all non-negative integers as
Fact(n) = n * Fact(n-1) if n > 1
        = 1             if n = 1

Write both recursive and non-recursive function that accepts and unsigned int n and return factorial of n
"""

@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_recursive(n, expected):
    # given
    solution = factorial.Solution()
    # when
    result_recursive = solution.recursive(n)
    # then
    assert result_recursive == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_non_recursive(n, expected):
    # given
    solution = factorial.Solution()
    # when
    result_non_recursive = solution.nonRecursive(n)

    # then
    assert result_non_recursive == expected