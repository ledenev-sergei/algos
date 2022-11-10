from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]

        for x in range(2, len(cost)):
            dp.append(min(dp[x-1], dp[x-2])+cost[x])

        return min(dp[-1], dp[-2])