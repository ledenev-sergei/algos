import pytest

from dynamic import jump_game2


"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0], 0),
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2)
    ],
)
def test_climb_stairs(nums, expected):
    # given
    solution = jump_game2.Solution()
    # when
    result = solution.jump(nums)
    # then
    assert result == expected
