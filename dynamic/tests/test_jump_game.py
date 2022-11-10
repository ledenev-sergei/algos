import pytest

from dynamic import jump_game


"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0], True),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False)
    ],
)
def test_climb_stairs(nums, expected):
    # given
    solution = jump_game.Solution()
    # when
    result = solution.canJump(nums)
    # then
    assert result == expected
