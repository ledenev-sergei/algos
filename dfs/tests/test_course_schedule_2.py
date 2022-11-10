import pytest

from dfs.course_schedule_2 import Solution


@pytest.mark.parametrize(
    "numCourses,prerequisites,expected",
    [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
        (1, [], [0])
    ],
)
def test_can_finish(numCourses, prerequisites, expected):
    # given
    solution = Solution()
    # when
    result = solution.findOrder(numCourses, prerequisites)
    # then
    assert result == expected