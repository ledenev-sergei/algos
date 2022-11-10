import pytest

from arrays.set_matrix_zeros import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ],
)
def test_set_zeroes(nums, expected):
    # given
    solution = Solution()
    # when
    solution.setZeroes(nums)
    # then
    assert nums == expected
