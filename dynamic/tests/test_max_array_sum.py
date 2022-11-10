from typing import List

import pytest

from dynamic.max_array_sum import maxSubsetSum


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([3, 7, 4, 6, 5], 13),
        ([2, 1, 5, 8, 4], 11),
        ([3, 5, -7, 8, 10], 15),
    ],
)
def test_max_subset_sum(arr: List[int], expected: int):
    # given
    # when
    result = maxSubsetSum(arr)
    # then
    assert result == expected
