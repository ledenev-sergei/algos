from heap import find_k_pairs_with_smallest_sum


def test_k_smallest_pairs():
    # given
    solution = find_k_pairs_with_smallest_sum.Solution()

    # when
    result = solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
    # then
    assert result == [[1, 2], [1, 4], [1, 6]]
