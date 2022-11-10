import pytest

from dynamic.target_sum import Solution


@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([1, 1, 1, 1, 1], 3, 5),
        ([1, 1, 1], 3, 1),
        ([1], 1, 1),
        ([1, 2, 3], 6, 1),
        ([0, 1], 1, 2),
        ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256)
    ],
)
def test_find_target_sum_ways(arr, target, expected):
    # given
    solution = Solution()
    # when
    result = solution.findTargetSumWays(arr, target)
    # then
    assert result == expected
