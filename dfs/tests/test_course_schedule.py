import pytest

from dfs.course_schedule import Solution


@pytest.mark.parametrize(
    "numCourses,prerequisites,expected",
    [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (5, [[1, 4], [2, 4], [3, 1], [3, 2]], True)
    ],
)
def test_can_finish(numCourses, prerequisites, expected):
    # given
    prerequisites
    solution = Solution()
    # when
    result = solution.canFinish(numCourses, prerequisites)
    # then
    assert result == expected