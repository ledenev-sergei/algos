from functools import cmp_to_key
from typing import List

from sorting.sorting_comparator import Player


def test_comparator():
    # given
    input_array = [
        Player("amy", 100),
        Player("david", 100),
        Player("heraldo", 50),
        Player("aakansha", 75),
        Player("aleksa", 150),
    ]


    # when
    sorted_array: List[Player] = sorted(input_array, key=cmp_to_key(Player.comparator))

    # then

    assert [p.score for p in sorted_array] == [150, 100, 100, 75, 50]
