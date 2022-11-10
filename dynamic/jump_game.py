from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        hops_available = 1

        for hops in nums:
            if hops_available == 0:
                return False

            hops_available = max(hops_available-1, hops)

        return True
