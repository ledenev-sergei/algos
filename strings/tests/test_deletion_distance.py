import pytest
from strings import deletion_distance

@pytest.mark.parametrize(
    "str1,str2,expected",
    [
        ("", "", 0),
        ("heat", "hit", 3),
        ("dog", "frog", 3),
        ("some", "some", 0),
        ("some", "thing", 9),
        ("ab", "ba", 2)

    ],
)
def test_deletion_distance(str1, str2, expected):
    # given / when
    result = deletion_distance.deletion_distance(str1, str2)
    # then
    assert result == expected