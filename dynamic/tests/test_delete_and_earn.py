import pytest

from dynamic import delete_and_earn


"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
"""

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),
        ([3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10], 66),
        ([1, 1, 1, 2, 4, 5, 5, 5, 6], 18),
        ([3, 1], 4),
        ([1, 6, 3, 3, 8, 4, 8, 10, 1, 3], 43),
        ([4, 10, 10, 8, 1, 4, 10, 9, 7, 6], 53),
        ([17, 15, 21, 61, 51, 69, 42, 48, 97, 88, 2, 35, 29, 72, 49, 76, 54, 72, 30, 94, 20, 72, 21, 65, 80, 31, 11, 81, 14, 43, 39, 83, 45, 29, 94, 76, 81, 1, 97, 48, 71, 88, 44, 34, 53, 62, 25, 1, 81, 79, 58, 24, 99, 15, 46, 63, 10, 11, 50, 19, 91, 56, 44, 56, 86, 35, 76, 22, 52, 27, 52, 60, 84, 15, 38, 80, 99, 1, 38, 86, 79, 85, 43, 16, 61, 68, 41, 8, 67, 29, 63, 64, 70, 91, 24, 79, 14, 62, 11, 41], 3765)
    ],
)
def test_climb_stairs(nums, expected):
    # given
    solution = delete_and_earn.Solution()
    # when
    result = solution.deleteAndEarn(nums)
    # then
    assert result == expected
