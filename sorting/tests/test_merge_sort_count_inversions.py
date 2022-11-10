import pytest

from sorting.merge_sort_count_inversions import countInversions

"""
7 5 3 1
5 7 1 3 - 2
5 1 7 3 - 1
1 5 3 7 - 2
1 3 5 7 - 1
"""
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 1, 1, 2, 2], 0),
        ([2, 1, 3, 1, 2], 4),
        ([7, 5, 3, 1], 6)
    ],
)
def test_count_inversions(arr, expected):
    # given
    # when
    result = countInversions(arr)
    # then
    assert result == expected
