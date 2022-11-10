from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')

        for cur in nums:
            cur_sum += cur

            if cur_sum > max_sum:
                max_sum = cur_sum

            if cur_sum < 0:
                cur_sum = 0

        return max_sum






