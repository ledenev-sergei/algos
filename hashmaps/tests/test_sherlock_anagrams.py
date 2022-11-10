import pytest

from hashmaps.sherlock_anagrams import sherlockAndAnagrams


@pytest.mark.parametrize(
    "input_string,expected",
    [("abba", 4), ("kkkk", 10), ],
)
def test_sherlock_and_anagrams(input_string: str, expected: int):
    # given

    # when
    result = sherlockAndAnagrams(input_string)

    # then
    assert result == expected
