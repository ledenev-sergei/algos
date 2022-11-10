from typing import Tuple

import pytest

from hashmaps.frequency_queries import freqQuery


@pytest.mark.parametrize(
    "queries,expected",
    [
        ([
            (1, 5),
            (1, 6),
            (3, 2),
            (1, 10),
            (1, 10),
            (1, 6),
            (2, 5),
            (3, 2)
          ], [0, 1]),
    ],
)
def test_freq_query(queries: Tuple[int, int], expected: int):
    # given
    # when
    result = freqQuery(queries)

    # then
    assert result == expected

