from bfs import number_of_islands


def test_should_find_one_island():
    # given
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    solution = number_of_islands.Solution()

    # when
    result = solution.numIslands(grid)
    pass

    # then
    assert result == 1


def test_should_find_three_islands():
    # given
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    solution = number_of_islands.Solution()

    # when
    result = solution.numIslands(grid)
    pass

    # then
    assert result == 3

def test_should_return_one_island_case2():
    # given
    grid = [
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]
    ]
    solution = number_of_islands.SolutionWoVisitedNodes()

    # when
    result = solution.numIslands(grid)
    pass

    # then
    assert result == 1

