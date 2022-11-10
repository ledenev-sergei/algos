import pytest

from interview.find_indices import findIndices


@pytest.mark.parametrize(
    "query, n,expected",
    [
        ([[1, 3], [1, 2], [4, 4]], 4, [3, 4]),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 5, [-1])
    ],
)
def test_find_indices(query, n, expected):
    # given
    # when
    result = findIndices(n, query)
    # then
    assert result == expected
