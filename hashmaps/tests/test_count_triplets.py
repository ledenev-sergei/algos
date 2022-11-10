from typing import List

import pytest

from hashmaps.count_triplets import countTriplets

@pytest.mark.parametrize(
    "arr,r,expected",
    [
        ([1, 2, 2, 4], 2, 2),
        ([1, 3, 9, 9, 27, 81], 3, 6),
        ([1, 5, 5, 25, 125], 5, 4),
        ([1 for n in range(0, 100)], 1, 161700),
        ([1237 for n in range(0, 100000)], 1, 166661666700000)
    ],
)
def test_count_triplets(arr: List[int], r: float, expected: int):
    # given

    # when
    result = countTriplets(arr, r)

    # then
    assert result == expected
