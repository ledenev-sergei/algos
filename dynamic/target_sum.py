from functools import lru_cache
from typing import List, Optional


class Solution:
    nums: List[int]
    count: int

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.count = 0
        return self.recursive(len(nums), target)
        #return self.bruteForce(0, 0, target)


    def bruteForce(self, i: int, current_sum: int, target: int):
        if i == len(self.nums):
            if current_sum == target:
                self.count += 1
        return self.count

    @lru_cache(None)
    def recursive(self, i: int, target: int) -> int:
        if i == 1:
            count = 0
            if self.nums[0] == target:
                count += 1
            if -self.nums[0] == target:
                count += 1

            return count

        last_value = self.nums[i-1]
        prev_sum_plus = self.recursive(i-1, target=target-last_value)
        prev_sum_minus = self.recursive(i-1, target=target+last_value)

        return prev_sum_plus + prev_sum_minus
