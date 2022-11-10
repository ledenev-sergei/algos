import pytest

from greedy.luck_balance import luckBalance


@pytest.mark.parametrize(
    "k,contests,expected",
    [
        (3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]], 29),
    ],
)
def test_luck_balance(k, contests, expected):
    # given
    # when
    result = luckBalance(k, contests)
    # then
    assert result == expected
