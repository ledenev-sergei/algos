import pytest

from dynamic import min_cost_climbing_stairs


"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

@pytest.mark.parametrize(
    "cost,expected",
    [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ],
)
def test_climb_stairs(cost, expected):
    # given
    solution = min_cost_climbing_stairs.Solution()
    # when
    result = solution.minCostClimbingStairs(cost)
    # then
    assert result == expected
