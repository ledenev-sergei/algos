from heap import top_k_frequent_elements


def test_top_kfrequent():
    # given
    solution = top_k_frequent_elements.Solution()

    # when
    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)

    # then
    assert result == [1, 2]
