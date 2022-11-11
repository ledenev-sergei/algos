from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)

        i = 0
        j = 1
        while j < len(nums):
            if nums[i] < nums[j]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
                j += 1
                continue

            if nums[i] == nums[j]:
                nums[j] = -1000
                j += 1
                continue

        return i+1
