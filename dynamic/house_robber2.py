from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_compute(nums[0:-1]), self.rob_compute(nums[1:]))

    def rob_compute(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        best_option = dp[0]

        for i in range(1, len(nums)):
            best_option = max(best_option, nums[i])

            if i >= 2:
                best_option = max(best_option, dp[i-2]+nums[i])

            if i >= 3:
                best_option = max(best_option, dp[i-3]+nums[i])

            dp.append(best_option)

        return best_option