from typing import List

import pytest

from sample.fizz_buzz import fizzBuzzSolution


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, ["1"]),  # is not a multiply 3 or 5
        (2, ["1", "2"]),  # is not a multiply 3 or 5
        (3, ["1", "2", "Fizz"]),  # multiply of 3 (but not 5)
        (5, ["1", "2", "Fizz", "4", "Buzz"]),  # multiply of 5 (but not 3)
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),  # multiply of 5 (but not 3)
    ],
)
def test_fizz_buzz_solution(n: int, expected: List[str]):
    # given
    # when
    result = list(fizzBuzzSolution(n))
    # then
    assert result == expected
