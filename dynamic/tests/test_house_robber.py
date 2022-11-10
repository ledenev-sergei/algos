import pytest

from dynamic import house_robber


"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ],
)
def test_climb_stairs(nums, expected):
    # given
    solution = house_robber.Solution()
    # when
    result = solution.rob(nums)
    # then
    assert result == expected
