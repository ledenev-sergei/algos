import pytest

from dynamic.climbing_stairs import Solution


"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

@pytest.mark.parametrize(
    "n,expected",
    [
        (2, 2),
        (3, 3),
    ],
)
def test_climb_stairs(n, expected):
    # given
    solution = Solution()
    # when
    result = solution.climbStairs(n)
    # then
    assert result == expected
