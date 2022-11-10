from heap import kth_smallest_element_in_sorted_matrix


def test_kth_smallest_case_one():
    # given
    solution = kth_smallest_element_in_sorted_matrix.Solution()

    # when
    result = solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)

    # then
    assert result == 13


def test_kth_smallest_case_two():
    # given
    solution = kth_smallest_element_in_sorted_matrix.Solution()

    # when
    result = solution.kthSmallest([[-5]], 1)

    # then
    assert result == -5


def test_kth_smallest_case_three():
    # given
    solution = kth_smallest_element_in_sorted_matrix.Solution()

    # when
    result = solution.kthSmallest([[1, 2], [1, 3]], 2)

    # then
    assert result == 1
