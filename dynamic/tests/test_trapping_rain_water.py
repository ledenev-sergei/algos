import pytest

from dynamic.trapping_rain_water import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ],
)
def test_trap(nums, expected):
    # given
    solution = Solution()
    # when
    result = solution.trap(nums)
    # then
    assert result == expected
