from typing import List

import pytest

from dynamic.maximum_subarray import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23)
    ],
)
def test_max_sub_array(nums: List[int], expected):
    # given
    solution = Solution()
    # when
    result = solution.maxSubArray(nums)
    # then
    assert result == expected
