from bfs import average_of_levels


def test_average_of_levels():
    # given
    tree = average_of_levels.TreeNode(
        3,
        average_of_levels.TreeNode(9),
        average_of_levels.TreeNode(20,
                                   average_of_levels.TreeNode(15),
                                   average_of_levels.TreeNode(7)
        )
    )
    solution = average_of_levels.Solution()

    # when
    result = solution.averageOfLevels(tree)

    # then
    assert result == [3, 14.5, 11]
