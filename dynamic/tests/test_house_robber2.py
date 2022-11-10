import pytest

from dynamic import house_robber2


"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([1], 1)
    ],
)
def test_climb_stairs(nums, expected):
    # given
    solution = house_robber2.Solution()
    # when
    result = solution.rob(nums)
    # then
    assert result == expected
