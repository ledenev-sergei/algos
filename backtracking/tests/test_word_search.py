import pytest

from backtracking.word_search import Solution


@pytest.mark.parametrize(
    "board,word,expected",
    [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
        ([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS", True)
    ],
)
def test_can_finish(board, word, expected):
    # given
    solution = Solution()
    # when
    result = solution.exist(board, word)
    # then
    assert result == expected