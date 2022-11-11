import pytest

from arrays import remove_dublicates


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([1, 1], 1),
    ],
)
def test_set_zeroes(nums, expected):
    # given
    solution = remove_dublicates.Solution()
    # when
    result = solution.removeDuplicates(nums)
    # then
    assert result == expected
