from typing import List

import pytest

from dynamic.maximum_product_subarray import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1], 1),
        ([-2], -2),
        ([0, 2], 2),
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([2, 3, -2, 1, -3], 36),
        ([2, 3, -2, 5, 6], 30),
        ([[2, -5, -2, -4, 3], 24])
    ],
)
def test_max_product_subarray(nums: List[int], expected):
    # given
    solution = Solution()
    # when
    result = solution.maxProduct(nums)
    # then
    assert result == expected
