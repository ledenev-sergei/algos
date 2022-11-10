from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        local_max, local_min = nums[0], nums[0]

        result = local_max

        for i in range(1, len(nums)):
            current = nums[i]

            temp_max = max(current, current*local_max, current*local_min)

            local_min = min(current,  current*local_max, current*local_min)

            local_max = temp_max

            result = max(result, local_max)

        return result








